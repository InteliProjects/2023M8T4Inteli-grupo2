import os 
import pandas as pd

def encontrar_codigos_com_branco(arquivo_excel, sheet_name, column_name):
    df_excel = pd.read_excel(arquivo_excel, sheet_name=sheet_name)
    def has_branco(row):
        for value in row.values:
            if isinstance(value, str) and 'branco' in value:
                return True
        return False
    linhas_com_branco = df_excel[df_excel.apply(has_branco, axis=1)]
    valores_cod_variavel = linhas_com_branco[column_name].tolist()
    print(valores_cod_variavel)

    return valores_cod_variavel


def preencher_valores_nulos_csv(arquivo_csv, arquivo_excel, sheet_name, column_name):
    df_rendimento = pd.read_csv(arquivo_csv)
    cols_to_fill_na_aplicavel = encontrar_codigos_com_branco(arquivo_excel, sheet_name, column_name)
    df_rendimento[cols_to_fill_na_aplicavel] = df_rendimento[cols_to_fill_na_aplicavel].fillna('nao_aplicavel')
    df_rendimento = df_rendimento.fillna('vazio')
    df = df_rendimento
    return df

def salvar_dataframes_como_csv(lista_dataframes, nomes_arquivos, pasta_destino='csvs_tratados'):
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    for df, nome_arquivo in zip(lista_dataframes, nomes_arquivos):
        caminho_completo = os.path.join(pasta_destino, nome_arquivo)
        df.to_csv(caminho_completo, index=False)
    
def load_data(path_to_file):
    df = pd.read_csv(path_to_file)
    data = df.to_numpy()

    return data
