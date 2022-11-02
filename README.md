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
[**submit_data_create**](docs/SubmitDataApi.md#submit_data_create) | **POST** /submitData | Добавление перевала
[**submit_data_partial_update**](docs/SubmitDataApi.md#submit_data_partial_update) | **PATCH** /submitData/{id}/ |  Редактирование перевала
[**submit_data_retrieve**](docs/SubmitDataApi.md#submit_data_retrieve) | **GET** /submitData/{id}/ | Извлечение данных о перевале
[**submit_data_user_email_list**](docs/SubmitDataApi.md#submit_data_user_email_list) | **GET** /submitData/user__email&#x3D;{email} | Извлечение списка перевалов пользователя

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
python manage.py runserver
```
7. Наслаждаетесь результатом)

### Лицензия

Лицензия не требуется. Проект может быль использован без ограничений. 

### Авторы

* [XanderMoroz](https://https://github.com/XanderMoroz/) - *Все работы*
