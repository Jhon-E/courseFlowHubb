from fastapi import APIRouter, Depends, HTTPException, status, Request, UploadFile, File
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sql.database import SessionLocal
from sql import models, schemes, crud
from datetime import datetime

router = APIRouter(
    prefix="/create",
    tags=["Create"],
    responses={404: {"description": "Not found"}},
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post("/user", status_code=status.HTTP_201_CREATED)
async def create_user(
    request: Request, 
    profile_picture: UploadFile = File(...),
    db: Session = Depends(get_db) 
):

    """"
    Crear un estudiante

    Args:
        Request: Datos del formulario
        profile_picture: Imagen de perfil
        db: Base de datos

    Returns:
        Estudiante creado
    """
    
    form_data = await request.form()
    
    student = crud.get_student_by_email(db=db, student_email=form_data.get("email"))
    professor = crud.get_professor_by_email(db=db, professor_email=form_data.get("email"))
    
    if student or professor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Email already registered")
    
    email = form_data.get("email")
    
    if not email.endswith("@coursefh.com"):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid email.")
    
    # Obtener la extensión del archivo
    file_extension = profile_picture.filename.split(".")[-1]

    # Crear un nombre de archivo único para evitar colisiones
    unique_filename = f"{email}_{datetime.utcnow().timestamp()}.{file_extension}"

    # Ruta completa al archivo de destino
    destination_path = f"./uploads/imgs/{unique_filename}"

    # Guardar el archivo en la carpeta de uploads
    with open(destination_path, "wb") as file:
        file.write(profile_picture.file.read())
    
    data = {
        "email": email,
        "name": form_data.get("name"),
        "full_name": form_data.get("full_name"),
        "phone_number": form_data.get("phone_number"),
        "profile_picture": unique_filename,
        "password": form_data.get("password")
    }
    
    role = form_data.get("role")
    
    if role == "student":
        
        db_student = schemes.StudentCreate(**data)
        
        return create_student(db=db, student_data=db_student)
        
    else:
        
        db_professor = schemes.ProfessorCreate(**data) 
        
        return create_professor(professor=db_professor, db=db)
    
@router.post("/student", response_model=schemes.StudentCreate)
def create_student(student: schemes.StudentCreate , db: Session = Depends(get_db)):
    return crud.create_student(db=db, student=student)

@router.post("/professor", response_model=schemes.ProfessorCreate)
def create_professor(professor: schemes.ProfessorCreate , db: Session = Depends(get_db)):
    return crud.create_professor(db=db, professor=professor)