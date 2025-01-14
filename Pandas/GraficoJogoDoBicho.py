import pandas as pd
import matplotlib.pyplot as plt
from Pandas.Dados_E_Leitura import Dados_Leitura  

class GraficoJogoDoBicho:
    def __init__(self, dados_jogo_do_bicho):
        self.dados = dados_jogo_do_bicho
        self.plot_grafico()

    def plot_grafico(self):
        import numpy as np
        np.random.seed(42)
        animais_aleatorios = self.dados.contagem_bichos.sample(frac=1)

        plt.figure(figsize=(12, 6))
        bars = plt.bar(animais_aleatorios.index, animais_aleatorios.values, color='skyblue')

        maiores_medias = self.dados.contagem_bichos[self.dados.contagem_bichos >= self.dados.media_aparicoes]
        for bar in bars:
            if bar.get_height() in maiores_medias.values:
                bar.set_color('red')

        plt.xlabel(f'Média: {self.dados.media_aparicoes:.2f}', ha='center', fontsize=20, color='green')
        plt.ylabel('Número de Aparições')
        plt.title('Número de Aparições por Animal')
        plt.xticks(rotation=45)

        for idx, value in enumerate(animais_aleatorios.values):
            plt.text(idx, value + 0.5, f'{value}', ha='center', va='bottom', fontsize=8)

        plt.axhline(y=self.dados.media_aparicoes, color='green', linestyle='--', linewidth=1.0)

        plt.tight_layout()
        plt.show()

if __name__ == '__main__':
    file_path = r'C:\Users\Caio Manoel\Desktop\Facul\Pandas\JogoDoBicho.xlsx'

    dados = Dados_Leitura(file_path)  # Criando o objeto dados utilizando Dados_Leitura
    GraficoJogoDoBicho(dados)  # Passando o objeto dados para a classe GraficoJogoDoBicho
