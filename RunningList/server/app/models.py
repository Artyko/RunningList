from sqlalchemy import Column, Integer, String, Boolean
from app import db, ma


class Task(db.Model):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    author = Column(String(100), nullable=False)
    read = Column(String(100))
    Mo = Column(Boolean, unique=False)
    Tu = Column(Boolean, unique=False)
    We = Column(Boolean, unique=False)
    Th = Column(Boolean, unique=False)
    Fr = Column(Boolean, unique=False)
    Sa = Column(Boolean, unique=False)
    Su = Column(Boolean, unique=False)


class TaskSerialization(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'author', 'read', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su')
