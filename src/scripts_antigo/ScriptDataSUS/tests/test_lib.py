import os
import csv
import shutil
import tempfile
import intelidata.lib as inteli
import unittest
import pandas as pd

class TesteObterNomesArquivos(unittest.TestCase):

    def setUp(self):
        self.diretorio_temporario = tempfile.mkdtemp()
        self.diretorio_temporario_vazio = tempfile.mkdtemp()
        self.caminho_csv = self.criar_arquivo_csv_populado()

    def tearDown(self):
        if os.path.exists(self.diretorio_temporario):
            shutil.rmtree(self.diretorio_temporario)
            
        if os.path.exists(self.diretorio_temporario_vazio):
            shutil.rmtree(self.diretorio_temporario_vazio)

    def criar_arquivo_csv_populado(self):
        caminho_arquivo_csv = os.path.join(self.diretorio_temporario, 'dados.csv')

        dados = [
            ['Nome', 'Idade', 'Cidade'],
            ['João', 25, 'São Paulo'],
            ['Maria', 30, 'Rio de Janeiro'],
            ['Carlos', 22, 'Belo Horizonte']
        ]

        with open(caminho_arquivo_csv, mode='w', newline='') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)
            escritor_csv.writerows(dados)

        return caminho_arquivo_csv

    def teste_obter_nome_arquivo_funcionando(self):
        resultado = inteli.obter_nomes_arquivos(self.diretorio_temporario)

        if 'O diretório' in resultado:
            self.fail(resultado)
        elif 'não é um diretório' in resultado:
            self.fail(resultado)
        elif 'está vazio' in resultado:
            print(resultado)
        else:
            print(resultado)

    def teste_ler_arquivo_csv_funcionando(self):
        resultado = inteli.ler_arquivo_csv(self.caminho_csv, ',')

        self.assertFalse(resultado.empty, "O DataFrame está vazio.")

    def teste_tratar_e_salvar_arquivo(self):
   
        pasta_tratados = self.diretorio_temporario_vazio
        valor_preenchimento = 'N/A'
        resultado = inteli.tratar_e_salvar_arquivo(self.caminho_csv, pasta_tratados, valor_preenchimento)
        
        print(resultado)
    

if __name__ == '__main__':
    unittest.main()
