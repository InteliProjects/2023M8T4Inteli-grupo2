import pandas as pd
import numpy as np

# Fazemos o load data
def preprocess():
    print("Vamos processar os dados!")
    
def load_data(path_to_file):
    # Ler o arquivo CSV usando pandas
    df = pd.read_csv(path_to_file)

    # Converter o DataFrame para um array NumPy
    data = df.to_numpy()

    return data

def clean_data(df):
    df = pd.DataFrame(df)
    # Removendo linhas que contêm valores NaN
    cleaned_df = df.dropna()

    return cleaned_df