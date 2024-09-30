# AniFigureShop

AniFigureShop - это веб-приложение для покупки фигурок, построенное на основе Django и React.

## Содержание

1. [Требования](#требования)
2. [Установка](#установка)
    - [Клонирование репозитория](#клонирование-репозитория)
    - [Настройка виртуального окружения](#настройка-виртуального-окружения)
    - [Установка зависимостей](#установка-зависимостей)
    - [Настройка окружения](#настройка-окружения) (В разработке)
3. [Применение миграций](#применение-миграций)
4. [Создание суперпользователя](#создание-суперпользователя)
5. [Запуск приложения](#запуск-приложения)
6. [Запуск фронтенда на React](#запуск-фронтенда-на-react)
7. [Документирование (SwaggerUI, Redoc)](#документирование)
8. [Дополнительные команды](#дополнительные-команды)
9. [Тестирование](#тестирование)  (В разработке)

## Требования

- Python 3.11+
- Node.js 16+
- Git

## Установка

### Клонирование репозитория

Клонируйте репозиторий на свой локальный компьютер:

```bash
git clone https://github.com/Munchen777/AniFigureShop.git
cd AniFigureShop
```

### Настройка виртуального окружения

Создайте и активируйте виртуальное окружение:

На Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

На macOs и Linux:

```bash
python -m venv venv
source venv/bin/activate
```

### Установка зависимостей

Установите зависимости проекта из файла requirements.txt:

```bash
pip install -r requirements.txt
```

## Применение миграций

Примените миграции для настройки базы данных:

```bash
python manage.py migrate
```

## Создание суперпользователя

Создайте суперпользователя для доступа к административной панели:

```bash
python manage.py createsuperuser
```

Следуйте инструкциям в терминале для создания суперпользователя.

## Запуск приложения

Запустите сервер разработки Django

```bash
python manage.py runserver
```

Приложение будет доступно по адресу http://127.0.0.1:8000/

## Запуск фронтенда на React

Перейдите в директорию с фронтендом и установите зависимости:

```bash
cd frontend
npm install
```

Запустите фронтенд:

```bash
npm start
```

Фронтенд будет доступен по адресу http://localhost:3000/

## Документирование (SwaggerUI, Redoc)

Перейдите по адресу:

http://127.0.0.1:8000/api/schema/swagger-ui/

http://127.0.0.1:8000/api/schema/redoc/

Здесь будут представлены эндпоинты, включающие параметры запроса и ответа.

## Дополнительные команды

### Создание новых миграций

```bash
python manage.py makemigrations
```

### Применение миграций

```bash
python manage.py migrate
```

### Запуск Django Shell

```bash
python manage.py shell
```

### Сборка статических файлов

```bash
python manage.py collectstatic
```