## RMS-fastapi
"Система Управления Ресурсами" (тестовое задание для Backend-разработчиков) 

### Описание проекта

API сервиса "Система Управления Ресурсами" с помощью FastAPI. 

### Стек технологий 

В ходе создания проекта применялись различные инстументы и технологии. Они представлены ниже:

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)
![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

## Документация для Эндпоинтов 

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**] | **POST** /v1/auth/register | Добавление нового пользователя
[**auth_user**] | **PATCH** /v1/auth/login |  Аутентификация пользователя перевала
[**read_user**] | **GET** //v1/user/{user_id}/ | Извлечение данных о пользователе

### Инструкция по установке 

1. Клонируете репозиторий

```sh
git clone https://github.com/XanderMoroz/RMS-fastapi.git
```
2. Уставливаете виртуальное окружение (virtual environment)
```sh
pip install virtualenv
```
3. Активируете виртуальное окружение
```sh
./venv/scripts/activate
```
4. Переходите в дерикторию проекта
```sh
cd ./Fan-game_service-board/
```
5. Устанавливаете зависимости
```sh
pip install -r requirements.txt
```
6. Запускаете сервер
```sh
uvicorn sql_app.main:app --reload --port 8080
```
7. Наслаждаетесь результатом)

### Лицензия

Лицензия не требуется. Проект может быль использован без ограничений. 

### Авторы

* [XanderMoroz](https://https://github.com/XanderMoroz/) - *Все работы*
