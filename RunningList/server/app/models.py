from sqlalchemy import Column, Integer, String, Boolean
from app import db, ma


class Task(db.Model):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    author = Column(String(100), nullable=False)
    read = Column(Boolean, unique=False, default=False)


class TaskSerialization(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'author', 'read')
