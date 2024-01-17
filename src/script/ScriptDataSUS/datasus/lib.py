import pandas as pd
import re
from datetime import datetime

def carregar_csv(caminho_arquivo, delimiter=','):
    return pd.read_csv(caminho_arquivo, delimiter=delimiter)

def carregar_csv_com_codificacao(caminho_arquivo, delimiter=',', chunk_size=None):
    codificacoes = ['utf-8', 'ISO-8859-1', 'cp1252']  # Lista de codificações comuns

    for codificacao in codificacoes:
        try:
            if chunk_size:
                return pd.read_csv(caminho_arquivo, delimiter=delimiter, encoding=codificacao, chunksize=chunk_size)
            else:
                return pd.read_csv(caminho_arquivo, delimiter=delimiter, encoding=codificacao)
        except UnicodeDecodeError:
            pass

    raise UnicodeDecodeError(f"Não foi possível ler o arquivo {caminho_arquivo} com as codificações testadas.")

def remover_coluna(df, nome_coluna):
    return df.drop(nome_coluna, axis=1)

def limpar_dados(df, colunas_a_ignorar=None, chunk_size=1000):
    def limpar_celula(celula):
        if isinstance(celula, str):
            return re.sub(r'[^\w\s]', '', celula)
        return celula

    colunas_a_ignorar = set(colunas_a_ignorar or [])
    chunks_limpos = []

    for start in range(0, df.shape[0], chunk_size):
        chunk = df[start:start + chunk_size]
        for coluna in chunk:
            if coluna not in colunas_a_ignorar:
                chunk[coluna] = chunk[coluna].apply(limpar_celula)
        chunks_limpos.append(chunk)

    df_limpo = pd.concat(chunks_limpos, ignore_index=True)
    return df_limpo

def tratar_valores_nulos(df, substituto_para_nulos, chunk_size=1000):
    chunks = [df[i:i + chunk_size] for i in range(0, df.shape[0], chunk_size)]
    chunks_tratados = [chunk.fillna(substituto_para_nulos) for chunk in chunks]

    df_tratado = pd.concat(chunks_tratados, ignore_index=True)
    return df_tratado


# TODO: Usar essa função no momento de implementação do código na empresa que utiliza AWS
def ajustar_amazon_s3(df, nome_arquivo_saida, chunk_size=100000):
    if not isinstance(df, pd.DataFrame):
        raise TypeError("O primeiro argumento deve ser um DataFrame.")

    for i in range(0, len(df), chunk_size):
        df_chunk = df.iloc[i:i+chunk_size]
        df_chunk = df_chunk.applymap(lambda x: x.replace(',', ';') if isinstance(x, str) else x)
        write_mode = 'w' if i == 0 else 'a'
        header = True if i == 0 else False
        df_chunk.to_csv(nome_arquivo_saida, mode=write_mode, header=header, index=False, encoding='utf-8')

    return nome_arquivo_saida

# TODO: Usar essa função no momento de implementação do código na empresa que utiliza Azure
def ajustar_azure_blob(df, nome_arquivo):
    df = df.applymap(lambda x: x.replace(',', ';') if isinstance(x, str) else x)

    df.to_csv(nome_arquivo, index=False, encoding='utf-8')

    return nome_arquivo
