# 🚀 NeoClippy: AI-powered Document Assistant

NeoClippy is an AI-powered document assistant that helps analyze and improve text documents. It supports **local LLM inference** and **API-based AI processing**. The project aims to create a modern, intelligent Clippy for document automation.

## 🌟 Features
- 📄 **Reads various file formats**: PDF, DOCX, TXT, Markdown
- 🤖 **Uses LLM (Mistral, LLaMA, GPT-4, or local AI)** to process text
- 📊 **Graph-based text analysis** for better insights
- ⚡ **Runs locally or via cloud API**
- 🔌 **Easy integration with Office tools, Notion, and VS Code**

## 🔧 Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/NeoClippy.git
cd NeoClippy

# Install dependencies
pip install -r requirements.txt

# Run the app
python neo_clippy.py --port 5000
```

## 🛠️ Usage
Send a request to analyze a document:
```bash
curl -X POST "http://localhost:5000/analyze" -H "Content-Type: application/json" -d '{"file_path": "example.pdf"}'
```

## 📈 Future Plans
- Add GUI (PyQt/Electron-based)
- Expand AI model support (LLaMA/Mistral + fine-tuning)
- Improve NLP and text summarization

---

# 🇷🇺 NeoClippy: AI-помощник для документов

**NeoClippy** — это интеллектуальный ассистент, который помогает анализировать и улучшать текстовые документы. Он поддерживает **локальную работу AI** и **подключение через API**.

## 🌟 Возможности
- 📄 **Читает файлы**: PDF, DOCX, TXT, Markdown
- 🤖 **Использует AI (Mistral, LLaMA, GPT-4, OpenAI API)** для обработки текста
- 📊 **Создаёт граф смыслов** для анализа структуры текста
- ⚡ **Работает локально или через облако**
- 🔌 **Лёгкая интеграция с Office, Notion, VS Code**

## 🔧 Установка
```bash
# Клонировать репозиторий
git clone https://github.com/yourusername/NeoClippy.git
cd NeoClippy

# Установить зависимости
pip install -r requirements.txt

# Запустить приложение
python neo_clippy.py --port 5000
```

## 🛠️ Использование
Отправьте запрос на анализ документа:
```bash
curl -X POST "http://localhost:5000/analyze" -H "Content-Type: application/json" -d '{"file_path": "example.pdf"}'
```

## 📈 Планы на будущее
- Добавить GUI (PyQt/Electron)
- Расширить поддержку моделей AI (LLaMA/Mistral + обучение)
- Улучшить NLP и анализ текста

