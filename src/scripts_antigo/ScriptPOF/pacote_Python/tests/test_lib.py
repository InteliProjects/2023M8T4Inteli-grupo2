import os
import pandas as pd
import numpy as np
import intelidata.lib as inteli
import pytest

def test_encontrar_codigos_com_branco_funciona(tmp_path):
    df_teste = pd.DataFrame({'Código da variável': ['A', 'B', 'C'],
                             'Coluna1': ['branco teste', 'valor', 'outra palavra']})
    arquivo_excel_temp = tmp_path / 'teste_encontrar_codigos_com_branco.xlsx'
    df_teste.to_excel(arquivo_excel_temp, index=False)

    codigos = inteli.encontrar_codigos_com_branco(arquivo_excel_temp, sheet_name=0, column_name='Código da variável')

    assert codigos == ['A'], "A função não retornou os códigos corretamente."

def test_encontrar_codigos_com_branco_nao_funciona(capfd):
    with pytest.raises(FileNotFoundError):
        with capfd.disabled():
            inteli.encontrar_codigos_com_branco('arquivo_inexistente.xlsx', sheet_name=0, column_name='Código da variável')

def test_preencher_valores_nulos_csv_funciona(tmp_path):
    df_teste = pd.DataFrame({'A': [np.nan, 1.0, 3],
                             'B': [np.nan, 'branco', 6],
                             'C': [np.nan, 'branco', 9]})
    arquivo_csv_temp = tmp_path / 'teste_preencher_valores_nulos.csv'
    df_teste.to_csv(arquivo_csv_temp, index=False)
    arquivo_excel_temp = tmp_path / 'teste_encontrar_codigos_com_branco.xlsx'
    pd.DataFrame({'Código da variável': ['A', 'B', 'C']}).to_excel(arquivo_excel_temp, index=False)

    df_resultado = inteli.preencher_valores_nulos_csv(arquivo_csv_temp, arquivo_excel_temp, sheet_name=0, column_name='Código da variável')

    print("Resultado da função:", df_resultado)

    assert df_resultado['A'].tolist() == ['vazio', 1, 3], "A função não preencheu os valores nulos corretamente. (teste a)"
    assert df_resultado['B'].tolist() == ['vazio', 'branco', '6'], "A função não preencheu os valores nulos corretamente. (teste b)"
    assert df_resultado['C'].tolist() == ['vazio', 'branco', '9'], "A função não preencheu os valores nulos corretamente. (teste c)"


def test_preencher_valores_nulos_csv_nao_funciona(capfd):
    with pytest.raises(FileNotFoundError):
        with capfd.disabled():
            inteli.preencher_valores_nulos_csv('arquivo_inexistente.csv', 'arquivo_excel.xlsx', sheet_name=0, column_name='Código da variável')

def test_salvar_dataframes_como_csv_funciona(tmp_path):
    df1 = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
    df2 = pd.DataFrame({'X': [10, 20, 30], 'Y': ['apple', 'banana', 'cherry']})
    arquivos_temp = [tmp_path / 'teste_df1.csv', tmp_path / 'teste_df2.csv']
    nomes_temp = ['df1.csv', 'df2.csv']
    for df, nome in zip([df1, df2], arquivos_temp):
        df.to_csv(nome, index=False)

    inteli.salvar_dataframes_como_csv([df1, df2], nomes_temp, pasta_destino=tmp_path)

    for nome in nomes_temp:
        assert os.path.exists(os.path.join(tmp_path, nome)), f"O arquivo CSV {nome} não foi criado."

def test_load_data_funciona(tmp_path):
    df_teste = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
    arquivo_csv_temp = tmp_path / 'teste_load_data.csv'
    df_teste.to_csv(arquivo_csv_temp, index=False)

    data = inteli.load_data(arquivo_csv_temp)

    assert isinstance(data, np.ndarray), "A função não retornou um array NumPy."

def test_load_data_nao_funciona(capfd):
    with pytest.raises(FileNotFoundError):
        with capfd.disabled():
            inteli.load_data('arquivo_inexistente.csv')
