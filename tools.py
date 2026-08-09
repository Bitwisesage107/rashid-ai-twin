import json
import os
import requests
import math
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

load_dotenv(find_dotenv(), override=True)

telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")
# Initialize OpenRouter for embeddings
client = OpenAI(
    api_key=os.environ.get("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)
EMBEDDING_MODEL = "nvidia/llama-nemotron-embed-vl-1b-v2:free"


def push(text):
    if telegram_bot_token and telegram_chat_id:
        try:
            url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
            requests.post(
                url,
                json={
                    "chat_id": telegram_chat_id,
                    "text": text,
                },
            )
        except Exception as e:
            print("Failed to send telegram message:", e)

def record_user_details(email, name="Name not provided", notes="not provided"):
    message = f"Recording interest from {name} with email {email} and notes {notes}"
    push(message)
    
    try:
        email_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "email.txt")
        with open(email_file, "a", encoding="utf-8") as f:
            f.write(message + "\n")
    except Exception as e:
        print("Failed to write to email.txt:", e)
        
    return "OK"


def record_unknown_question(question):
    push(f"Recording {question} asked that I couldn't answer")
    return "OK"


def cosine_similarity(v1, v2):
    dot_product = sum(a * b for a, b in zip(v1, v2))
    norm_v1 = math.sqrt(sum(a * a for a in v1))
    norm_v2 = math.sqrt(sum(b * b for b in v2))
    if norm_v1 == 0 or norm_v2 == 0: return 0
    return dot_product / (norm_v1 * norm_v2)


def search_knowledge_base(query):
    print(f"Agent is searching KB for: {query}")
    try:
        response = client.embeddings.create(
            input=query,
            model=EMBEDDING_MODEL,
            encoding_format="float"
        )
        query_embedding = response.data[0].embedding
        
        kb_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "kb.json")
        if not os.path.exists(kb_path):
            return "Knowledge base not found. Please run build_kb.py first."
            
        with open(kb_path, "r", encoding="utf-8") as f:
            kb = json.load(f)
            
        results = []
        for doc in kb:
            sim = cosine_similarity(query_embedding, doc["embedding"])
            results.append((sim, doc["filename"], doc["content"]))
            
        # Sort by similarity descending
        results.sort(key=lambda x: x[0], reverse=True)
        
        # Return the top 3 results
        top_results = results[:3]
        
        context = "Here is the relevant information from Rashid's knowledge base:\n\n"
        for i, (sim, filename, content) in enumerate(top_results):
            context += f"--- Source: {filename} (Relevance: {sim:.2f}) ---\n"
            context += content + "\n\n"
            
        return context
    except Exception as e:
        return f"Error searching knowledge base: {e}"


record_user_details_json = {
    "name": "record_user_details",
    "description": "Use this tool to record that a user is interested in being in touch and provided an email address",
    "parameters": {
        "type": "object",
        "properties": {
            "email": {"type": "string", "description": "The email address of this user"},
            "name": {"type": "string", "description": "The user's name, if they provided it"},
            "notes": {
                "type": "string",
                "description": "Any additional info about the conversation that's worth recording to give context",
            },
        },
        "required": ["email"],
        "additionalProperties": False,
    },
}

record_unknown_question_json = {
    "name": "record_unknown_question",
    "description": "Always use this tool to record any question that couldn't be answered as you didn't know the answer",
    "parameters": {
        "type": "object",
        "properties": {
            "question": {"type": "string", "description": "The question that couldn't be answered"},
        },
        "required": ["question"],
        "additionalProperties": False,
    },
}

search_knowledge_base_json = {
    "name": "search_knowledge_base",
    "description": "Searches Rashid's documents (resume, projects, about me, etc.) to find factual answers to user questions.",
    "parameters": {
        "type": "object",
        "properties": {
            "query": {"type": "string", "description": "The search query to find relevant information"},
        },
        "required": ["query"],
        "additionalProperties": False,
    },
}

tools = [
    {"type": "function", "function": record_user_details_json},
    {"type": "function", "function": record_unknown_question_json},
    {"type": "function", "function": search_knowledge_base_json},
]

tool_map = {
    "record_user_details": record_user_details,
    "record_unknown_question": record_unknown_question,
    "search_knowledge_base": search_knowledge_base,
}

def handle_tool_calls(tool_calls):
    results = []
    for tool_call in tool_calls:
        tool_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)
        print(f"Tool called: {tool_name}", flush=True)
        tool = tool_map.get(tool_name)
        result = tool(**arguments) if tool else "Unknown tool: " + tool_name
        results.append(
            {"role": "tool", "content": json.dumps(result), "tool_call_id": tool_call.id}
        )
    return results
