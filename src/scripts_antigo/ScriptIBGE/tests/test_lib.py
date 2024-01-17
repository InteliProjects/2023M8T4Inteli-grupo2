# test_lib.py
import sys
import os
import pandas as pd
import numpy as np
import pytest

# Adicionando o diretório raiz ao path para importar o módulo lib
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import ibge.lib as ibge


def test_preprocess_output(capfd):  # capfd é um "fixture" do pytest para capturar saídas impressas.
    ibge.preprocess()
    out, err = capfd.readouterr()
    assert out == "Teste IBGE!\n", "A saída impressa não corresponde ao esperado"

def test_clean_data_success():
    # Criando um DataFrame sem valores NaN
    data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
    df = pd.DataFrame(data)
    
    # Testando a função clean_data
    result = ibge.clean_data(df)
    
    # Verifica se o DataFrame resultante é igual ao DataFrame original
    assert result.equals(df), "Teste falhou: O DataFrame resultante deveria ser igual ao original."

def test_clean_data_failure():
    # Criando um DataFrame com valores NaN
    data = {'col1': [1, 2, None], 'col2': [4, None, 6]}
    df = pd.DataFrame(data)
    
    # Testando a função clean_data
    result = ibge.clean_data(df)
    
    # Verifica se o DataFrame resultante é diferente do DataFrame original
    assert not result.equals(df), "Teste falhou: O DataFrame resultante não deveria ser igual ao original."


def teste_ajustar_amazon_s3_sucesso():
    # Cria um DataFrame de teste
    dados = {'coluna1': ['a,b', 'c,d'], 'coluna2': [1, 2]}
    df_teste = pd.DataFrame(dados)

    # Nome do arquivo de teste
    nome_arquivo = 'teste.csv'

    # Executa a função
    resultado = ibge.ajustar_amazon_s3(df_teste, nome_arquivo)

    # Verifica se o resultado é o esperado
    assert resultado == nome_arquivo
    assert os.path.isfile(nome_arquivo)  # Verifica se o arquivo foi criado

    # Limpa (remove o arquivo de teste)
    os.remove(nome_arquivo)


def teste_ajustar_amazon_s3_falha():
    # Cria um DataFrame de teste
    dados = {'coluna1': ['a,b', 'c,d'], 'coluna2': [1, 2]}
    df_teste = pd.DataFrame(dados)

    # Define um nome de arquivo inválido (caminho que não existe ou sem permissão de escrita)
    nome_arquivo_invalido = '/caminho/inexistente/teste.csv'

    # Verifica se a função levanta uma exceção ao tentar escrever em um arquivo inválido
    with pytest.raises(Exception):  # Substituir 'Exception' pela exceção específica esperada, se aplicável
        ibge.ajustar_amazon_s3(df_teste, nome_arquivo_invalido)




# Rodando os testes
test_clean_data_success()
test_clean_data_failure()
teste_ajustar_amazon_s3_sucesso()
