import matplotlib
matplotlib.use('Agg')  # Use o backend 'Agg' para evitar problemas com o Tkinter
import matplotlib.pyplot as plt
import pandas as pd
import os

def plot_data(df, output_path):
    # Verifica se o diretório "static" existe, se não existir, cria-o
    directory = os.path.dirname(output_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    if 'Name' in df.columns:
        df['Count'] = 1  # Adiciona uma coluna de contagem
        df.groupby('Name')['Count'].count().plot(kind='bar')  # Agrupa por Name e conta
        plt.title('Sales Stores')
        plt.xlabel('Store Name')
        plt.ylabel('Count')
    else:
        print("A coluna 'Name' não existe na tabela selecionada.")
        if pd.api.types.is_numeric_dtype(df.iloc[:, 0]) and pd.api.types.is_numeric_dtype(df.iloc[:, 1]):
            df.plot(kind='bar', x=df.columns[0], y=df.columns[1])
            plt.title('Dados da Tabela')
            plt.xlabel(df.columns[0])
            plt.ylabel(df.columns[1])
        else:
            plt.figure(figsize=(10, 5))
            plt.text(0.5, 0.5, 'Dados insuficientes ou não numéricos para plotar', horizontalalignment='center', verticalalignment='center')
            plt.axis('off')

    plt.savefig(output_path)  # Salva o gráfico no caminho especificado
    plt.tight_layout()  # Ajusta o layout para não cortar os labels
    plt.close()  # Fecha a figura para liberar memória
