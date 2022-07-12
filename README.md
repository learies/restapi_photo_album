# Rest API для Фотоальбома

## Описание
Пользователь может создавать фотоальбомы, добавлять фотографии, присваивать фотографиям теги.

## Технологии
- Django Rest Framework
- Djoser
- SQLite3

## Установка
Создать виртуальное окружение
```bash
python3 -m venv venv
```
Активировать
```bash
source venv/bin/activate
```
Установить зависимости
```bash
pip install -r requirements.txt
```
Применить миграции
```bash
python manage.py migrate
```
Запустить сервер
```
python manage.py runserver
```
