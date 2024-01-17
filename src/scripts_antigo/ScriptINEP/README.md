# 1. Package INEP

&emsp;&emsp; Este pacote é dedicado ao tratamento e envio para a AWS S3 de dados do INEP, selecionados para atender às necessidades do projeto. Seu objetivo principal é facilitar o processamento e análise desses dados, garantindo uma integração suave com as ferramentas da AWS. As instruções abaixo guiarão você no uso adequado deste pacote, desde a execução dos notebooks Jupyter até a realização de testes do código.

## 1.1 Arquivos do pacote

Este é um breve guia sobre os arquivos contidos neste pacote Python.

- **.env.tmpl**: Arquivo de configuração de ambiente. Contém as keys da AWS Lab. 

- **.gitignore**: Arquivo de configuração do Git para ignorar o arquivo  ``.env.tmpl`` durante o versionamento.

- **.ipynb_checkpoints**: Diretório que armazena checkpoints automáticos de notebooks Jupyter.

- **.pytest_cache**: Diretório que armazena cache e dados temporários do Pytest.

- **build**: Diretório gerado durante o processo de construção do pacote. Contém arquivos intermediários.

- **csv**: Diretório para armazenar arquivos CSV relacionados ao projeto.

- **inep.ipynb**: Jupyter Notebook principal do projeto, que contém todo o processo de tratamento dos dados CSV.

- **ana**: Pacote Python dos dados da ANA.

  - **__init__.py**: Arquivo necessário para que o diretório seja tratado como um pacote Python.
  
  - **lib.py**: Módulo Python contendo funcionalidades específicas. Aqui são definidas todas as funções de processamento utilizadas no `inep.ipynb`.
 
- **ed_superior**: Pacote Python dos dados da Educação Superior.

  - **__init__.py**: Arquivo necessário para que o diretório seja tratado como um pacote Python.
  
  - **lib.py**: Módulo Python contendo funcionalidades específicas. Aqui são definidas todas as funções de processamento utilizadas no `inep.ipynb`.
 
- **enceja**: Pacote Python dos dados do ENCEJA.

  - **__init__.py**: Arquivo necessário para que o diretório seja tratado como um pacote Python.
  
  - **lib.py**: Módulo Python contendo funcionalidades específicas. Aqui são definidas todas as funções de processamento utilizadas no `inep.ipynb`.

- **intelidata.egg-info**: Informações sobre o pacote, geradas durante a construção.

- **requirements.txt**: Lista de dependências necessárias para executar o projeto.

- **send_inep.ipynb**: Jupyter Notebook onde os arquivos CSV, após o processamento, são encaminhados aos buckets da AWS S3.

- **setup.py**: Script de configuração para instalar o pacote.

- **tests_ana**: Diretório contendo testes para o pacote ANA.

  - **test_lib.py**: Arquivo de teste do módulo.

- **tests_ed_sup**: Diretório contendo testes para o pacote Educação Superior.

  - **test_lib.py**: Arquivo de teste do módulo.
 
- **tests_enceja**: Diretório contendo testes para o pacote do ENCEJA.

  - **test_lib.py**: Arquivo de teste do módulo.
  
- **README.md**: Este arquivo, fornecendo informações sobre o pacote.

## 1.2 Executando o Pacote

**Observação** : Antes de executar os arquivos, certifique-se de ter instalado todas as dependências do projeto. 

Para executar os processos principais do projeto, utilize os seguintes notebooks Jupyter:

- **ine.ipynb**: Este notebook contém o fluxo principal de tratamento dos dados CSV. Basta abrir o notebook e executar suas células para processar e analisar os dados.

- **send_inep.ipynb**: Utilize este notebook para o envio dos dados processados para o Amazon S3. Abra o notebook e execute suas células para encaminhar os arquivos CSV aos buckets da AWS S3.

# 2. Testes Unitários 

A seguir, estão documentados os testes unitários para as funções contidas nos arquivos `test_lib.py`.

## 2.1 ANA, Educação Superior e ENCEJA

**Função 1:** ```test_clean_data_sucesso()```

&emsp;&emsp; Testa a funcionalidade de limpeza de dados da função clean_data do módulo. Verifica se todos os valores NaN foram removidos, utilizando assert para garantir que a soma total de valores NaN no DataFrame limpo seja zero. Se houver algum valor NaN restante, uma mensagem de erro é exibida.

**Função 2:** ```test_clean_data_falha()```

&emsp;&emsp; Testa a robustez da função clean_data ao lidar com entradas inválidas. Usa ```pytest.raises``` para verificar se um TypeError é levantado, o que é esperado quando um tipo de dado incompatível é passado para a função.

**Função 3:** ```test_ajustar_amazon_s3_sucesso()```

&emsp;&emsp; Testa a funcionalidade da função do módulo para situações de sucesso. Verifica se o retorno da função é o mesmo nome de arquivo passado e se ele foi criado no sistema de arquivos.

**Função 4:** ```test_ajustar_amazon_s3_falha()```

&emsp;&emsp; Testa a robustez da função ao lidar com parâmetros de entrada inválidos. Chama a função ajustar_amazon_s3 com um caminho de arquivo inválido. Usa pytest.raises para verificar se uma exceção é levantada, indicando o manejo apropriado de entradas inválidas.

## 2.4 Execução dos Testes

A pasta "tests" contém testes para garantir a integridade do pacote. Para executar os testes, recomenda-se o uso do Windows Subsystem for Linux (WLS) ou de um terminal Linux. Utilize o seguinte comando no terminal:

```bash
pytest tests
```

# 3. Licença

Este pacote é distribuído sob a licença [Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
