import pandas as pd
from sqlalchemy import text
import sys
from pathlib import Path


sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.utils import get_engine, get_project_root

def descobrir_tabelas():
    engine = get_engine()
    root = get_project_root()
    
    # Query 
    query = """
    SELECT table_schema, table_name 
    FROM information_schema.tables 
    WHERE table_schema IN ('public', 'sensitive', 'neon_auth')
    ORDER BY table_schema, table_name;
    """

    try:
        with engine.connect() as connection:
            df_tabelas = pd.read_sql(text(query), connection)
            
            if df_tabelas.empty:
                print("⚠️ Conectado, mas nenhum objeto foi encontrado nos schemas selecionados.")
            else:
                print(f"🆙 Tabelas detectadas:\n{df_tabelas}")
                
                
                output_path = root / "data" / "raw" / "lista_tabelas.csv"
                output_path.parent.mkdir(parents=True, exist_ok=True)
                
                df_tabelas.to_csv(output_path, index=False)
                print(f"\n 📦 Inventário salvo em: {output_path}")

    except Exception as e:
        print(f"❌ Falha na Descoberta de Schema: {e}")

if __name__ == "__main__":
    descobrir_tabelas()