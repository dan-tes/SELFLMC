# 🧪 TesterLMC — Website Extension for SyncShare
# Платформа для обучения с автопроверкой программирования на питоне
## 🚀 Запуск проекта на FastAPI

## 📋 Описание проекта
Проект создан на базе **FastAPI** с использованием **Uvicorn** для запуска веб-сервера. В данном руководстве описаны шаги по установке зависимостей и запуску проекта.

---

## 📂 Структура проекта
```
📂 .venv/                # Виртуальное окружение
📂 DataBaseManager/      # Управление базой данных
├── __init__.py
└── models.py           # Описание моделей БД 
📂 utils/                # Утилиты
└── logger.py           # Логирование
📂 routers/ # Общие роутеры для потоков запросов с общей приставкой
📄 .gitignore     # Игнорируемые файлы
📄 main.py               # Основной файл приложения
📄 models.py             # Модели для API
📄 requirements.txt      # Файл зависимостей
📄 .env Переменные окружения
```

**TesterLMC** is a web application that extends the functionality of SyncShare. It automatically builds a test from pull request tasks, including all questions currently registered in the testing system.

## 🚀 Features

- Automatically generates tests based on pull request tasks
- Collects all currently registered questions for testing
- Seamless integration with SyncShare

## ⚙️ Requirements

- A valid **SSL certificate** for your domain
- Installed [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/)

## 🛠 Installation and Usage

```bash
git clone https://github.com/dan-tes/TesterLMC/
cd TesterLMC
docker compose up
```