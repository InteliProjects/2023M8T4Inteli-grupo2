# 1. Package Pesquisa de orçamento familiar
Este pacote é dedicado ao tratamento e envio para a AWS S3 de dados relacionados à pesquisa de orçamento familiar realizada nos anos de 2017 e 2018, selecionados para atender às necessidades do projeto. Seu objetivo principal é facilitar o processamento e análise desses dados, garantindo uma integração com as ferramentas da AWS. As instruções abaixo guiarão você no uso adequado deste pacote, desde a execução dos notebooks Jupyter até a realização de testes do código.
## 1.1 Arquivos do pacote
Este é um breve guia sobre os arquivos contidos neste pacote Python.
- **.env**: Arquivo de configuração de ambiente. Contém as keys da AWS Lab. 
- **.gitignore**: Arquivo de configuração do Git para ignorar o arquivo  ``.env.tmpl`` durante o versionamento.
- **.ipynb_checkpoints**: Diretório que armazena checkpoints automáticos de notebooks Jupyter.
- **.pytest_cache**: Diretório que armazena cache e dados temporários do Pytest.
- **build**: Diretório gerado durante o processo de construção do pacote. Contém arquivos intermediários.
- **csvs**: Diretório para armazenar os arquivos CSV relacionados à pesquisa de orçamento familiar. Para o bom funcionamento desse script, é preciso copiar todos arquivos dessa pasta e colar na raiz da pasta pacote python. Os arquivos dessa pasta não devem ser excluídos, mas, após o uso, todos aqueles que foram copiados devem ser excluídos. **ATENÇÃO: o arquivo "Dicionários de variáveis.xlsx" NÃO deve ser excluído sob nenhuma hipótese.**
- **csvs_tratados**: Diretório para armazenar os arquivos CSV pré-processados pelo código. Essa pasta deve ser esvaziada sempre que o código for rodado.
- **inteli.ipynb**: Jupyter Notebook principal do projeto, que contém todo o processo de tratamento dos dados CSV.
- **intelidata**: Pacote Python principal.
  - **__init__.py**: Arquivo necessário para que o diretório seja tratado como um pacote Python.
  
  - **lib.py**: Módulo Python contendo funcionalidades específicas. Aqui são definidas todas as funções de processamento utilizadas no `inteli.ipynb`.
- **intelidata.egg-info**: Informações sobre o pacote, geradas durante a construção.
- **requirements.txt**: Lista de dependências necessárias para executar o projeto.
- **send_pof_2017_2018.ipynb**: Jupyter Notebook onde os arquivos CSV, após o processamento, são encaminhados aos buckets da AWS S3.
- **setup.py**: Script de configuração para instalar o pacote.
- **tests**: Diretório contendo testes para o pacote.
  - **test_lib.py**: Arquivo de teste do módulo.
  
- **README.md**: Este arquivo, fornecendo informações sobre o pacote.
## 1.2 Executando o Pacote
Antes de executar os arquivos, certifique-se de ter instalado todas as dependências do projeto. 
Para isso, execute os seguintes comandos no seu terminal do VS Code, após abrir a pasta "Script_POF_S3"
```
cd pacotePython
pip install . 
```
### 1.2.1 Notebooks Jupyter
Para executar os processos principais do projeto, utilize os seguintes notebooks Jupyter:
- **inteli.ipynb**: Este notebook contém o fluxo principal de tratamento dos dados CSV. Basta abrir o notebook e executar suas células para processar e analisar os dados.
- **send_pof_2017_2018.ipynb**: Utilize este notebook para o envio dos dados processados para o Amazon S3. Abra o notebook e execute suas células para encaminhar os arquivos CSV aos buckets da AWS S3.
### 1.2.2 Testes
A pasta "tests" contém testes para garantir a integridade do pacote. Para executar os testes, recomenda-se o uso do Windows Subsystem for Linux (WLS) ou de um terminal Linux. Contudo, apesar disso, é possível prosseguir com os testes utilizando o sistema operacional Widnows também. Utilize o seguinte comando no terminal:
```bash
# navegue até a pasta teste
cd pacotePython
cd tests
pytest .\test_lib.py
```
## 1.3 Licença
Este pacote é distribuído sob a licença [Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
ã
# Documentação dos testes
### Teste: `test_encontrar_codigos_com_branco_funciona`
#### Objetivo:
Este teste tem como objetivo verificar se a função `encontrar_codigos_com_branco` da biblioteca `intelidata.lib` está retornando corretamente os códigos associados às linhas que contêm a palavra 'branco' em uma determinada coluna de um arquivo Excel.
#### Função Testada:
`intelidata.lib.encontrar_codigos_com_branco`
#### Cenário de Teste:
Um DataFrame de teste é criado com códigos de variáveis ('Código da variável') e uma coluna ('Coluna1') que contém a palavra 'branco teste'. A função é então chamada para encontrar os códigos associados à presença da palavra 'branco' na coluna especificada.
#### Critérios de Sucesso:
O teste é considerado bem-sucedido se a função retornar os códigos esperados.
### Teste: `test_encontrar_codigos_com_branco_nao_funciona`
#### Objetivo:
Este teste visa garantir que a função `encontrar_codigos_com_branco` lida adequadamente com a exceção `FileNotFoundError` quando é fornecido um arquivo inexistente como entrada.
#### Função Testada:
`intelidata.lib.encontrar_codigos_com_branco`
#### Cenário de Teste:
A função é chamada com o caminho de um arquivo inexistente.
#### Critérios de Sucesso:
O teste é considerado bem-sucedido se a função lançar a exceção `FileNotFoundError`.
### Teste: `test_preencher_valores_nulos_csv_funciona`
#### Objetivo:
O objetivo deste teste é verificar se a função `preencher_valores_nulos_csv` da biblioteca `intelidata.lib` preenche corretamente os valores nulos em um DataFrame, utilizando informações de um arquivo Excel.
#### Função Testada:
`intelidata.lib.preencher_valores_nulos_csv`
#### Cenário de Teste:
Um DataFrame de teste é criado com valores nulos em algumas colunas. A função é então chamada para preencher os valores nulos com base nos códigos encontrados em um arquivo Excel.
#### Critérios de Sucesso:
O teste é considerado bem-sucedido se os valores nulos forem preenchidos corretamente conforme esperado.
### Teste: `test_preencher_valores_nulos_csv_nao_funciona`
#### Objetivo:
Este teste visa garantir que a função `preencher_valores_nulos_csv` lida adequadamente com a exceção `FileNotFoundError` quando é fornecido um arquivo CSV inexistente como entrada.
#### Função Testada:
`intelidata.lib.preencher_valores_nulos_csv`
#### Cenário de Teste:
A função é chamada com caminhos de arquivo CSV e Excel inexistentes.
#### Critérios de Sucesso:
O teste é considerado bem-sucedido se a função lançar a exceção `FileNotFoundError`.
### Teste: `test_salvar_dataframes_como_csv_funciona`
#### Objetivo:
Este teste tem como objetivo verificar se a função `salvar_dataframes_como_csv` da biblioteca `intelidata.lib` salva corretamente os DataFrames em arquivos CSV.
#### Função Testada:
`intelidata.lib.salvar_dataframes_como_csv`
#### Cenário de Teste:
Dois DataFrames de teste são criados e salvos como arquivos CSV em um diretório temporário. A função é então chamada para salvar esses DataFrames em arquivos CSV em um diretório de destino.
#### Critérios de Sucesso:
O teste é considerado bem-sucedido se todos os arquivos CSV esperados forem criados no diretório de destino.
### Teste: `test_load_data_funciona`
#### Objetivo:
Este teste tem como objetivo verificar se a função `load_data` da biblioteca `intelidata.lib` carrega corretamente um arquivo CSV como um array NumPy.
#### Função Testada:
`intelidata.lib.load_data`
#### Cenário de Teste:
Um DataFrame de teste é criado e salvo como um arquivo CSV. A função é então chamada para carregar esse arquivo como um array NumPy.
#### Critérios de Sucesso:
O teste é considerado bem-sucedido se a função retornar um array NumPy.
### Teste: `test_load_data_nao_funciona`
#### Objetivo:
Este teste visa garantir que a função `load_data` lida adequadamente com a exceção `FileNotFoundError` quando é fornecido um arquivo CSV inexistente como entrada.
#### Função Testada:
`intelidata.lib.load_data`
#### Cenário de Teste:
A função é chamada com o caminho de um arquivo CSV inexistente.
#### Critérios de Sucesso:
O teste é considerado bem-sucedido se a função lançar a exceção `FileNotFoundError`.