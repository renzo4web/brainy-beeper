from sqlalchemy import String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import List

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    tg_id: Mapped[str] = mapped_column(String(100), unique=True)
    todos: Mapped[List["Todo"]] = relationship("Todo", back_populates="user")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, tg_id={self.tg_id!r})"

class Todo(Base):
    __tablename__ = "todos"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(200))
    content: Mapped[str] = mapped_column(String(1000))
    is_completed: Mapped[bool] = mapped_column(Boolean, default=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship("User", back_populates="todos")

    def __repr__(self) -> str:
        return f"Todo(id={self.id!r}, title={self.title!r}, is_completed={self.is_completed!r})"
