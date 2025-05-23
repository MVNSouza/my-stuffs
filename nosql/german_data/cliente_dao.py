import pandas as pd
from modelo import Cliente

class ClienteDAO():
    def __init__(self, csv_path: str):
        self.csv_path = csv_path
        self.columns = ['id', 'idade', 'sexo', 'credito', 'moradia', 'conta_poupanca', 'conta_corrente', 'valor_conjunto', 'duracao', 'proposito', 'aprovacao']
        self._encontrar_arquivo()

def _encontrar_arquivo(self):
    try:
        pd.read_csv(self.csv_path)
    except:
        df = pd.DataFrame(columns=self.columns)
        df.to_csv(self.csv_path, index=False)