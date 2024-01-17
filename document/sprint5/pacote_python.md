## Sumário

[1. Introdução](#c1)

[2. CNPJ](#c2)

[3. DataSUS](#c3)

[4. IBGE](#c4) 

[5. POF](#c5)

<br>

# <a name="c1"></a>1. Introdução

O Batch e o processamento em streaming representam abordagens distintas para lidar com o processamento de dados. O Batch é projetado para executar trabalhos em lote escaláveis, agendando a execução de grandes volumes de dados de uma só vez. Ele gerencia automaticamente os recursos computacionais na nuvem. Por outro lado, o processamento em streaming envolve o processamento contínuo de dados à medida que são gerados, oferecendo baixa latência e capacidade de resposta em tempo real. Este documento explora a criação de um script Python dedicado ao tratamento de dados e ao subsequente envio para buckets da Amazon Web Services (AWS) usando o serviço de lote (Batch). 


# <a name="c2"></a>2. CNPJ

&emsp;&emsp; Entre os cinco arquivos específicos sobre CNPJ, é possível encontrar informações variadas, como dados cadastrais das empresas, histórico de alterações contratuais, situação cadastral, meio de contato. A combinação desses arquivos proporciona uma base sólida para a tomada de decisões estratégicas. A seguir, é apresentado as premissas e as restruções das funções utilizadas para tratar esses dados. Importante ressaltar que o código está presente neste repositório, na pasta ```src/scripts/ScriptCNPJ```.

## 2.1 Arquivo lib.py

&emsp;&emsp; A função ```carregar_dados_delimitador_correto``` tem como objetivo carregar um arquivo CSV, permitindo a especificação do delimitador utilizado. Essa função opera em chunks para otimizar a leitura de grandes conjuntos de dados, lidando adequadamente com erros de parsing. 

&emsp;&emsp; **Premissa:** existência de arquivo em formato CSV na pasta especificada no código, por exemplo: ```./csv/nome_arquivo.csv'```. 

&emsp;&emsp; Além disso, a função não apresenta nenhum tipo de restrição ou dependência por ser a primeira função a ser aplicada no arquivo. Abaixo, é possível visualizar como o arquivo pode ser aplicado. Este, utiliza o ponto e vírgula como delimitador, como segundo argumento da função. O DataFrame resultante é armazenado na variável df.

```
df = funcao.carregar_dados_delimitador_correto('./csv/nome_arquivo.csv', ';')
```

&emsp;&emsp; A função ```limpar_dados``` realiza a limpeza de dados em um DataFrame, removendo caracteres especiais de determinadas colunas. A limpeza também pode ser efetuada em _chunks_, neste caso, se no momento da aplicação não for especificado o tamanho do _chunks_, ele vai utilizar o "padrão" dito na função. Como premissa é necessário que o arquivo tenha sido carregado, ou seja, aplicado na função ```carregar_dados_delimitador_correto```, e a mesma variável definida anteriormente (```df```) seja aplicada na função. A segunda premissa é que as colunas devem ser passadas como _arrays_, já que neste caso é mais de uma. A única restrição dessa função é que deve ser uma variável a ser aplicada na função, e não um arquivo csv, por exemplo.

&emsp;&emsp; A aplicação da função ```limpar_dados``` é feita ao DataFrame df, removendo caracteres especiais e ignorando o _array_ passado em colunas_a_ignorar, que incluem 'email', 'data', 'data_situacao_cadastral', 'data_inicio_atividade' e 'data_situacao_especial'. Essas colunas foram ignoradas já que os caracteres especiais significam algo, como o '@' na coluna 'email'.

```
df = funcao.limpar_dados(df, colunas_a_ignorar=['email', 'data', 'data_situacao_cadastral', 'data_inicio_atividade', 'data_situacao_especial'])
```

&emsp;&emsp; A função ```tratar_valores_nulos``` aborda valores nulos em um DataFrame, substituindo-os por um valor especificado. O tratamento também pode ser efetuada em _chunks_, neste caso, se no momento da aplicação não for especificado o tamanho do _chunks_, ele vai utilizar o "padrão" dito na função. A premissa dessa função é utilizar o ```df``` criado na função anterior, além disso, é necessário definir um substituto para os valores nulos, neste exemplo: "nan". A única restrição dessa função é que deve ser uma variável a ser aplicada na função, e não um arquivo csv, por exemplo.

&emsp;&emsp; Aqui, a função ```tratar_valores_nulos``` é utilizada para substituir valores nulos no DataFrame (df) pelo valor especificado ('nan'). A operação é realizada em chunks de tamanho 100 para otimizar o tratamento em grandes conjuntos de dados.

```
df = funcao.tratar_valores_nulos(df, 'nan', chunk_size=1000)
```

&emsp;&emsp; A função ```remover_coluna``` remove uma coluna do DataFrame. A premissa dessa função é utilizar o ```df``` criado na função anterior, além disso, é necessário definir a coluna a ser removida, como mostra o exemplo. A única restrição dessa função é que deve ser uma variável a ser aplicada na função, e não um arquivo csv, por exemplo.

&emsp;&emsp; Abaixo, é empregado a função ```remover_coluna``` para excluir a coluna 'cnae_fiscal_secundaria' do DataFrame df. Essa coluna foi excluida pois não foi encontrada nenhuma utilidade no momento para ela. Note que a coluna deve ser passada em ''.

```
df = funcao.remover_coluna(df, 'cnae_fiscal_secundaria')
```

&emsp;&emsp; A função ```ajustar_amazon_s3``` é projetada para ajustar um DataFrame antes de carregá-lo no Amazon S3. A premissa desta função é receber como primeiro argumento a variável aplicada na função anterior e é necessário definir um caminho para que a função crie esse arquivo CSV, como mostra o código abaixo. Além disso, a restrição é que deve ser uma variável a ser aplicada na função, e não um arquivo csv, por exemplo.

&emsp;&emsp; A aplicação da função ```ajustar_amazon_s3``` é feita para criar um arquivo CSV na pasta ```./csv_s3/cnpj_5_s3.csv```.

```
funcao.ajustar_amazon_s3(df, './csv_s3/cnpj_5_s3.csv')
```

## 2.2 Aplicação do arquivo send_s3.ipynb

&emsp;&emsp; O script em Python apresentado tem como objetivo automatizar a transferência de arquivos CSV de um diretório local para o Amazon S3, seguido pela exclusão desses arquivos locais. Na primeira parte, são definidas variáveis que armazenam as credenciais de acesso à AWS, a região do Amazon S3, os diretórios locais dos arquivos CSV e o nome do bucket S3. Abaixo é demonstrado uma tabela que explica as variáveis do código abaixo.

| Nome da variável | Explicação | Premissa | Onde deve ser preenchido |
| ----------- | ----------- | ----------- | ----------- |
| aws_access_key_id | String alfanumérica única que identifica uma conta ou usuário AWS para propósitos de autenticação | Deve ter uma conta na AWS com as credenciais criadas ou acessar no AWSLabs | Arquivo ```.env.tmpl``` por questão de segurança |
| aws_secret_access_key | Chave secreta utilizada em conjunto com a anterior para assinar as solicitações | Deve ter uma conta na AWS com as credenciais criadas ou acessar no AWSLabs | Arquivo ```.env.tmpl``` por questão de segurança |
| aws_session_token | Componente das credenciais temporárias | Deve ter uma conta na AWSLabs | Arquivo ```.send_s3``` |
| region_name | Identifica a região da AWS onde você deseja que seus recursos e operações estejam localizados | Deve ser a mesma região do bucket | Arquivo ```.send_s3``` |
| bucket_name | Nome do Bucket que você deseja inserir na AWS | O Bucket deve estar criado na mesma conta das credenciais | Arquivo ```.send_s3``` |
| csv_directory_s3 | Diretório que se localiza os arquivos tratados | Os arquivos tratados devem estar neste diretório | Arquivo ```.send_s3``` |
| csv_directory | Diretório que se localiza os arquivos iniciais | Os arquivos devem estar neste diretório | Arquivo ```.send_s3``` |
| s3 | Criação de um cliente para o serviço Amazon S3 usando o Boto3 | Preenchimento de todas as variáveis acima | Arquivo ```.send_s3``` |

&emsp;&emsp; Por último, é definida uma função ```delete_csv_files``` para excluir todos os arquivos CSV de um diretório local. A função é então chamada para os diretórios csv_directory_s3 e csv_directory.

```
def delete_csv_files(directory):
    csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]
    for csv_file in csv_files:
        file_path = os.path.join(directory, csv_file)
        os.remove(file_path)
        print(f'O arquivo {csv_file} foi excluído de {directory}.')
```

# <a name="c3"></a>3. DataSUS

&emsp;&emsp; O DataSUS é o departamento de informática do Sistema Único de Saúde (SUS) no Brasil e é responsável por coletar, processar e disseminar informações sobre saúde no país. Entre as inúmeras bases de dados mantidas pelo DataSUS, duas categorias importantes para o projeto são: ocupação de leitos e os arquivos de leitos em si. Importante ressaltar que o código está presente neste repositório, na pasta ```src/scripts/ScriptDataSUS```.

## 3.1 Arquivo lib.py

&emsp;&emsp; A função ```carregar_csv``` carregar um arquivo CSV a partir de um caminho especificado. O parâmetro opcional delimiter permite a personalização do delimitador utilizado no arquivo CSV.

&emsp;&emsp; **Premissa:** existência de arquivo em formato CSV na pasta especificada no código, por exemplo: ```./csv/nome_arquivo.csv'```. 

&emsp;&emsp; Além disso, a função não apresenta nenhum tipo de restrição ou dependência por ser a primeira função a ser aplicada no arquivo. Abaixo, é possível visualizar como o arquivo pode ser aplicado. O DataFrame resultante é armazenado na variável df.

```
df = funcao.carregar_csv('./csv/nome_arquivo.csv') # Se o delimitador for ',' não precisa especificar na aplicação
```

&emsp;&emsp; A função acima é utilizada nos arquivos de 'Leito' e de 'Leito Ocupação', a única exceção é 'Leitos 2023' que precisa ser aplicado com a função abaixo. 

&emsp;&emsp; A função ```carregar_csv_com_codificacao``` carregar um arquivo CSV a partir de um caminho especificado, mas oferece suporte a diferentes codificações. Ela tenta carregar o arquivo usando várias codificações comuns até encontrar a que funciona. O parâmetro adicional chunk_size permite o carregamento em blocos, útil para arquivos muito grandes.

&emsp;&emsp; **Premissa:** existência de arquivo em formato CSV na pasta especificada no código, por exemplo: ```./csv/nome_arquivo.csv'```. 

&emsp;&emsp; Além disso, a função não apresenta nenhum tipo de restrição ou dependência por ser a primeira função a ser aplicada no arquivo. Abaixo, é possível visualizar como o arquivo pode ser aplicado. O DataFrame resultante é armazenado na variável df.

```
df = funcao.carregar_csv_com_codificacao('./csv/nome_arquivo.csv')
```

&emsp;&emsp; A função ```remover_coluna``` remove uma coluna do DataFrame.

&emsp;&emsp; **Premissa:** utilizar o ```df``` criado na função anterior, além disso, é necessário definir a coluna a ser removida, como mostra o exemplo. 

&emsp;&emsp; A única restrição dessa função é que deve ser uma variável a ser aplicada na função, e não um arquivo csv, por exemplo. Abaixo, é empregado a função ```remover_coluna``` para excluir a coluna 'cnae_fiscal_secundaria' do DataFrame df. Essa coluna foi excluida pois não foi encontrada nenhuma utilidade no momento para ela. Note que a coluna deve ser passada em ''.

```
df = funcao.remover_coluna(df, 'cnae_fiscal_secundaria')
```

&emsp;&emsp; A função ```limpar_dados``` realiza a limpeza de dados em um DataFrame, removendo caracteres especiais de determinadas colunas. A limpeza também pode ser efetuada em _chunks_, neste caso, se no momento da aplicação não for especificado o tamanho do _chunks_, ele vai utilizar o "padrão" dito na função. 

&emsp;&emsp; **Premissa:** é necessário que o arquivo tenha sido carregado, ou seja, aplicado na função ```carregar_dados_delimitador_correto```, e a mesma variável definida anteriormente (```df```) seja aplicada na função. A segunda premissa é que as colunas devem ser passadas como _arrays_, já que neste caso é mais de uma. 

&emsp;&emsp; A única restrição dessa função é que deve ser uma variável a ser aplicada na função, e não um arquivo csv, por exemplo. A aplicação da função ```limpar_dados``` é feita ao DataFrame df, removendo caracteres especiais e ignorando o _array_ passado em colunas_a_ignorar, que incluem 'email', 'data', 'data_situacao_cadastral', 'data_inicio_atividade' e 'data_situacao_especial'. Essas colunas foram ignoradas já que os caracteres especiais significam algo, como o '@' na coluna 'email'.

```
df = funcao.limpar_dados(df, colunas_a_ignorar=['dataNotificacao', '_created_at', '_updated_at', 'origem', '_id', '_p_usuario'])
```

&emsp;&emsp; A função ```tratar_valores_nulos``` aborda valores nulos em um DataFrame, substituindo-os por um valor especificado. O tratamento também pode ser efetuada em _chunks_, neste caso, se no momento da aplicação não for especificado o tamanho do _chunks_, ele vai utilizar o "padrão" dito na função. 

&emsp;&emsp; **Premissa:** utilizar o ```df``` criado na função anterior, além disso, é necessário definir um substituto para os valores nulos, neste exemplo: "nan". 

&emsp;&emsp; A única restrição dessa função é que deve ser uma variável a ser aplicada na função, e não um arquivo csv, por exemplo. Aqui, a função ```tratar_valores_nulos``` é utilizada para substituir valores nulos no DataFrame (df) pelo valor especificado ('nan'). A operação é realizada em chunks de tamanho 100 para otimizar o tratamento em grandes conjuntos de dados.

```
df = funcao.tratar_valores_nulos(df, 'nan', chunk_size=1000)  
```

&emsp;&emsp; Além disso, é aplicada uma função da biblioteca 'pandas' ```.split('')```. Nesta caso, a função substitui os valores na coluna por suas versões com a parte da hora removida, mantendo apenas a parte da data. 

&emsp;&emsp; **Premissa:** utilizar o ```df``` criado na função anterior, além disso, é necessário definir qual é o caractere que separa as duas informações. 

&emsp;&emsp; A única restrição dessa função é que deve ser uma variável a ser aplicada na função, e não um arquivo csv, por exemplo. Aqui, a função ```.split('')``` é utilizada na coluna de data.

```
df['dataNotificacao'] = df['dataNotificacao'].str.split('T').str[0]
```

&emsp;&emsp; A função ```ajustar_amazon_s3``` é projetada para ajustar um DataFrame antes de carregá-lo no Amazon S3. A premissa desta função é receber como primeiro argumento a variável aplicada na função anterior e é necessário definir um caminho para que a função crie esse arquivo CSV, como mostra o código abaixo. Além disso, a restrição é que deve ser uma variável a ser aplicada na função, e não um arquivo csv, por exemplo.

&emsp;&emsp; A aplicação da função ```ajustar_amazon_s3``` é feita para criar um arquivo CSV na pasta ```./csv_s3/cnpj_5_s3.csv```.

```
funcao.ajustar_amazon_s3(df, './csv_s3/cnpj_5_s3.csv')
```

## 3.2 Aplicação do arquivo send_s3.ipynb

&emsp;&emsp; O script em Python apresentado tem como objetivo automatizar a transferência de arquivos CSV de um diretório local para o Amazon S3, seguido pela exclusão desses arquivos locais. A explicação deste arquivo se deu no tópico 1.2 deste mesmo documento.

# <a name="c4"></a>4. IBGE

&emsp;&emsp; O Instituto Brasileiro de Geografia e Estatística (IBGE) é uma instituição responsável por coletar, analisar e divulgar informações estatísticas sobre o Brasil. No que diz respeito ao Produto Interno Bruto (PIB), o IBGE realiza pesquisas e censos econômicos que fornecem uma visão abrangente da atividade econômica do país. Além do PIB, o IBGE também é responsável por calcular o Índice de Gini, uma medida de desigualdade econômica que avalia a distribuição de renda em uma sociedade. O Índice de Gini varia de 0 a 1, sendo 0 representativo de uma distribuição totalmente igualitária, enquanto 1 indica extrema desigualdade. Importante ressaltar que o código está presente neste repositório, na pasta ```src/scripts/ScriptIBGE```.

## 4.1 Arquivo lib.py

&emsp;&emsp; A função ```load_data_with_correct_delimiter``` carregar um arquivo CSV a partir de um caminho especificado. OTenta inicialmente ler o arquivo usando o delimitador ';'. Se ocorrer um erro de análise, assume que o delimitador real é ',' e substitui todas as ocorrências de ';' por ',' no conteúdo do arquivo antes de tentar novamente a leitura.

&emsp;&emsp; **Premissa:** existência de arquivo em formato CSV na pasta especificada no código, por exemplo: ```./csv/nome_arquivo.csv'```. 

&emsp;&emsp; Além disso, a função não apresenta nenhum tipo de restrição ou dependência por ser a primeira função a ser aplicada no arquivo. Abaixo, é possível visualizar como o arquivo pode ser aplicado. O DataFrame resultante é armazenado na variável df.

```
df = funcao.load_data_with_correct_delimiter("./csv/nome_arquivo.csv")
```

&emsp;&emsp; A função ```clean_data``` recebe um DataFrame como entrada e retorna um novo 'df' após a remoção de linhas que contêm valores nulos. Esta funcão é utilizada somente porque o modelo do arquivo do IBGE contém uma fonte no final do arquivo, e devemos excluir essa parte. 

&emsp;&emsp; **Premissa:** utilizar o ```df``` criado na função anterior.

&emsp;&emsp; A única restrição dessa função é que deve ser uma variável a ser aplicada na função, e não um arquivo csv, por exemplo. Abaixo, é empregado a função ```clean_data``` para excluir os valores nulos encontrados.

```
df = funcao.clean_data(df)
```

&emsp;&emsp; A função ```ajustar_amazon_s3``` é projetada para ajustar um DataFrame antes de carregá-lo no Amazon S3. A premissa desta função é receber como primeiro argumento a variável aplicada na função anterior e é necessário definir um caminho para que a função crie esse arquivo CSV, como mostra o código abaixo. Além disso, a restrição é que deve ser uma variável a ser aplicada na função, e não um arquivo csv, por exemplo.

&emsp;&emsp; A aplicação da função ```ajustar_amazon_s3``` é feita para criar um arquivo CSV na pasta ```./csv_s3/cnpj_5_s3.csv```.

```
funcao.ajustar_amazon_s3(df, './csv_s3/cnpj_5_s3.csv')
```

## 4.2 Aplicação do arquivo send_s3.ipynb

&emsp;&emsp; O script em Python apresentado tem como objetivo automatizar a transferência de arquivos CSV de um diretório local para o Amazon S3, seguido pela exclusão desses arquivos locais. A explicação deste arquivo se deu no tópico 1.2 deste mesmo documento.

# <a name="c5"></a>5. POF

&emsp;&emsp; A Pesquisa de Orçamentos Familiares (POF), conduzida pelo Instituto Brasileiro de Geografia e Estatística (IBGE), é uma iniciativa fundamental para compreender os padrões de consumo e a estrutura orçamentária das famílias brasileiras. Realizada periodicamente, a POF coleta dados detalhados sobre os gastos das famílias em diversos itens, como alimentação, habitação, transporte, saúde e educação Importante ressaltar que o código está presente neste repositório, na pasta ```src/scripts/ScriptPOF```.

## 5.1 Arquivo lib.py

&emsp;&emsp; A função ```load_data_with_correct_delimiter``` renomea a colunas em um DataFrame, utilizando um arquivo de mapeamento. O DataFrame é carregado a partir de um arquivo CSV, juntamente com um segundo DataFrame que contém um mapeamento entre os códigos das variáveis e suas traduções correspondentes.

&emsp;&emsp; **Premissa:** existência dos arquivos em formato CSV e devem ser correspondidos em variáveis chamadas na função.

&emsp;&emsp; Além disso, a função não apresenta nenhum tipo de restrição ou dependência por ser a primeira função a ser aplicada no arquivo. Abaixo, é possível visualizar como o arquivo pode ser aplicado. O DataFrame resultante é armazenado na variável df.

```
arquivo_csv = './csv/nome_arquivo.csv' # Arquivo da POF
arquivo_excel = './tradutores/Dicionários de váriaveis.xlsx' # Dicionário das variáveis - utilizado depois
arquivo_mapeamento = './tradutores/traducao_domicilio.csv' # Dicionário das colunas
column_name = 'Categorias' # Utilizado depois

df_traduzido = funcao.traduzir_nomes_colunas(arquivo_csv, arquivo_mapeamento)
```

&emsp;&emsp; A função ```encontrar_codigos_com_branco``` recebe um DataFrame como entrada e retorna um novo 'df' após o encontro dos valores nulos, e com esse valores nulos ele substitui para os valores especificados no Dicionário (arquivo_excel).

&emsp;&emsp; **Premissa:** utilizar o ```df``` criado na função anterior.

&emsp;&emsp; A única restrição dessa função é que deve ser uma variável a ser aplicada na função, e não um arquivo csv, por exemplo. Abaixo, é empregado a função ```encontrar_codigos_com_branco``` para excluir os valores nulos encontrados.

```
df = funcao.preencher_valores_nulos_csv(df, arquivo_excel, column_name)
```

&emsp;&emsp; A função ```encontrar_codigos_com_branco``` aborda valores nulos em um DataFrame, substituindo-os por um valor especificado.

&emsp;&emsp; **Premissa:** utilizar o ```df``` criado na função anterior, além disso, é necessário definir um substituto para os valores nulos, neste exemplo: "N/A". 

&emsp;&emsp; A única restrição dessa função é que deve ser uma variável a ser aplicada na função, e não um arquivo csv, por exemplo. Aqui, a função ```tratar_valores_nulos``` é utilizada para substituir valores nulos no DataFrame (df) pelo valor especificado ('N/A'). 

```
df_nulos = funcao.tratar_valores_nulos(df_com_nulos_preenchidos, 'N/A')
```

&emsp;&emsp; A função ```translate_numeric_values_in_df_uf``` traduz os valores numéricos em uma coluna específica de um DataFrame, utilizando um arquivo CSV de mapeamento para os estados brasileiros. Ao mapear os códigos numéricos para os estados correspondentes, ela cria uma nova coluna no DataFrame original com os valores traduzidos, facilitando a interpretação dos dados.

&emsp;&emsp; **Premissa:** utilizar o ```df``` criado na função anterior, além disso, é necessário especificar o caminho do arquivo com a tradução. Essa função deve ser aplicada em todos os arquivos da POF. 

&emsp;&emsp; A única restrição dessa função é que deve ser uma variável a ser aplicada na função, e não um arquivo csv, por exemplo. Aqui, a função ```translate_numeric_values_in_df_uf``` é utilizada para traduzir os estados brasileiros. 

```
df = funcao.translate_numeric_values_in_df(df, './tradutores/traducao_uf.csv', 'unidade_federativa')
```

&emsp;&emsp; A função ```translate_numeric_values_in_df_alimento``` traduz os valores numéricos em uma coluna específica de um DataFrame, utilizando um arquivo CSV de mapeamento para os códigos dos alimentos. Ao mapear os códigos numéricos para os alimentos correspondentes, ela cria uma nova coluna no DataFrame original com os valores traduzidos, facilitando a interpretação dos dados.

&emsp;&emsp; **Premissa:** utilizar o ```df``` criado na função anterior, além disso, é necessário especificar o caminho do arquivo com a tradução. Essa função deve ser aplicada **somente** no arquivo de _consumo_alimentar_.

&emsp;&emsp; A única restrição dessa função é que deve ser uma variável a ser aplicada na função, e não um arquivo csv, por exemplo. Aqui, a função ```translate_numeric_values_in_df_alimento``` é utilizada para traduzir os estados brasileiros. 

```
df = funcao.translate_numeric_values_in_df_alimento(df, './tradutores/Produtos do Consumo Alimentar.csv', 'codigo_tipo_alimento')
```

&emsp;&emsp; A função ```ajustar_amazon_s3``` é projetada para ajustar um DataFrame antes de carregá-lo no Amazon S3. A premissa desta função é receber como primeiro argumento a variável aplicada na função anterior e é necessário definir um caminho para que a função crie esse arquivo CSV, como mostra o código abaixo. Além disso, a restrição é que deve ser uma variável a ser aplicada na função, e não um arquivo csv, por exemplo.

&emsp;&emsp; A aplicação da função ```ajustar_amazon_s3``` é feita para criar um arquivo CSV na pasta ```./csv_s3/cnpj_5_s3.csv```.

```
funcao.ajustar_amazon_s3(df, './csv_s3/cnpj_5_s3.csv')
```

## 5.2 Aplicação do arquivo send_s3.ipynb

&emsp;&emsp; O script em Python apresentado tem como objetivo automatizar a transferência de arquivos CSV de um diretório local para o Amazon S3, seguido pela exclusão desses arquivos locais. A explicação deste arquivo se deu no tópico 1.2 deste mesmo documento.


# Observação:

Se não houver localizado informações pertinentes no presente documento, por favor, consulte o link a seguir, que direciona à documentação oficial.

<a href="https://docs.google.com/document/d/18IWwAVmbsr7sUm45ySdnJtWkj1H6QQnC/edit?usp=sharing&ouid=112389543027386593098&rtpof=true&sd=true">Documentação Oficial</a>

