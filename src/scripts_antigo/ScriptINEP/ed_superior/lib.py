import pandas as pd
import numpy as np
from pandas.errors import ParserError

# Fazemos o load data
def preprocess():
    print("Teste Educação Superior!")

def load_data_with_correct_delimiter(path_to_file):
    # Lista de codificações comuns a serem testadas
    encodings = ['utf-8', 'ISO-8859-1', 'latin1', 'Windows-1252']
    
    for encoding in encodings:
        try:
            # Tente ler o arquivo com o delimitador ';' e a codificação atual
            df = pd.read_csv(path_to_file, delimiter=';', encoding=encoding)
            print(f"Arquivo carregado com sucesso usando a codificação {encoding}")
            return df
        except UnicodeDecodeError as e:
            # Se houver um erro de decodificação, vá para a próxima codificação
            print(f"Erro de decodificação com a codificação {encoding}: {e}")
        except ParserError as e:
            # Se houver um erro de delimitador, tente corrigi-lo
            print(f"Erro de delimitador com a codificação {encoding}: {e}")
            try:
                # Tente substituir ';' por ',' e ler o arquivo novamente
                with open(path_to_file, 'r', encoding=encoding) as file:
                    file_content = file.read().replace(';', ',')
                
                # Escreva o conteúdo corrigido em um novo arquivo temporário
                temp_path = "temp_file.csv"
                with open(temp_path, 'w', encoding=encoding) as file:
                    file.write(file_content)
                
                # Tente ler o novo arquivo com o delimitador ','
                df = pd.read_csv(temp_path, delimiter=',', encoding=encoding)
                print(f"Arquivo carregado com sucesso após substituir delimitador usando a codificação {encoding}")
                return df
            except Exception as e:
                # Se ainda houver um erro, vá para a próxima codificação
                print(f"Erro ao ler o arquivo após substituir delimitador com a codificação {encoding}: {e}")

    # Se nenhuma codificação funcionar, levante uma exceção
    raise ValueError("Não foi possível ler o arquivo com as codificações e delimitadores testados.")

def clean_data(data):
    if not isinstance(data, pd.DataFrame):
        raise TypeError("A entrada deve ser um DataFrame do Pandas.")
    
    cleaned_data = data.fillna("null")
    return cleaned_data

def ajustar_amazon_s3(df, nome_arquivo):
    # Tratando os dados - por exemplo, substituir NaN por strings vazias e remover caracteres que podem causar problemas
    df = df.applymap(lambda x: x.replace(',', ';') if isinstance(x, str) else x)

    # Salvar o DataFrame em um arquivo CSV com a codificação UTF-8
    df.to_csv(nome_arquivo, index=False, encoding='utf-8')

    # Retornar o nome do arquivo para confirmar a criação do arquivo
    return nome_arquivo

def ajustar_azure_blob(df, nome_arquivo):
    # Tratando os dados - por exemplo, substituir NaN por strings vazias e remover caracteres que podem causar problemas
    df = df.fillna('')
    df = df.applymap(lambda x: x.replace(',', ';') if isinstance(x, str) else x)

    # Salvar o DataFrame em um arquivo CSV com a codificação UTF-8 e delimitador padrão
    df.to_csv(nome_arquivo, index=False, encoding='utf-8')

    # Retornar o nome do arquivo para confirmar a criação do arquivo
    return nome_arquivo

