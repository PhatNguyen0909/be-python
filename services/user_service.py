from sqlalchemy.orm import Session
from repositories.user_repository import UserRepository
from schemas.user import UserCreate, UserUpdate
from models.user import User

class UserService:
    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def get_user(self, user_id: int) -> User:
        user = self.repo.get(user_id)
        if not user:
            raise ValueError("User not found")
        return user

    def list_users(self, skip: int = 0, limit: int = 100):
        return self.repo.list(skip=skip, limit=limit)

    def create_user(self, data: UserCreate) -> User:
        if self.repo.get_by_username(data.username):
            raise ValueError("Username already exists")
        if self.repo.get_by_email(data.email):
            raise ValueError("Email already exists")
        return self.repo.create(data)

    def update_user(self, user_id: int, data: UserUpdate) -> User:
        user = self.repo.get(user_id)
        if not user:
            raise ValueError("User not found")
        return self.repo.update(user, data)

    def delete_user(self, user_id: int):
        user = self.repo.get(user_id)
        if not user:
            raise ValueError("User not found")
        self.repo.delete(user)
        return {"detail": "User deleted"}
