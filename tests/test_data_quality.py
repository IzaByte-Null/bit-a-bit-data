import pandas as pd
from pathlib import Path
import sys


root = Path(__file__).resolve().parent.parent
data_path = root / "data" / "raw" / "ranking_global.csv"

def test_ranking_integrity():
    print(" [TEST] Iniciando Auditoria de Qualidade no Ranking...")
    
    if not data_path.exists():
        print("!! FALHA CRÍTICA !!: Arquivo de dados não encontrado para teste.")
        return

    df = pd.read_csv(data_path)

    #(Data Quality)
    errors = 0

    # Nulos
    if df['username'].isnull().any():
        print("! Erro de Integridade: Encontrados usuários sem nome!")
        errors += 1

    #Score 
    if (df['score_acumulado'] < 0).any():
        print("! Erro de Lógica: Encontrado score negativo no ranking!")
        errors += 1

    if errors == 0:
        print(":) PASSED: Integridade dos dados validada com sucesso.")
    else:
        print(f"X FAILED: O pipeline gerou {errors} inconsistências.")

if __name__ == "__main__":
    test_ranking_integrity()