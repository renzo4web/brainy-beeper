from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import User, Todo
from typing import Optional
from config import TURSO_DATABASE_URL, TURSO_AUTH_TOKEN

class DatabaseService:
    _instance = None
    _engine = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseService, cls).__new__(cls)
            if not TURSO_DATABASE_URL or not TURSO_AUTH_TOKEN:
                raise ValueError("Please set TURSO_DATABASE_URL and TURSO_AUTH_TOKEN in .env file")
            
            db_url = f"sqlite+{TURSO_DATABASE_URL}/?authToken={TURSO_AUTH_TOKEN}&secure=true"
            cls._engine = create_engine(db_url, connect_args={'check_same_thread': False})
        return cls._instance

    @classmethod
    def get_instance(cls) -> 'DatabaseService':
        if cls._instance is None:
            cls._instance = DatabaseService()
        return cls._instance
    
    def get_session(self) -> Session:
        return Session(self._engine)

    def create_user(self, tg_id: str) -> User:
        with self.get_session() as session:
            user = User(tg_id=tg_id)
            session.add(user)
            session.commit()
            return user
            
    def create_todo(self, title: str, content: str, user_id: int) -> Todo:
        with self.get_session() as session:
            todo = Todo(title=title, content=content, user_id=user_id)
            session.add(todo)
            session.commit()
            return todo
    
    def update_todo(
        self, 
        todo_id: int, 
        title: Optional[str] = None, 
        content: Optional[str] = None, 
        is_completed: Optional[bool] = None
    ) -> Optional[Todo]:
        with self.get_session() as session:
            todo = session.query(Todo).filter(Todo.id == todo_id).first()
            if not todo:
                return None
                
            if title is not None:
                todo.title = title
            if content is not None:
                todo.content = content
            if is_completed is not None:
                todo.is_completed = is_completed
                
            session.commit()
            return todo
            
    def get_user_todos(self, tg_id: int) -> list[Todo]:
        with self.get_session() as session:
            user = session.query(User).filter(User.tg_id == tg_id).first()
            return user.todos if user else []
    
    def get_user(self, tg_id: int) -> Optional[User]:
        with self.get_session() as session:
            user = session.query(User).filter(User.tg_id == tg_id).first()
            return user
