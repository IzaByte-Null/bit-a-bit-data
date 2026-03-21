import sys
from pathlib import Path
from sqlalchemy import text

# Adiciona a raiz ao path para encontrar o src.utils
sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.utils import get_engine

def testar_conexao():
    print("🌐 Tentando conectar ao servidor do Neon...")
    try:
        engine = get_engine()
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
            print("🆙 SUCESSO: O tunneling está aberto e respondendo!")
    except Exception as e:
        print(f"🚫 ERRO \nDetalhe: {e}")

if __name__ == "__main__":
    testar_conexao()

