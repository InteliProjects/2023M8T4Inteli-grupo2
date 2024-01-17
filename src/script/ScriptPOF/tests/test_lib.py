import os
import sys
import shutil
import tempfile
import unittest
import pandas as pd
import re
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pof.lib as funcao

# Funções de sucesso para testar

def test_traduzir_nomes_colunas_sucesso():
    # Criar arquivos de exemplo
    df_path = 'test_df.csv'
    mapeamento_path = 'test_mapeamento.csv'

    pd.DataFrame({'coluna1': [1, 2, 3], 'coluna2': ['a', 'b', 'c']}).to_csv(df_path, index=False)
    pd.DataFrame({'Código da variável': ['coluna1', 'coluna2'],
                  'Tradução código da variável': ['var1', 'var2']}).to_csv(mapeamento_path, index=False)

    # Executar a função e verificar se as colunas foram traduzidas corretamente
    assert 'var1' in funcao.traduzir_nomes_colunas(df_path, mapeamento_path).columns
    assert 'var2' in funcao.traduzir_nomes_colunas(df_path, mapeamento_path).columns

    # Limpar os arquivos de teste
    os.remove(df_path)
    os.remove(mapeamento_path)


def test_encontrar_codigos_com_branco_sucesso():
    arquivo_excel = 'arquivo_teste.xlsx'
    column_name = 'coluna'
    df_excel = pd.DataFrame({'coluna': ['a', ' ', 'c'], 'outra_coluna': [1, 2, 3]})
    df_excel.to_excel(arquivo_excel, index=False)
    valores_cod_variavel = funcao.encontrar_codigos_com_branco(arquivo_excel, column_name)
    assert valores_cod_variavel == [' ']

def test_preencher_valores_nulos_csv_sucesso():
    # Criar arquivo de exemplo
    arquivo_excel = 'test_arquivo.xlsx'
    
    df = pd.DataFrame({'coluna1': [1, 2, None], 'coluna2': ['a', None, 'c']})
    df.to_excel(arquivo_excel, index=False)

    # Executar a função e verificar se os valores nulos foram preenchidos corretamente
    df_resultado = funcao.preencher_valores_nulos_csv(df, arquivo_excel, 'coluna2')
    assert not df_resultado['coluna2'].isnull().any()

    # Limpar o arquivo de teste
    os.remove(arquivo_excel)


def test_translate_numeric_values_in_df_uf_sucesso():
    df_nulos = pd.DataFrame({'coluna1': [1, 2, 3], 'uf': [1, 2, 3]})
    csv_x = 'arquivo_teste.csv'
    column_z = 'uf'
    df_x = pd.DataFrame({'codigo': [1, 2, 3], 'estado': ['SP', 'RJ', 'MG']})
    df_x.to_csv(csv_x, index=False)
    df_resultado = funcao.translate_numeric_values_in_df_uf(df_nulos, csv_x, column_z)
    assert 'uf_traduzido' in df_resultado.columns

def test_translate_numeric_values_in_df_alimento_sucesso():
    df_nulos = pd.DataFrame({'coluna1': [1, 2, 3], 'alimento': [1, 2, 3]})
    csv_x = 'arquivo_teste.csv'
    column_z = 'alimento'
    df_x = pd.DataFrame({'codigo_alimento': [1, 2, 3], 'descricao_alimento': ['Arroz', 'Feijão', 'Macarrão']})
    df_x.to_csv(csv_x, index=False)
    df_resultado = funcao.translate_numeric_values_in_df_alimento(df_nulos, csv_x, column_z)
    assert 'alimento_traduzido' in df_resultado.columns

def test_tratar_valores_nulos_sucesso():
    df = pd.DataFrame({'coluna1': [1, 2, None], 'coluna2': ['a', None, 'c']})
    df_resultado = funcao.tratar_valores_nulos(df, substituto_para_nulos='ha')
    assert not df_resultado.isnull().values.any()

def test_ajustar_amazon_s3_sucesso():
    df = pd.DataFrame({'coluna1': [1, 2, 3], 'coluna2': ['a', 'b', 'c']})
    nome_arquivo_saida = 'saida_amazon_s3.csv'
    resultado = funcao.ajustar_amazon_s3(df, nome_arquivo_saida)
    assert resultado == nome_arquivo_saida

def test_ajustar_azure_blob_sucesso():
    df = pd.DataFrame({'coluna1': [1, 2, 3], 'coluna2': ['a', 'b', 'c']})
    nome_arquivo_saida = 'saida_azure_blob.csv'
    resultado = funcao.ajustar_azure_blob(df, nome_arquivo_saida)
    assert resultado == nome_arquivo_saida



# Funções de falha para testar

def test_traduzir_nomes_colunas_falha(tmp_path):
    # Cria um DataFrame de exemplo
    df = pd.DataFrame({'coluna1': [1, 2, 3], 'coluna2': ['a', 'b', 'c']})

    # Salva o DataFrame como CSV temporário
    caminho_dataframe = tmp_path / 'test_dataframe.csv'
    df.to_csv(caminho_dataframe, index=False)

    # Cria um DataFrame de mapeamento com uma coluna inexistente
    mapeamento = pd.DataFrame({'Código da variável': ['coluna1', 'coluna3'],
                                'Tradução código da variável': ['var1', 'var2']})

    # Salva o DataFrame de mapeamento como CSV temporário
    caminho_mapeamento = tmp_path / 'test_mapeamento.csv'
    mapeamento.to_csv(caminho_mapeamento, index=False)

    # Testa se a função retorna algo (não levanta exceção)
    resultado = funcao.traduzir_nomes_colunas(caminho_dataframe, caminho_mapeamento)  # Corrige a chamada da função
    assert resultado is not None

def test_encontrar_codigos_com_branco_falha():
    arquivo_excel = 'arquivo_teste.xlsx'
    column_name = 'coluna'
    df_excel = pd.DataFrame({'coluna': ['a', 'b', 'c'], 'outra_coluna': [1, 2, 3]})
    df_excel.to_excel(arquivo_excel, index=False)
    with pytest.raises(AssertionError):
        valores_cod_variavel = funcao.encontrar_codigos_com_branco(arquivo_excel, column_name)
        assert valores_cod_variavel == [' ']


def test_translate_numeric_values_in_df_uf_falha():
    df_nulos = pd.DataFrame({'coluna1': [1, 2, 3], 'uf': [1, 2, 3]})
    csv_x = 'arquivo_teste.csv'
    column_z = 'uf_inexistente'  # Coluna que não existe no DataFrame
    df_x = pd.DataFrame({'codigo': [1, 2, 3], 'estado': ['SP', 'RJ', 'MG']})
    df_x.to_csv(csv_x, index=False)
    with pytest.raises(KeyError):
        df_resultado = funcao.translate_numeric_values_in_df_uf(df_nulos, csv_x, column_z)

def test_translate_numeric_values_in_df_alimento_falha():
    df_nulos = pd.DataFrame({'coluna1': [1, 2, 3], 'alimento': [1, 2, 3]})
    csv_x = 'arquivo_teste.csv'
    column_z = 'alimento_inexistente'  # Coluna que não existe no DataFrame
    df_x = pd.DataFrame({'codigo_alimento': [1, 2, 3], 'descricao_alimento': ['Arroz', 'Feijão', 'Macarrão']})
    df_x.to_csv(csv_x, index=False)
    with pytest.raises(KeyError):
        df_resultado = funcao.translate_numeric_values_in_df_alimento(df_nulos, csv_x, column_z)

def test_tratar_valores_nulos_falha():
    df = pd.DataFrame({'coluna1': [1, 2, 3], 'coluna2': ['a', 'b', 'c']})
    funcao.tratar_valores_nulos(df, substituto_para_nulos='zero')

def test_ajustar_amazon_s3_falha():
    df = 'Isso não é um DataFrame'
    with pytest.raises(TypeError):
        funcao.ajustar_amazon_s3(df, 'saida_amazon_s3.csv')

def test_ajustar_azure_blob_falha():
    df = 42  # Alguma coisa que não seja um DataFrame
    with pytest.raises(AttributeError):
        funcao.ajustar_azure_blob(df, 'saida_azure_blob.csv')

if __name__ == '__main__':
    unittest.main()
