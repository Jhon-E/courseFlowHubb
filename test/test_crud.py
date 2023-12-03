from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sql import schemes, models
from sql.crud import create_professor, create_student
from auth.hashing import verify_password
from os import getenv
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from app.main import app
import pytest
import sys

load_dotenv()
sys.path.append(getenv("ROUTE_PROJECT"))

DATABASE_URL = getenv("TEST_SQLALCHEMY_DATABASE_URL")
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
models.Base.metadata.create_all(bind=engine)

client = TestClient(app)

@pytest.fixture(scope="function")
def db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_create_student(db: Session):
    # Fake data
    student_data = {
        "email": "test.student2@example.com",
        "name": "Test Student 2",
        "full_name": "Test Full Name 2",
        "phone_number": "1234567890",
        "password": "testpassword2",
        "semester": 3,
        "profile_picture": "test_profile2.jpg",
    }

    created_student = create_student(db, schemes.StudentCreate(**student_data))

    # Verifica que la id no sea nula
    assert created_student.student_id
    # Verifica que esté bien el email del usuario
    assert created_student.email == student_data["email"]
    # Verifica que el nombre del usuario esté bien
    assert created_student.name == student_data["name"]
    # Verifica que la contraseña se ha almacenado correctamente y se puede verificar
    assert verify_password(student_data["password"], created_student.password)
    
def test_create_professor(db: Session):
    professor_data = {
        "email": "test.professor@example.com",
        "name": "Test Professor",
        "full_name": "Test Professor Full Name",
        "phone_number": "987654321",
        "password": "testprofpassword",
        "profile_picture": "test_prof_profile.jpg",
    }

    created_professor = create_professor(db, schemes.ProfessorCreate(**professor_data))

    assert created_professor.professor_id
    assert created_professor.email == professor_data["email"]
    assert created_professor.name == professor_data["name"]
    # Agrega más aserciones según sea necesario

    # Verifica que la contraseña se ha almacenado correctamente y se puede verificar
    assert verify_password(professor_data["password"], created_professor.password)
