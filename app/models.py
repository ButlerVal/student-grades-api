from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    score = Column(Float)
    grade = Column(String)
