import pandas as pd
import numpy as np

# Fazemos o load data
def preprocess():
    print("Teste IBGE!")
    
def clean_data(df):
    df = pd.DataFrame(df)
    cleaned_df = df.dropna()

    return cleaned_df

def load_data_with_correct_delimiter(path_to_file):
    try:
        df = pd.read_csv(path_to_file, delimiter=';')
    except pd.errors.ParserError:
        with open(path_to_file, 'r') as file:
            file_content = file.read()
        file_content = file_content.replace(';', ',')
        with open(path_to_file, 'w') as file:
            file.write(file_content)

        df = pd.read_csv(path_to_file, delimiter=',')

    return df

def ajustar_amazon_s3(df, nome_arquivo):
    df = df.applymap(lambda x: x.replace(',', ';') if isinstance(x, str) else x)

    df.to_csv(nome_arquivo, index=False, encoding='utf-8')

    return nome_arquivo

def ajustar_azure_blob(df, nome_arquivo):
    df = df.applymap(lambda x: x.replace(',', ';') if isinstance(x, str) else x)

    df.to_csv(nome_arquivo, index=False, encoding='utf-8')

    return nome_arquivo

