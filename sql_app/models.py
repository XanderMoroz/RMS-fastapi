from sqlalchemy import Column, Integer, String, Date

from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    phone = Column(String, comment='Номер телефона пользователя')
    login = Column(String(128), comment='Логин')
    password = Column(String(128), comment='Пароль')
    name = Column(String(128), comment='Имя пользователя')
    birth = Column(Date, comment='Дата рождения пользователя')
    tg = Column(String(128), nullable=True, comment='Телеграмм пользователя')  # необязательное поле
    email = Column(String(128), nullable=True, comment='Email пользователя')  # необязательное поле
