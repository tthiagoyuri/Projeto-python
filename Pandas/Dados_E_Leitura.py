import pandas as pd

class Dados_Leitura:
    def __init__(self, file_path):
        self.file_path = file_path
        self.contagem_bichos = None
        self.media_aparicoes = None
        self._processar_dados()

    def _processar_dados(self):
        try:
            tabela = pd.read_excel(self.file_path)
        except FileNotFoundError:
            print(f"Arquivo '{self.file_path}' não encontrado. Verifique o caminho e tente novamente.")
            exit()
        except Exception as e:
            print(f"Ocorreu um erro ao ler o arquivo '{self.file_path}': {str(e)}")
            exit()
        
        self.contagem_bichos = tabela['Bicho'].value_counts()
        self.media_aparicoes = self.contagem_bichos.mean()
