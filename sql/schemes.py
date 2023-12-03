from pydantic import BaseModel, EmailStr
from typing import List
from datetime import datetime

class AdminBase(BaseModel):

    email: EmailStr
    name: str
    full_name: str
    phone_number: str
    profile_picture: str

class AdminCreate(AdminBase):
    
    password: str


class Admin(AdminBase):
    
    admin_id: int
    
    class Config:
        orm_mode = True

# Clase base
class StudentBase(BaseModel):
    
    email: EmailStr
    name: str
    full_name: str
    phone_number: str
    profile_picture: str
    semester: int

# Clase para crear un estudiante
class StudentCreate(StudentBase):
    
    password: str
    
# Clase para obtener un estudiante
class Student(StudentBase):

    student_id: int
    
    inscriptions: List["Inscription"] = []
    tasks: List["Task"] = []
    
    class Config:
        orm_mode = True

class ProfessorBase(BaseModel):

    email: EmailStr
    name: str
    full_name: str
    phone_number: str
    profile_picture: str


class ProfessorCreate(ProfessorBase):
    
    password: str


class Professor(ProfessorBase):
    
    courses: List["Course"] = []
    
    class Config:
        orm_mode = True


class CourseBase(BaseModel):

    name: str
    full_name: str
    phone_number: str
    description: str
    semester: int
    program: str
    professor_id: int

class CourseCreate(CourseBase):
    
    profile_picture: str
    password: str

class Course(CourseBase):

    course_id: int
    professor: Professor
    
    inscriptions: List["Inscription"] = []
    tasks: List["Task"] = []

    class Config:

        orm_mode = True

class InscriptionBase(BaseModel):
    
    student_id: int
    course_id: int

class InscriptionCreate(InscriptionBase):

    pass

class Inscription(InscriptionBase):

    inscription_id: int
    student: Student
    course: Course

    class Config:

        orm_mode = True


class TaskBase(BaseModel):

    name: str
    description: str
    start_date: datetime
    end_date: datetime
    unique_filename: str
    active: bool

class TaskCreate(TaskBase):
    
    course: Course

class Task(TaskBase):

    task_id: int
    course: Course
    
    notes: List["Note"] = [] 

    class Config:

        orm_mode = True


class NoteBase(BaseModel):

    note: float

class NoteCreate(NoteBase):

    pass


class Note(NoteBase):

    note_id: int
    task: Task
    student: Student

    class Config:
            
        orm_mode = True