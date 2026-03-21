import os
from pathlib import Path
from sqlalchemy import create_engine
from dotenv import load_dotenv

#localizar
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

def get_engine():
    """Cria e retorna o engine de conexão com o banco Neon."""
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT', '5432')
    db = os.getenv('DB_NAME')

    if not all([user, password, host, db]):
        raise ValueError("ERRO: Variáveis de ambiente de banco de dados não encontradas.")

    #segurança em cloud
    DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{db}?sslmode=require"
    
    return create_engine(DATABASE_URL)

def get_project_root() -> Path:
    """Retorna o caminho absoluto para a raiz do projeto."""
    return BASE_DIR