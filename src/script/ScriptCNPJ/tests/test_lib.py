import os
import sys
import shutil
import tempfile
import unittest
import pandas as pd
import re
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import cnpj.lib as funcao

class TesteFuncoes(unittest.TestCase):

    def teste_carregar_dados_delimitador_correto_sucesso(self):
        dados = {'coluna1': ['a,b', 'c,d'], 'coluna2': [1, 2]}
        df_teste = pd.DataFrame(dados)
        nome_arquivo = 'teste.csv'
        df_teste.to_csv(nome_arquivo, index=False)
        resultado = funcao.carregar_dados_delimitador_correto(nome_arquivo, delimiter=',')
        self.assertIsInstance(resultado, pd.DataFrame)
        os.remove(nome_arquivo)

    def teste_carregar_dados_delimitador_correto_falha(self):
        nome_arquivo_inexistente = '/caminho/inexistente/teste.csv'
        with self.assertRaises(FileNotFoundError):
            funcao.carregar_dados_delimitador_correto(nome_arquivo_inexistente, delimiter=',')

    def teste_limpar_dados_sucesso(self):
        dados = {'coluna1': ['a,b', 'c,d'], 'coluna2': [1, 2]}
        df_teste = pd.DataFrame(dados)
        resultado = funcao.limpar_dados(df_teste)
        self.assertIsInstance(resultado, pd.DataFrame)

    def teste_limpar_dados_falha(self):
        df_teste = pd.DataFrame({'coluna1': ['a,b', 'c,d'], 'coluna2': [1, 2]})      
        funcao.limpar_dados(df_teste)

    def teste_tratar_valores_nulos_sucesso(self):
        dados = {'coluna1': [1, 2, None], 'coluna2': ['a', None, 'c']}
        df_teste = pd.DataFrame(dados)
        resultado = funcao.tratar_valores_nulos(df_teste, substituto_para_nulos=0)
        self.assertIsInstance(resultado, pd.DataFrame)

    def teste_tratar_valores_nulos_falha(self):
        df_teste = pd.DataFrame({'coluna1': [1, 2, None], 'coluna2': ['a', None, 'c']})
        with self.assertRaises(TypeError):
            funcao.tratar_valores_nulos(df_teste)  # Removido o argumento inexistente

    def teste_ajustar_azure_blob_sucesso(self):
        dados = {'coluna1': ['a,b', 'c,d'], 'coluna2': [1, 2]}
        df_teste = pd.DataFrame(dados)
        nome_arquivo = 'teste.csv'
        resultado = funcao.ajustar_azure_blob(df_teste, nome_arquivo)
        self.assertEqual(resultado, nome_arquivo)
        self.assertTrue(os.path.isfile(nome_arquivo))
        os.remove(nome_arquivo)

    def teste_ajustar_azure_blob_falha(self):
        df_teste = pd.DataFrame({'coluna1': ['a,b', 'c,d'], 'coluna2': [1, 2]})
        nome_arquivo_invalido = '/caminho/inexistente/teste.csv'
        with self.assertRaises(Exception):
            funcao.ajustar_azure_blob(df_teste, nome_arquivo_invalido)

    def teste_ajustar_amazon_s3_sucesso(self):
        dados = {'coluna1': ['a,b', 'c,d'], 'coluna2': [1, 2]}
        df_teste = pd.DataFrame(dados)
        resultado = funcao.ajustar_amazon_s3(df_teste, 'teste.csv')
        # Adicione os testes adequados para a função ajustar_amazon_s3
        self.assertEqual(resultado, 'teste.csv')  # Substitua pelo que é esperado para seu caso
        # Adicione mais asserções conforme necessário

    def teste_ajustar_amazon_s3_falha(self):
        df_teste = pd.DataFrame({'coluna1': ['a,b', 'c,d'], 'coluna2': [1, 2]})
        nome_arquivo_invalido = '/caminho/inexistente/teste.csv'
        with self.assertRaises(Exception):
            funcao.ajustar_amazon_s3(df_teste, nome_arquivo_invalido)


if __name__ == '__main__':
    unittest.main()
