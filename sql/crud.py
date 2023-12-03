from sqlalchemy.orm import Session
from . import models, schemes
from auth.hashing import hash_password, verify_password

def create_student(db: Session, student: schemes.StudentCreate):
    
    """
    Crea un nuevo estudiante en la base de datos.

    Args:
        db (Session): Objeto de sesión de SQLAlchemy.
        student (schemes.StudentCreate): Datos del estudiante a crear.

    Returns:
        models.Student: Objeto del estudiante recién creado.
    """
    
    password = hash_password(student.password)
    
    db_student = models.Student(
        email=student.email,
        name=student.name,
        full_name=student.full_name,
        phone_number=student.phone_number,
        password=password,
        semester=student.semester,
        profile_picture=student.profile_picture
    )
    
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    
    return db_student

def create_professor(db: Session, professor: schemes.ProfessorCreate):

    """
    Crea un nuevo profesor en la base de datos.

    Args:
        db (Session): Objeto de sesión de SQLAlchemy.
        professor (schemes.ProfessorCreate): Datos del profesor a crear.

    Returns:
        models.Professor: Objeto del profesor recién creado.
    """

    password = hash_password(professor.password)

    db_professor = models.Professor(
        email=professor.email,
        name=professor.name,
        full_name=professor.full_name,
        phone_number=professor.phone_number,
        password=password,
        profile_picture=professor.profile_picture,
    )

    db.add(db_professor)
    db.commit()
    db.refresh(db_professor)
        
    return db_professor

def get_student_by_email(db: Session, student_email: str):

    """
    Obtiene un estudiante de la base de datos a partir de su correo electrónico.

    Args:
        db (Session): Objeto de sesión de SQLAlchemy.
        student_email (str): Correo electrónico del estudiante a buscar.
    
    Returns:
        models.Student: Objeto del estudiante encontrado.
    """
    
    return db.query(models.Student).filter(models.Student.email == student_email).first()

def get_student_by_id(db: Session, student_id: int):

    """"
    Obtiene un estudiante de la base de datos a partir de su id.

    Args:
        db (Session): Objeto de sesión de SQLAlchemy.
        student_id (int): Id del estudiante a buscar.

    Returns:
        models.Student: Objeto del estudiante encontrado.
    """

    return db.query(models.Student).filter(models.Student.student_id == student_id).first()

def get_professor_by_email(db: Session, professor_email: str):
    
    """
    Obtiene un profesor de la base de datos a partir de su correo electrónico.

    Args:
        db (Session): Objeto de sesión de SQLAlchemy.
        student_email (str): Correo electrónico del profesor a buscar.
    
    Returns:
        models.Profesor: Objeto del profesor encontrado.
    """

    return db.query(models.Professor).filter(models.Professor.email == professor_email).first()

def get_professor_by_id(db: Session, professor_id: int):

    """"
    Obtiene un profesor de la base de datos a partir de su id.

    Args:
        db (Session): Objeto de sesión de SQLAlchemy.
        professor_id (int): Id del profesor a buscar.

    Returns:
        models.Professor: Objeto del profesor encontrado.
    """

    return db.query(models.Professor).filter(models.Professor.professor_id == professor_id).first()

def update_student(db: Session, student_id: int, updated_data: schemes.StudentCreate):
    """
    Actualiza un estudiante en la base de datos.

    Args:
        db (Session): Objeto de sesión de SQLAlchemy.
        student_id (int): Id del estudiante a actualizar.
        updated_data (schemes.StudentUpdate): Datos actualizados del estudiante.

    Returns:
        models.Student: Objeto del estudiante actualizado.
    """
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()

    if db_student:
        for key, value in updated_data.dict(exclude_unset=True).items():
            setattr(db_student, key, value)

        db.commit()
        db.refresh(db_student)

    return db_student

def update_professor(db: Session, professor_id: int, updated_data: schemes.ProfessorCreate):
    """
    Actualiza un profesor en la base de datos.

    Args:
        db (Session): Objeto de sesión de SQLAlchemy.
        professor_id (int): Id del profesor a actualizar.
        updated_data (schemes.ProfessorUpdate): Datos actualizados del profesor.

    Returns:
        models.Professor: Objeto del profesor actualizado.
    """
    db_professor = db.query(models.Professor).filter(models.Professor.id == professor_id).first()

    if db_professor:
        for key, value in updated_data.dict(exclude_unset=True).items():
            setattr(db_professor, key, value)

        db.commit()
        db.refresh(db_professor)

    return db_professor
