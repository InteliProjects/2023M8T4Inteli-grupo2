## Sumário

[1. Identificação dos tipos de dados e suas características](#c1)

[2. Dados CSV](#c2)

[3. Dados CNPJ](#c3)

[4. API](#c4)

<br>

# <a name="c1"></a>1. Identificação dos tipos de dados e suas características

&emsp;&emsp; O cenário atual do mercado exige uma análise criteriosa e abrangente dos dados para embasar decisões estratégicas bem-informadas. Como parte do entregável da primeira *sprint* do módulo 8 (*Big Data*), que corresponde ao artefato “*Arquitetura de Ingestão de Dados do Parceiro*” o presente documento apresenta a identificação detalhada das bases de dados fornecidas pelo parceiro, explorando os diversos tipos de dados e suas características. 

# <a name="c2"></a>2. Dados CSV 

&emsp;&emsp; O conjunto de dados disponível na pasta “Dados CSV” que pode ser acessada através [deste link,](https://drive.google.com/drive/folders/1VZbDxxVORVeUfBRy7XIzdFIIwLoJmhp6) apresenta os microdados da Pesquisa de Orçamentos Familiares (POF) referentes aos anos de 2017 a 2018. Os arquivos de dados presentes nesta compilação são um reflexo das variáveis exploradas em diversas publicações divulgadas, proporcionando uma visão ampla e detalhada das dinâmicas socioeconômicas e de consumo. Estes dados abrangem uma variedade de temas, desde despesas e rendimentos familiares até indicadores de qualidade de vida no Brasil. Além disso, os microdados incluem informações demográficas e socioeconômicas, como número de cômodos, idade e educação dos moradores, bem como detalhes sobre a posse de bens duráveis e características do trabalho. Apresentaremos a seguir uma análise aprofundada destes microdados, elucidando sua relevância e características. 

## 2.1 Tipos de Dados e suas Características

1. **Informações Geográficas e Estratificação Social:** 
- `UF`: Identifica a unidade federativa, ajudando a localizar geograficamente os dados. 
- `ESTRATO\_POF`: Indica a estratificação social, o que pode ser crucial para entender diferentes comportamentos de consumo e necessidades. 
2. **Identificação e Situação Residencial:** 
- As colunas como `TIPO_SITUACAO_REG`, `COD_UPA`, `NUM_DOM`, e `NUM_UC` proporcionam uma visão detalhada da situação residencial e identificação dos domicílios, que podem ser essenciais para analisar o mercado de aluguel. 
3. **Dados Econômicos:** 
- Colunas como `V9001`, `V9002`, `V8000`, e `RENDA_TOTAL` fornecem informações sobre o poder aquisitivo e condições econômicas, que são fundamentais para entender a demanda e a capacidade de pagamento dos grupos pesquisados. 
1. **Fatores de Correção e Peso:** 
- `DEFLATOR`, `FATOR_ANUALIZACAO`, `PESO`, e `PESO_FINAL` ajudam na normalização ou ajuste dos dados para garantir precisão e relevância. 
5. **Tipo dos dados:** 

|**Nome da Coluna:** |**Tipo do Dado:** |
| - | - |
|UF   |int64   |
|ESTRATO_POF int64   |int64   |
|TIPO_SITUACAO_REG  |int64   |
|COD_UPA            |int64   |
|NUM_DOM             |int64   |
|NUM_UC             |int64   |
|QUADRO              |int64   |
|V9001              |int64   |
|V9002              |int64   |
|V8000              |float64 |
|V9010               |int64   |
|V9011               |int64   |
|DEFLATOR           |float64 |
|V8000_DEFLA        |float64 |
|COD_IMPUT_VALOR    |int64   |
|FATOR_ANUALIZACAO  |int64   |
|PESO               |float64 |
|PESO_FINAL         |float64 |
|RENDA_TOTAL        |float64 |

## 2.2 Importância para o Projeto

&emsp;&emsp; Esses dados podem proporcionar insights valiosos sobre variações regionais no comportamento do consumidor, o que é crucial para formular estratégias de _Go to Market_.  

# <a name="c3"></a> 3.Dados CNPJ

&emsp;&emsp; O conjunto de dados disponível na pasta “CNPJ” que pode ser acessada através [deste link.](https://drive.google.com/drive/folders/1b0KXB9m42_Ch3tO-nu6Z6XY_E9TvbQIJ) A base de dados do Cadastro Nacional de Pessoa Jurídica (CNPJ) é um recurso que fornece informações detalhadas sobre entidades empresariais no Brasil. As colunas desta base são estruturadas para oferecer insights sobre diferentes aspectos corporativos, como identificação, localização, atividade econômica e canais de contato. Ao explorar esses dados, visamos não apenas entender a estrutura e operações dessas entidades, mas também estabelecer uma fundação sólida para análises futuras que podem impulsionar decisões de negócios. 

## 3.1 Tipos de Dados e suas Características 

1. **Identificação da Empresa:** 
- `cnpj`: Número completo do CNPJ que identifica de maneira única cada empresa. 
- `cnpj_basico`: Parte básica do CNPJ. 
- `cnpj_ordem`: Número de ordem do CNPJ. 
- `cnpj_dv`: Dígito verificador do CNPJ. 
- `identificador_matriz_filial`: Indica se o CNPJ pertence a uma matriz ou filial. 
2. **Status Cadastral:** 
- `situacao_cadastral`: Status atual do cadastro da empresa. 
- `motivo_situacao_cadastral`: Motivo pelo qual a empresa se encontra na situação cadastral informada. 
3. **Informações de Atividade e Localização:** 
- `id_pais`: Identificação do país. 
- `cnae_fiscal_principal`: Classificação Nacional de Atividades Econômicas principal da empresa. 
- `id_municipio`: Identificação do município. 
- `id_municipio_rf`: Identificação do município na Receita Federal. 
4. **Contato:** 
- `ddd_1`, `ddd_2`: Códigos de área para telefonia. 
- `telefone_2`: Número de telefone secundário. 
- `ddd_fax`: Código de área para fax. 
5. **Número de linhas e colunas:** 

*O conjunto de dados é dividido em cinco bases distintas, cada uma com 33 colunas. Abaixo estão detalhadas as quantidades de linhas em cada base:* 

- *cnpj\_1: 409,357 linhas*  
- *cnpj\_2: 318,897 linhas*  
- *cnpj\_3: 44,974 linhas*  
- *cnpj\_4: 78,748 linhas*  
- *cnpj\_5: 64,565 linhas*  
- *Total acumulado entre as cinco bases: 916,541 linhas.*

6. **Tipo dos dados:** 

|**Nome da Coluna:** |**Tipo de Dado:** |
| - | - |
|data  |object |
|cnpj  |int64 |
|cnpj\_basico |int64 |
|cnpj\_ordem  |int64 |
|cnpj\_dv  |int64 |
|identificador\_matriz\_filial  |int64 |
|nome\_fantasia object situacao\_cadastral  |int64 |
|data\_situacao\_cadastral  |object |
|motivo\_situacao\_cadastral  |int64 |
|nome\_cidade\_exterior  |object |
|id\_pais  |float64 |
|data\_inicio\_atividade  |object |
|cnae\_fiscal\_principal  |int64 |
|cnae\_fiscal\_secundaria   |object |
|sigla\_uf |object |
|id\_municipio  |float64 |
|id\_municipio\_rf   |int64 |
|tipo\_logradouro  |object |
|logradouro  |object |
|numero  |object |
|complemento  |object |
|bairro  |object |
|cep |object |
|ddd\_1  |float64 |
|telefone\_1 |object |
|ddd\_2  |float64 |
|telefone\_2   |float64 |
|ddd\_fax |float64 |
|fax |object |
|email  |object |
|situacao\_especial |object |
|data\_situacao\_especial |object |
|dtype |object |

## 3.2 Importância para o Projeto:

&emsp;&emsp; Identificação precisa das empresas é fundamental para qualquer análise ou operação corporativa. Compreender o status cadastral e os motivos associados pode ser crucial para análises legais e de compliance. As colunas relacionadas à localização e atividade principal podem ajudar a entender o ambiente operacional e a natureza dos negócios. 

# <a name="c4"></a> 4. API

1. ***Endpoint*: [https://intelifunctiongetdata.azurewebsites.net/api/InteliFunctionGetData ](https://intelifunctiongetdata.azurewebsites.net/api/InteliFunctionGetData)**
- **Método Aceito:** *GET*  
- **Token de uso:** pZh3gmJW\_87epswrWDuB7CvQle- KqjsVh2ZJUaifiXd4AzFuOEy98w== 
2. **Parâmetros de Consulta** (*Query Parameters*):  
- **code:** Este é o *token* de autenticação necessário para fazer a requisição. É um tipo de dado *string*.  
- **table:** Este parâmetro informa à API para qual tabela da base de dados a chamada HTTP GET será feita. É um tipo de dado string e os valores possíveis são: "*Category", "Establishment*" e *"Sale*".  
- **saleDate** (opcional): Parâmetro de filtro por data de venda. É um tipo de dado string no formato *yyyy-mm-dd* (ex.: 2023-09-23).  
- **saleCnpj** (opcional): Parâmetro de filtro por CNPJ. É um tipo de dado *string* que deve ser um CNPJ válido.  
- **saleCategory** (opcional): Parâmetro de filtro por nome de categoria. É um tipo de dado *string* que deve ser um nome válido de categoria.  
3. **Resposta da API:** A resposta da API será em formato JSON. Cada entrada no JSON corresponderá a uma coluna na tabela de dados correspondente e o tipo de dado de cada entrada será determinado pelo tipo de dado da coluna na base de dados.  
3. **Tratamento de Exceções:** A API está preparada para lidar com quatro tipos de exceções relacionadas a parâmetros faltando ou inválidos, fornecendo mensagens de erro específicas para ajudar a diagnosticar e corrigir problemas com as requisições.  
3. **Exemplo de Código:** O exemplo de código fornecido mostra como fazer uma requisição GET para a API usando a biblioteca *requests* em Python, passando os parâmetros de consulta como um dicionário e tratando a resposta. 
