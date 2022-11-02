from typing import Union

from pydantic import BaseModel, validator

from datetime import datetime, date

class UserCreate(BaseModel):
    """Схема запроса для создания экземпляра пользователя согласно задаче №1:"""
    phone: str
    login: str
    password: str
    name: str
    birth: date
    tg: str = None
    email: str = None

    @validator('birth')
    def check_date_of_birth(cls, value):
        """Проверка возраста пользователя"""
        if datetime.now().year - value.year < 18:
            raise ValueError('В сервисе не должны быть зарегистрированы несовершеннолетние.')

class UserID(BaseModel):
    """Схема ответа согласно задаче №1, 2:
    возвращает json с идентификатором пользователя"""
    id: int

    class Config:
        orm_mode = True

class UserResponse(UserID):
    """Схема ответа согласно задаче №3:
    возвращает json со всеми полями пользователя (кроме пароля)"""
    phone: str
    login: str
    name: str
    birth: date
    tg: str
    email: str





