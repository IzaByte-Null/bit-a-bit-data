import pandas as pd
from utils import get_engine, get_project_root

def extrair_dados():
    engine = get_engine()
    root = get_project_root()
    output_dir = root / "data" / "raw"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    fluxos = {
        "ranking_global": "SELECT * FROM v_ranking_global",
        "observabilidade_bot": "SELECT * FROM v_observabilidade_bitbot",
        "logs_erro": "SELECT * FROM log_erros_api"
    }
    
    print("[ETL] Iniciando extração do Neon...")
    for arquivo, query in fluxos.items():
        try:
            
            df = pd.read_sql(query, engine)
            full_path = output_dir / f"{arquivo}.csv"
            df.to_csv(full_path, index=False)
            print(f":) SUCESSO!: {arquivo}.csv salvo em {full_path}")
        except Exception as e:
            print(f":( X ERRO na extração de {arquivo}: {e}")

if __name__ == "__main__":
    extrair_dados()