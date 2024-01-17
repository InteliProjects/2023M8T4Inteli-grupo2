import pandas as pd
import numpy as np
from pandas.errors import ParserError

# Fazemos o load data
def preprocess():
    print("Teste Enceja!")
    

def load_data(path_to_file, encoding='ISO-8859-1'):
    try:
        # Ler o arquivo CSV usando pandas com o encoding especificado
        df = pd.read_csv(path_to_file, encoding=encoding)

        return df
    except Exception as e:
        print(f"Ocorreu um erro ao carregar o arquivo: {e}")
        return None


def clean_data(df):
    df = pd.DataFrame(df)
    # Removendo linhas que contêm valores NaN
    cleaned_df = df.dropna()

    return cleaned_df

def load_data_with_correct_delimiter(path_to_file):
    # Lista de codificações comuns a serem testadas
    encodings = ['utf-8', 'ISO-8859-1']
    
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


def ajustar_amazon_s3(df, nome_arquivo_saida, chunk_size=10000):
    # Verifique se df é um DataFrame
    if not isinstance(df, pd.DataFrame):
        raise TypeError("O primeiro argumento deve ser um DataFrame.")

    # Dividindo o DataFrame em chunks e processando cada um
    for i in range(0, len(df), chunk_size):
        # Selecionando o chunk
        df_chunk = df.iloc[i:i+chunk_size]

        # Aplica a transformação
        df_chunk = df_chunk.applymap(lambda x: x.replace(',', ';') if isinstance(x, str) else x)

        # Modo de escrita: 'w' para o primeiro chunk, 'a' para os subsequentes
        write_mode = 'w' if i == 0 else 'a'

        # Cabeçalho: incluído apenas no primeiro chunk
        header = True if i == 0 else False

        # Salva o chunk no arquivo CSV
        df_chunk.to_csv(nome_arquivo_saida, mode=write_mode, header=header, index=False, encoding='utf-8')

    # Retornar o nome do arquivo para confirmar a criação do arquivo
    return nome_arquivo_saida



def ajustar_azure_blob(df, nome_arquivo):
    # Tratando os dados - por exemplo, substituir NaN por strings vazias e remover caracteres que podem causar problemas
    df = df.fillna('')
    df = df.applymap(lambda x: x.replace(',', ';') if isinstance(x, str) else x)

    # Salvar o DataFrame em um arquivo CSV com a codificação UTF-8 e delimitador padrão
    df.to_csv(nome_arquivo, index=False, encoding='utf-8')

    # Retornar o nome do arquivo para confirmar a criação do arquivo
    return nome_arquivo

