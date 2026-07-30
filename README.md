# Mini Social Network

Backend для мини социальной сети, разработанный на Python с
использованием FastAPI, PostgreSQL и SQLAlchemy.

Проект создаётся с целью изучения построения полноценного
backend-приложения с разделением ответственности между слоями, работой с
базой данных, миграциями и асинхронным API.

> 🚧 Проект находится в активной разработке.

## 🚀 Технологии

-   Python 3.12+
-   FastAPI
-   SQLAlchemy 2.0 (Async ORM)
-   PostgreSQL 16
-   Alembic
-   Pydantic
-   Docker / Docker Compose
-   asyncpg
-   Uvicorn

## 📌 Реализовано

### Posts

-   ✅ Создание постов
-   ✅ Валидация входных данных через Pydantic
-   ✅ Сохранение данных в PostgreSQL
-   ✅ Асинхронная работа с базой данных
-   ✅ Миграции базы данных через Alembic

## 🏗 Архитектура проекта

    app/
    │
    ├── api/              # HTTP слой (FastAPI routers)
    ├── services/         # Бизнес-логика
    ├── repositories/     # Работа с базой данных
    ├── models/           # SQLAlchemy модели
    ├── schemas/          # Pydantic схемы
    ├── database/         # Подключение к БД
    └── core/             # Конфигурация и зависимости

## 🔄 Поток запроса

    Client
      |
      ↓
    FastAPI Router
      |
      ↓
    Pydantic Schema
      |
      ↓
    Service
      |
      ↓
    Repository
      |
      ↓
    SQLAlchemy
      |
      ↓
    PostgreSQL

## 🐳 Запуск PostgreSQL через Docker

``` bash
docker compose up -d
```

Проверить контейнер:

``` bash
docker ps
```

## ⚙️ Настройка окружения

Создать файл `.env`:

``` env
POSTGRES_USERNAME=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=mini_social
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/mini_social
```

## 📦 Установка зависимостей

Установить зависимости:

``` bash
pip install -r requirements.txt
```

## 🗄 Миграции базы данных

Создать новую миграцию:

``` bash
alembic revision --autogenerate -m "migration name"
```

Применить миграции:

``` bash
alembic upgrade head
```

## ▶️ Запуск приложения

``` bash
uvicorn app.main:app --reload
```

API:

    http://localhost:8000

Swagger:

    http://localhost:8000/docs

## 📡 API

### Создание поста

`POST /posts/`

Request:

``` json
{
    "text": "Hello world"
}
```

Response:

``` json
{
    "id": 1,
    "text": "Hello world",
    "created_at": "2026-07-25T16:00:00"
}
```

### Получение постов

`GET /posts/`

Response:

``` json
[
    {
        "id": 1,
        "text": "Hello world",
        "created_at": "2026-07-25T16:00:00"
    }
]
```

## 🛠 План развития

### Пользователи

-   [ ] Регистрация пользователей
-   [ ] Авторизация через JWT
-   [ ] Профиль пользователя
-   [ ] Связь User → Posts

### Социальные функции

-   [ ] Лайки
-   [ ] Комментарии
-   [ ] Подписки
-   [ ] Лента новостей

### Улучшение backend

-   [ ] Redis кеширование
-   [ ] Pagination
-   [ ] Rate limiting
-   [ ] Background tasks
-   [ ] Docker контейнер для приложения
-   [ ] CI/CD

## 🎯 Цель проекта

Получить практический опыт разработки backend-приложений:

-   проектирование API
-   работа с PostgreSQL
-   использование ORM
-   миграции базы данных
-   построение масштабируемой архитектуры
-   асинхронное программирование в Python
