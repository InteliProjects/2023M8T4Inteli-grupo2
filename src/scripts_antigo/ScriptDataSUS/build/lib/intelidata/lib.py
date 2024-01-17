import os
import pandas as pd

def obter_nomes_arquivos(pasta):
    nomes_arquivos = []
    for nome_arquivo in os.listdir(pasta):
        if nome_arquivo.endswith('.csv'):
            nomes_arquivos.append(nome_arquivo)
    return nomes_arquivos

def ler_arquivo_csv(caminho_completo_arquivo, separadores):
    for separador in separadores:
        try:
            df = pd.read_csv(caminho_completo_arquivo, encoding='latin1', sep=separador)
            break
        except pd.errors.ParserError:
            continue
    return df

def tratar_e_salvar_arquivo(nome_arquivo, pasta, pasta_tratados, valor_preenchimento):
    caminho_completo_arquivo = os.path.join(pasta, nome_arquivo)
    separadores = [',', ';']
    df = ler_arquivo_csv(caminho_completo_arquivo, separadores)
    df = df.fillna(valor_preenchimento)
    caminho_arquivo_tratado = os.path.join(pasta_tratados, f"{nome_arquivo}_tratado.csv")
    df.to_csv(caminho_arquivo_tratado, index=False, sep=separadores[0], encoding='utf-8')  # Use o primeiro separador
    print(f"Arquivo {nome_arquivo} tratado e salvo como {caminho_arquivo_tratado}")

def processar_arquivos_csv():
    pasta = './csv'
    nomes_arquivos = obter_nomes_arquivos(pasta)

    pasta_tratados = './csv_tratados'
    valor_preenchimento = "null"

    for nome_arquivo in nomes_arquivos:
        tratar_e_salvar_arquivo(nome_arquivo, pasta, pasta_tratados, valor_preenchimento)
