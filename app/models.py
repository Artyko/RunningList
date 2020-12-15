from sqlalchemy import Column, Integer, String, Boolean
from app import db, ma


class Task(db.Model):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    author = Column(String(100), nullable=False)
    read = Column(String(100))
    Mo = Column(Boolean, unique=False, default=False)
    Tu = Column(Boolean, unique=False, default=False)
    We = Column(Boolean, unique=False, default=False)
    Th = Column(Boolean, unique=False, default=False)
    Fr = Column(Boolean, unique=False, default=False)
    Sa = Column(Boolean, unique=False, default=False)
    Su = Column(Boolean, unique=False, default=False)


class TaskSerialization(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'author', 'read', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su')


class CompleteDaysSerialization(ma.Schema):
    class Meta:
        fields = ('Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su')
