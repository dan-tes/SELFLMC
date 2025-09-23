# 🧪 TesterLMC — Веб-сайт для расширения SyncShare

**TesterLMC** — это веб-приложение, расширяющее функциональность SyncShare. Оно автоматически строит тест на основе задач из pull request'ов, охватывая все вопросы, зарегистрированные на текущий момент в системе тестирования.

## 🚀 Возможности

- Генерация тестов на основе задач из пуллов
- Сбор всех актуальных вопросов для тестирования
- Интеграция с SyncShare

## ⚙️ Требования

- SSL-сертификат для вашего домена
- Установленные [Docker](https://www.docker.com/) и [Docker Compose](https://docs.docker.com/compose/)

## 🛠 Установка и запуск

```bash
git clone https://github.com/dan-tes/TesterLMC/
cd TesterLMC
docker compose up
