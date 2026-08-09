from openai import OpenAI
from context import TWIN_SYSTEM_PROMPT
from tools import tools, handle_tool_calls
from styles import CSS, JS, EXAMPLES
from dotenv import load_dotenv, find_dotenv
import gradio as gr
import os
import modal
from fastapi import FastAPI

load_dotenv(find_dotenv(), override=True)

MODEL_NAME = "openai/gpt-oss-120b"

openai = OpenAI(
    api_key=os.environ.get("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

system = [{"role": "system", "content": TWIN_SYSTEM_PROMPT}]

initial_message = {"role": "assistant", "content": "Hi! I am Rashid's AI Twin. 👋\nFeel free to ask me about his experience, projects, or leave your email and a message for him to reach out to you!"}

def user_interaction(user_message, history):
    return "", history + [{"role": "user", "content": user_message}]

def bot_interaction(history):
    messages = system + history
    response = openai.chat.completions.create(model=MODEL_NAME, messages=messages, tools=tools)
    
    while response.choices[0].finish_reason == "tool_calls":
        message = response.choices[0].message
        tool_calls = message.tool_calls
        results = handle_tool_calls(tool_calls)
        messages.append(message)
        messages.extend(results)
        response = openai.chat.completions.create(model=MODEL_NAME, messages=messages, tools=tools)
        
    history.append({"role": "assistant", "content": response.choices[0].message.content})
    return history

def clear_chat():
    return [initial_message]

def create_btn_click(btn_text):
    def on_click(history):
        return "", history + [{"role": "user", "content": btn_text}]
    return on_click

with gr.Blocks() as demo:
    gr.Markdown("# Meet Rashid AI &nbsp; <span style='font-size: 16px; font-weight: normal; color: #888;'>Chat with my interactive AI Twin to learn about my projects, career, and skills.</span>")
    
    with gr.Row():
        with gr.Column(scale=3):
            chatbot = gr.Chatbot(
                value=[initial_message],
                show_label=False,
                height=600
            )
            msg = gr.Textbox(show_label=False, placeholder="Type your message here...")
            
            with gr.Row():
                submit = gr.Button("Send", variant="primary")
                clear = gr.Button("Clear Chat")
                
        with gr.Column(scale=1):
            gr.Markdown("### 💡 Suggested Questions\n*Click any question below to ask the AI Twin!*")
            for ex in EXAMPLES:
                btn = gr.Button(ex, variant="secondary")
                btn.click(
                    fn=create_btn_click(ex),
                    inputs=[chatbot],
                    outputs=[msg, chatbot]
                ).then(
                    fn=bot_interaction,
                    inputs=[chatbot],
                    outputs=[chatbot]
                )

    msg.submit(
        fn=user_interaction,
        inputs=[msg, chatbot],
        outputs=[msg, chatbot]
    ).then(
        fn=bot_interaction,
        inputs=[chatbot],
        outputs=[chatbot]
    )
    
    submit.click(
        fn=user_interaction,
        inputs=[msg, chatbot],
        outputs=[msg, chatbot]
    ).then(
        fn=bot_interaction,
        inputs=[chatbot],
        outputs=[chatbot]
    )
    
    clear.click(fn=clear_chat, inputs=None, outputs=[chatbot])

# --- MODAL DEPLOYMENT CONFIGURATION ---
app = modal.App("rashid-ai-twin")
image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install_from_requirements("requirements.txt")
    .add_local_dir(".", remote_path="/root")
)

@app.function(
    image=image, 
    secrets=[modal.Secret.from_dotenv()]
)
@modal.asgi_app()
def serve():
    web_app = FastAPI()
    return gr.mount_gradio_app(web_app, demo, path="/")

if __name__ == "__main__":
    demo.launch(css=CSS, js=JS, theme=gr.themes.Base())
