from sqlalchemy.orm import Session

from . import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(phone=user.phone,
                          login=user.login,
                          password=user.password,
                          name=user.name,
                          birth=user.birth,
                          tg=user.tg,
                          email=user.email
                          )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def autenticate_user(db: Session, user_login: str, user_password: str):
    return db.query(models.User).filter(models.User.login == user_login and models.User.password == user_password)

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()
