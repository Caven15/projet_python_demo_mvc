from flask_login import UserMixin
from sqlalchemy import Boolean, ForeignKey, Integer, String, Column
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(UserMixin, Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(200), nullable=False)
    is_active = Column(Boolean, default=True)
    
    tasks = relationship("Task", back_populates="user")

    def get_id(self):
        return str(self.id)

class Task(Base):
    __tablename__ = 'task'
    
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(200), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    
    user = relationship("User", back_populates="tasks")