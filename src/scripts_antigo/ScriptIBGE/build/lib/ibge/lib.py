import pandas as pd
import numpy as np

# Fazemos o load data
def preprocess():
    print("Teste IBGE!")
    

def clean_data(df):
    df = pd.DataFrame(df)
    # Removendo linhas que contêm valores NaN
    cleaned_df = df.dropna()

    return cleaned_df

def load_data_with_correct_delimiter(path_to_file):
    try:
        # Tente ler o arquivo CSV com o delimitador correto (;)
        df = pd.read_csv(path_to_file, delimiter=';')
    except pd.errors.ParserError:
        # Se a leitura falhar, trate a exceção substituindo o ; por , no arquivo
        with open(path_to_file, 'r') as file:
            file_content = file.read()
        file_content = file_content.replace(';', ',')
        with open(path_to_file, 'w') as file:
            file.write(file_content)

        # Tente carregar o arquivo novamente
        df = pd.read_csv(path_to_file, delimiter=',')

    return df

def ajustar_amazon_s3(df, nome_arquivo):
    # Tratando os dados - por exemplo, substituir NaN por strings vazias e remover caracteres que podem causar problemas
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

