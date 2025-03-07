import os
import sys
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import pdfplumber
import docx
import markdown
import networkx as nx
import matplotlib.pyplot as plt
from flask import Flask, request, jsonify
import argparse

# Проверяем наличие GPU
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Загружаем модель LLM (можно заменить на локальную LLaMA/Mistral)
MODEL_NAME = "mistralai/Mistral-7B-v0.1"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME).to(DEVICE)

app = Flask(__name__)

# Чтение текста из файлов
def read_text(file_path):
    ext = os.path.splitext(file_path)[-1].lower()
    if ext == ".pdf":
        with pdfplumber.open(file_path) as pdf:
            return " ".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    elif ext == ".docx":
        doc = docx.Document(file_path)
        return " ".join([p.text for p in doc.paragraphs])
    elif ext == ".md":
        with open(file_path, "r", encoding="utf-8") as f:
            return markdown.markdown(f.read())
    else:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

# Простая LLM-обработка текста
def generate_response(prompt):
    inputs = tokenizer(prompt, return_tensors="pt").to(DEVICE)
    output = model.generate(**inputs, max_length=200)
    return tokenizer.decode(output[0], skip_special_tokens=True)

# Создание графа смыслов текста
def create_text_graph(text):
    words = text.split()
    G = nx.Graph()
    for i in range(len(words) - 1):
        G.add_edge(words[i], words[i+1])
    return G

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    file_path = data.get("file_path")
    if not file_path:
        return jsonify({"error": "No file path provided"})
    
    text = read_text(file_path)
    graph = create_text_graph(text)
    response = generate_response(text[:500])
    
    plt.figure(figsize=(10, 6))
    nx.draw(graph, with_labels=True, font_size=8)
    plt.savefig("text_graph.png")
    
    return jsonify({"text": text[:1000], "response": response, "graph": "text_graph.png"})

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="NeoClippy: AI-powered document assistant")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Host for the Flask app")
    parser.add_argument("--port", type=int, default=5000, help="Port for the Flask app")
    parser.add_argument("--debug", action="store_true", help="Run in debug mode")
    args = parser.parse_args()
    
    app.run(host=args.host, port=args.port, debug=args.debug)
