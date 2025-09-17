from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate, UserUpdate
from passlib.hash import bcrypt

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get(self, user_id: int) -> User:
        return self.db.query(User).filter(User.id == user_id).first()

    def list(self, skip: int = 0, limit: int = 100) -> list[User]:
        return self.db.query(User).offset(skip).limit(limit).all()

    def get_by_username(self, username: str) -> User:
        return self.db.query(User).filter(User.username == username).first()

    def get_by_email(self, email: str) -> User:
        return self.db.query(User).filter(User.email == email).first()

    def create(self, user_in: UserCreate) -> User:
        hashed_pw = bcrypt.hash(user_in.password)
        db_user = User(
            username=user_in.username,
            email=user_in.email,
            password=hashed_pw,
            full_name=user_in.full_name
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def update(self, db_user: User, updates: UserUpdate) -> User:
        data = updates.model_dump(exclude_unset=True)
        if "password" in data:
            data["password"] = bcrypt.hash(data["password"])
        for key, value in data.items():
            setattr(db_user, key, value)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def delete(self, db_user: User) -> None:
        self.db.delete(db_user)
        self.db.commit()
