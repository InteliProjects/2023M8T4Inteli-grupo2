# Requisição para a API do parceiro
## Introdução

Este script Python tem como objetivo facilitar o processo de obtenção, processamento e armazenamento de dados provenientes de uma API externa no serviço de armazenamento em nuvem Amazon S3. O código é modular e composto por funções que realizam tarefas específicas.

## Funcionalidades Principais

### 1. Obtenção de Dados da API

A função `get_data` realiza uma requisição HTTP a uma API específica, fornecendo um código de autenticação, o nome da tabela desejada e uma data como parâmetros. Em caso de sucesso (código de status 200), os dados são retornados no formato JSON. Caso contrário, é exibida uma mensagem de falha.

### 2. Salvamento de Dados em um Arquivo CSV
A função `save_to_csv` recebe os dados obtidos pela função anterior e os salva em um arquivo CSV local. O nome do arquivo é fornecido como parâmetro. Caso não haja dados, a função não realiza nenhuma operação.

### 3. Envio do Arquivo para o Amazon S3
A função `upload_to_aws` utiliza a biblioteca boto3 para interagir com o serviço Amazon S3. O script tenta fazer o upload do arquivo local para um bucket específico no S3. Em caso de sucesso, exibe uma mensagem indicando o êxito. Em caso de falha, exibe uma mensagem de erro.
### 4. Salvamento Principal
A função `process_and_save` é a função principal do script. Ela chama as funções anteriores em sequência: obtém dados da API, salva localmente em um arquivo CSV e, em seguida, envia esse arquivo para o Amazon S3.
### 5. Função main
A função `main` é a função de execução principal. Ela obtém a data de venda do dia anterior, define as categorias desejadas (['category', 'establishment', 'sale']) e o nome do bucket S3. Em seguida, itera sobre as categorias, processa e salva os dados para cada uma.
## 6. Observações Importantes:
- Certifique-se de substituir os marcadores de posição ('SEU_API_CODE', 'SEU_ACCESS_KEY', 'SEU_SECRET_KEY', 'SEU_SESSION_TOKEN' e 'SUA_REGION') pelas suas credenciais reais antes de executar o código.

Para mais detalhes sobre a execução e configuração, consulte o código fonte.