import os 
import pandas as pd
#import openpyxl



def encontrar_codigos_com_branco(arquivo_excel, column_name):
    df_excel = pd.read_excel(arquivo_excel)
    def has_branco(row):
        return any(isinstance(value, str) and value.strip() == '' for value in row.values)
    linhas_com_branco = df_excel[df_excel.apply(has_branco, axis=1)]
    valores_cod_variavel = linhas_com_branco[column_name].tolist()
    return valores_cod_variavel

def preencher_valores_nulos_csv(df, arquivo_excel, column_name):
    cols_to_fill_na_aplicavel = encontrar_codigos_com_branco(arquivo_excel, column_name)
    df[cols_to_fill_na_aplicavel] = df[cols_to_fill_na_aplicavel].fillna('nao_aplicavel')
    df = df.fillna('-1')
    return df

def tratar_valores_nulos(df, substituto_para_nulos, chunk_size=1000):
    chunks = [df[i:i + chunk_size] for i in range(0, df.shape[0], chunk_size)]
    chunks_tratados = [chunk.fillna(substituto_para_nulos) for chunk in chunks]
    df_tratado = pd.concat(chunks_tratados, ignore_index=True)
    return df_tratado

def translate_numeric_values_in_df_uf(df_nulos, csv_x, column_z):
    df_x = pd.read_csv(csv_x)
    mapping_dict = pd.Series(df_x.estado.values, index=df_x.codigo.astype(str)).to_dict()
    translated_column = df_nulos[column_z].astype(str).map(mapping_dict)
    col_index = df_nulos.columns.get_loc(column_z)
    df_nulos.insert(col_index + 1, f"{column_z}_traduzido", translated_column)

    return df_nulos

def translate_numeric_values_in_df_alimento(df_nulos, csv_x, column_z):
    df_x = pd.read_csv(csv_x)
    mapping_dict = pd.Series(df_x.descricao_alimento.values, index=df_x.codigo_alimento.astype(str)).to_dict()
    translated_column = df_nulos[column_z].astype(str).map(mapping_dict)
    col_index = df_nulos.columns.get_loc(column_z)
    df_nulos.insert(col_index + 1, f"{column_z}_traduzido", translated_column)

    return df_nulos

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

