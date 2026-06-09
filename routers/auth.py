from models.models import Usuario
from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from database.database import get_session
from sqlmodel import Session, select, SQLModel
from typing import Annotated
from pwdlib import PasswordHash
from datetime import datetime, timedelta
import jwt

senha_context = PasswordHash.recommended()
token_schema = OAuth2PasswordBearer(tokenUrl="/login")

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter(prefix="/login", tags=["login"])

SECRET_KEY = "senha"
ALGORITIMO = "HS256"

class Token(SQLModel):
    access_token: str
    token_type: str

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITIMO)

    return token

def get_usuario_logado(session: SessionDep, token: Annotated[str, Depends(token_schema)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Sem Permissão",
        headers={"WWW-Authenticate": 'Bearer'}
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITIMO])
        email = payload.get("sub")

        if not email:
            raise credentials_exception
        
        usuario = session.scalar(select(Usuario).where(Usuario.email == email))

        if not usuario:
            raise credentials_exception
        
        return usuario
    
    except Exception:
        raise credentials_exception

@router.post("/", response_model=Token)
def login(session: SessionDep, form: OAuth2PasswordRequestForm = Depends()):
    usuario = session.scalar(select(Usuario).where(Usuario.email == form.username))

    if not usuario:
        raise HTTPException(status_code=400, detail="Erro")

    if not senha_context.verify(form.password, usuario.senha_hash):
        raise HTTPException(status_code=400, detail="Erro")

    access_token = create_access_token(data = {"sub": usuario.email})

    return {"access_token": access_token, "token_type": "bearer"}