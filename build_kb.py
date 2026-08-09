import os
import json
import glob
from openai import OpenAI
from pypdf import PdfReader
import docx
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)

# Initialize OpenRouter client
client = OpenAI(
    api_key=os.environ.get("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)
MODEL_NAME = "nvidia/llama-nemotron-embed-vl-1b-v2:free"

KB_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(KB_DIR, "data")

def get_embedding(text):
    response = client.embeddings.create(
        input=text,
        model=MODEL_NAME,
        encoding_format="float"
    )
    return response.data[0].embedding

def extract_text_from_pdf(filepath):
    text = ""
    try:
        reader = PdfReader(filepath)
        for page in reader.pages:
            t = page.extract_text()
            if t:
                text += t + "\n"
    except Exception as e:
        print(f"Error reading PDF {filepath}: {e}")
    return text.strip()

def extract_text_from_docx(filepath):
    text = ""
    try:
        doc = docx.Document(filepath)
        for para in doc.paragraphs:
            text += para.text + "\n"
    except Exception as e:
        print(f"Error reading DOCX {filepath}: {e}")
    return text.strip()

def build():
    kb = []
    print("Building Knowledge Base from data/ directory...")
    
    # Process all markdown and text files
    for ext in ["*.md", "*.txt"]:
        for filepath in glob.glob(os.path.join(DATA_DIR, ext)):
            filename = os.path.basename(filepath)
                
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read().strip()
                
            if content:
                print(f"Embedding {filename}...")
                embedding = get_embedding(content)
                kb.append({
                    "filename": filename,
                    "content": content,
                    "embedding": embedding
                })
                
    # Process PDF
    pdf_path = os.path.join(DATA_DIR, "linkedin.pdf")
    if os.path.exists(pdf_path):
        content = extract_text_from_pdf(pdf_path)
        if content:
            print("Embedding linkedin.pdf...")
            embedding = get_embedding(content)
            kb.append({"filename": "linkedin.pdf", "content": content, "embedding": embedding})
            
    # Process DOCX
    docx_path = os.path.join(DATA_DIR, "Rashid_Husain_10.docx")
    if os.path.exists(docx_path):
        content = extract_text_from_docx(docx_path)
        if content:
            print("Embedding Rashid_Husain_10.docx...")
            embedding = get_embedding(content)
            kb.append({"filename": "Rashid_Husain_10.docx", "content": content, "embedding": embedding})

    # Save to kb.json in the main directory
    with open(os.path.join(KB_DIR, "kb.json"), "w", encoding="utf-8") as f:
        json.dump(kb, f)
    print(f"Successfully embedded {len(kb)} documents into kb.json.")

if __name__ == "__main__":
    build()
