import sys
import pandas as pd
import numpy as np
import pytest
import os

# Adicionando o diretório raiz ao path para importar o módulo lib
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import ed_superior.lib as ed_sup

def test_clean_data_sucesso():
    data = pd.DataFrame({'A': [1, np.nan, 3], 'B': [4, 5, np.nan]})
    cleaned_data = ed_sup.clean_data(data)
    assert cleaned_data.isnull().sum().sum() == 0, "Ainda existem valores NaN"

def test_clean_data_falha():
    with pytest.raises(TypeError):
        ed_sup.clean_data("isso não é um dataframe")
        
def test_ajustar_amazon_s3_sucesso():
    df = pd.DataFrame({'coluna1': ['a,b', 'c,d'], 'coluna2': [1, 2]})
    nome_arquivo = 'teste.csv'
    assert ed_sup.ajustar_amazon_s3(df, nome_arquivo) == nome_arquivo
    assert os.path.isfile(nome_arquivo)
    os.remove(nome_arquivo)

def test_ajustar_amazon_s3_falha():
    df = pd.DataFrame({'coluna1': ['a,b', 'c,d'], 'coluna2': [1, 2]})
    nome_arquivo_invalido = '/caminho/invalido/teste.csv'
    with pytest.raises(Exception):
        ed_sup.ajustar_amazon_s3(df, nome_arquivo_invalido)
        

test_clean_data_sucesso()
test_clean_data_falha()
test_ajustar_amazon_s3_sucesso()
test_ajustar_amazon_s3_falha()