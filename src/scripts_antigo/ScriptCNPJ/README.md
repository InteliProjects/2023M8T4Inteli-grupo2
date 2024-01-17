# 1. Package CNPJ e DATASUS

Este pacote é dedicado ao tratamento e envio para a AWS S3 de dados relacionados aos CNPJs e ao DATASUS, selecionados para atender às necessidades do projeto. Seu objetivo principal é facilitar o processamento e análise desses dados, garantindo uma integração suave com as ferramentas da AWS. As instruções abaixo guiarão você no uso adequado deste pacote, desde a execução dos notebooks Jupyter até a realização de testes do código.

## 1.1 Arquivos do pacote

Este é um breve guia sobre os arquivos contidos neste pacote Python.

- **.env.tmpl**: Arquivo de configuração de ambiente. Contém as keys da AWS Lab. 

- **.gitignore**: Arquivo de configuração do Git para ignorar o arquivo  ``.env.tmpl`` durante o versionamento.

- **.ipynb_checkpoints**: Diretório que armazena checkpoints automáticos de notebooks Jupyter.

- **.pytest_cache**: Diretório que armazena cache e dados temporários do Pytest.

- **build**: Diretório gerado durante o processo de construção do pacote. Contém arquivos intermediários.

- **arquivos_csv**: Diretório para armazenar arquivos CSV relacionados ao projeto.

- **inteli.ipynb**: Jupyter Notebook principal do projeto, que contém todo o processo de tratamento dos dados CSV.

- **intelidata**: Pacote Python principal.

  - **__init__.py**: Arquivo necessário para que o diretório seja tratado como um pacote Python.
  
  - **lib.py**: Módulo Python contendo funcionalidades específicas. Aqui são definidas todas as funções de processamento utilizadas no `inteli.ipynb`.

- **intelidata.egg-info**: Informações sobre o pacote, geradas durante a construção.

- **requirements.txt**: Lista de dependências necessárias para executar o projeto.

- **send_s3.ipynb**: Jupyter Notebook onde os arquivos CSV, após o processamento, são encaminhados aos buckets da AWS S3.

- **setup.py**: Script de configuração para instalar o pacote.

- **tests**: Diretório contendo testes para o pacote.

  - **test_lib.py**: Arquivo de teste do módulo.
  
- **README.md**: Este arquivo, fornecendo informações sobre o pacote.

## 1.2 Executando o Pacote

**Observação** : Antes de executar os arquivos, certifique-se de ter instalado todas as dependências do projeto. 

Para executar os processos principais do projeto, utilize os seguintes notebooks Jupyter:

- **inteli.ipynb**: Este notebook contém o fluxo principal de tratamento dos dados CSV. Basta abrir o notebook e executar suas células para processar e analisar os dados.

- **send_s3.ipynb**: Utilize este notebook para o envio dos dados processados para o Amazon S3. Abra o notebook e execute suas células para encaminhar os arquivos CSV aos buckets da AWS S3.

# 2. Testes Unitários

A seguir, estão documentados os testes unitários para as funções contidas no arquivo `test_lib.py`, na classe `TesteObterNomesArquivos`.

**Método setUp** : 
Este método é executado antes de cada teste. Ele cria um diretório temporário e um arquivo CSV populado dentro dele.

**Método tearDown** : 
Este método é executado após cada teste. Ele remove o diretório temporário criado durante o teste.

**Método criar_arquivo_csv_populado** : 
Este método cria um arquivo CSV populado com dados fictícios. O caminho do arquivo criado é retornado.

**Método teste_obter_nome_arquivo_funcionando** : Este teste verifica se a função inteli.obter_nomes_arquivos retorna resultados adequados para o diretório temporário criado. Imprime os resultados ou falha se houver problemas.

**Método teste_ler_arquivo_csv_funcionando** : 
Este teste verifica se a função `ler_arquivo_csv` pode ler corretamente o arquivo CSV criado durante a configuração. Falha se o DataFrame resultante estiver vazio.

**Método teste_tratar_e_salvar_arquivo** : 
Este teste verifica se a função `tratar_e_salvar_arquivo` pode processar e salvar corretamente o arquivo CSV criado durante a configuração. Imprime os resultados.

## 2.1 Execução dos Testes

A pasta "tests" contém testes para garantir a integridade do pacote. Para executar os testes, recomenda-se o uso do Windows Subsystem for Linux (WLS) ou de um terminal Linux. Utilize o seguinte comando no terminal:

```bash
pytest tests
```

# 3. Licença

Este pacote é distribuído sob a licença [Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
