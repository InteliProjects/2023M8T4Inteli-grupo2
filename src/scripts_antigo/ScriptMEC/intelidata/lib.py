import os
import pandas as pd
import boto3

def listar_arquivos_csv(diretorio):
    """ Lista todos os arquivos CSV no diretório especificado. """
    return [arquivo for arquivo in os.listdir(diretorio) if arquivo.endswith('.csv')]

def ler_e_processar_csv(nome_arquivo, diretorio):
    caminho_completo = os.path.join(diretorio, nome_arquivo)
    try:
        df = pd.read_csv(caminho_completo, sep=',')
    except pd.errors.ParserError:
        try:
            df = pd.read_csv(caminho_completo, sep=';', error_bad_lines=False)
        except Exception as e:
            print(f"Erro ao ler o arquivo {nome_arquivo}: {e}")
            df = pd.DataFrame()  # Retorna um DataFrame vazio em caso de erro
    return df


    if processamento_func:
        df = processamento_func(df)

    return df

def processamento_basico(df):
    """ Realiza processamento básico em um DataFrame. """
    # Exemplo: substituir valores nulos por um valor padrão
    return df.fillna('valor_padrao')

def upload_para_s3(cliente_s3, bucket_name, df, nome_arquivo):
    """ Converte um DataFrame para CSV e faz upload para o AWS S3. """
    caminho_temp = '/tmp/' + nome_arquivo
    df.to_csv(caminho_temp, index=False)

    cliente_s3.upload_file(caminho_temp, bucket_name, nome_arquivo)
    print(f'O arquivo {nome_arquivo} foi enviado para o Amazon S3.')

# Uso das funções
def processar_e_enviar_arquivos_s3(diretorio, bucket_name, cliente_s3):
    nomes_arquivos = listar_arquivos_csv(diretorio)
    for nome_arquivo in nomes_arquivos:
        df = ler_e_processar_csv(nome_arquivo, diretorio, processamento_basico)
        upload_para_s3(cliente_s3, bucket_name, df, nome_arquivo)

# Configuração do cliente S3 (este código deve vir do seu script original)
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, 
                  aws_secret_access_key=aws_secret_access_key, 
                  region_name=region_name, aws_session_token=aws_session_token)

# Processa e envia arquivos para o S3
processar_e_enviar_arquivos_s3('./sisu', 'dadosmecdatadream', s3)
