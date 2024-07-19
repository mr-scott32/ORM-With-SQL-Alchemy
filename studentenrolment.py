from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    
    student_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    surname = Column(String)
    grade = Column(Integer)
    
    # Relationship with Enrolment
    enrolments = relationship('Enrolment', back_populates='student')

class Subject(Base):
    __tablename__ = 'subject'
    
    subject_id = Column(String, primary_key=True)
    subject_name = Column(String)
    
    # Relationship with Enrolment
    enrolments = relationship('Enrolment', back_populates='subject')

class Enrolment(Base):
    __tablename__ = 'enrolment'
    
    student_id = Column(Integer, ForeignKey('student.student_id'), primary_key=True)
    subject_id = Column(String, ForeignKey('subject.subject_id'), primary_key=True)
    
    # Relationships
    student = relationship('Student', back_populates='enrolments')
    subject = relationship('Subject', back_populates='enrolments')

# Create an engine and a session
engine = create_engine('sqlite:///school.db')  # Example using SQLite
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Example usage
# Add a student
new_student = Student(student_id=1, first_name='Bart', surname='Simpson', grade=12)
session.add(new_student)
session.commit()

# Add a subject
new_subject = Subject(subject_id='12SE6', subject_name='12 Software Engineering 6')
session.add(new_subject)
session.commit()

# Enrol a student in a subject
enrolment = Enrolment(student_id=1, subject_id='12SE6')
session.add(enrolment)
session.commit()