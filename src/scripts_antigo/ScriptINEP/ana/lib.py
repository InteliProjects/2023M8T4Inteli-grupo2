import pandas as pd
import numpy as np

# Fazemos o load data
def preprocess():
    print("Teste ANA!")
    
def load_data(path_to_file):
    # Ler o arquivo CSV usando pandas
    df = pd.read_csv(path_to_file)

    return df

def clean_data(data):
    if not isinstance(data, pd.DataFrame):
        raise TypeError("A entrada deve ser um DataFrame do Pandas.")
    
    cleaned_data = data.fillna("null")
    return cleaned_data


def ajustar_amazon_s3(df, nome_arquivo):
    # Tratando os dados - remover caracteres que podem causar problemas
    df = df.applymap(lambda x: x.replace(',', ';') if isinstance(x, str) else x)

    # Salvar o DataFrame em um arquivo CSV com a codificação UTF-8
    df.to_csv(nome_arquivo, index=False, encoding='utf-8')

    # Retornar o nome do arquivo para confirmar a criação do arquivo
    return nome_arquivo

def ajustar_azure_blob(df, nome_arquivo):
    # Tratando os dados - por exemplo, substituir NaN por strings vazias e remover caracteres que podem causar problemas
    df = df.applymap(lambda x: x.replace(',', ';') if isinstance(x, str) else x)

    # Salvar o DataFrame em um arquivo CSV com a codificação UTF-8 e delimitador padrão
    df.to_csv(nome_arquivo, index=False, encoding='utf-8')

    # Retornar o nome do arquivo para confirmar a criação do arquivo
    return nome_arquivo

