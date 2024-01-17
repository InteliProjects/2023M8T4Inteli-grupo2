import os
import sys
import shutil
import tempfile
import unittest
import pandas as pd
import re
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import datasus.lib as funcao

# Funções de sucesso para testar

def test_carregar_csv_sucesso():
    df = funcao.carregar_csv('tests/csv_teste/teste.csv')
    assert isinstance(df, pd.DataFrame)

def test_carregar_csv_com_codificacao_sucesso():
    df = funcao.carregar_csv_com_codificacao('tests/csv_teste/teste.csv')
    assert isinstance(df, pd.DataFrame)

def test_remover_coluna_sucesso():
    df = pd.DataFrame({'coluna1': [1, 2, 3], 'coluna2': ['a', 'b', 'c']})
    df_resultado = funcao.remover_coluna(df, 'coluna1')
    assert 'coluna1' not in df_resultado.columns

def test_limpar_dados_sucesso():
    df = pd.DataFrame({'coluna1': ['1', '2', '3'], 'coluna2': ['a!', 'b@', 'c#']})
    df_resultado = funcao.limpar_dados(df)
    assert all(df_resultado.applymap(lambda x: isinstance(x, str)))

def test_tratar_valores_nulos_sucesso():
    df = pd.DataFrame({'coluna1': [1, 2, None], 'coluna2': ['a', None, 'c']})
    df_resultado = funcao.tratar_valores_nulos(df, substituto_para_nulos=0)
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

def test_carregar_csv_falha():
    with pytest.raises(FileNotFoundError):
        funcao.carregar_csv('caminho/inexistente/teste.csv')

def test_carregar_csv_com_codificacao_falha_nenhum_arquivo():
    with pytest.raises(ValueError):
        funcao.carregar_csv_com_codificacao(None, delimiter=',')

def test_remover_coluna_falha():
    df = pd.DataFrame({'coluna1': [1, 2, 3], 'coluna2': ['a', 'b', 'c']})
    with pytest.raises(KeyError):
        funcao.remover_coluna(df, 'coluna_inexistente')

def test_limpar_dados_falha():
    df = 42  # Alguma coisa que não seja um DataFrame
    with pytest.raises(AttributeError):
        funcao.limpar_dados(df)

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
