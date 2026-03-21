from pipeline import extrair_dados
from utils import get_project_root
import pandas as pd

def mostrar_dashboard():
    
    extrair_dados()
    
    root = get_project_root()
    ranking_path = root / "data" / "raw" / "ranking_global.csv"
    
    print("\n" + "="*30)
    print("BIT-A-BIT: DASHBOARD DE DADOS")
    print("="*30)


    if ranking_path.exists():
        df = pd.read_csv(ranking_path)
        print("\n🏆 TOP 5 RANKING GLOBAL:")
        print(df.head(5)[['username', 'score_acumulado', 'partidas_jogadas']])
    else:
        print(":0 !ALERTA!: Base de dados não encontrada. Verifique a conexão com o Banco de Dados.")

if __name__ == "__main__":
    mostrar_dashboard()