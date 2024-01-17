## Sumário

[1. Introdução ](#c1)

[2. Data Lake](#c2)

[3. OLAP (Online Analytical Processing)](#c3) 

[4. Amazon Redshift e Escalabilidade dos Dados ](#c4)

[5. Data Warehouse](#c5)

[6. Views](#c6)

[7. Referências](#c7)

<br>

# <a name="c1"></a>1. Introdução

&emsp;&emsp; Este documento explora conceitos-chave e práticas emergentes no armazenamento e análise de dados, com foco em **Data Lakes**, **OLAP** e **Data Warehouses**. Inicialmente, discutimos o *Data Lake*, exemplificado pelo uso do **Amazon S3**, destacando sua flexibilidade e escalabilidade no armazenamento de dados variados. Em seguida, exploramos no **OLAP** e na implementação do **Amazon Redshift**, ressaltando sua importância em análises multidimensionais. Também comparamos o Redshift com outras soluções de mercado, como **Google BigQuery**, **Snowflake** e **Azure Synapse Analytics**, fornecendo uma visão comparativa. O papel dos **Data Warehouses** na consolidação e análise de dados é então abordado, seguido por uma discussão sobre a estruturação de dados e a criação de visualizações para análises eficientes. Este documento visa oferecer um entendimento abrangente das tecnologias de dados modernas e suas aplicações práticas no cenário empresarial.


# <a name="c2"></a>2. Data Lake

&emsp;&emsp; "Data Lake" é um conceito que se refere a um repositório de dados que pode armazenar uma grande quantidade de dados brutos, estruturados e não estruturados, em sua forma nativa, até que sejam necessários para análise. É uma abordagem que permite armazenar dados em sua forma bruta, sem a necessidade de estruturá-los previamente, oferecendo flexibilidade na análise posterior.

**Importância do Data Lake:**

- **Armazenamento Versátil:** Data Lakes, como o S3 da AWS, oferecem um local para armazenar dados em diversos formatos, como texto, imagens, vídeos e outros, sem a necessidade imediata de organização. Isso permite que as organizações armazenem uma grande variedade de dados de maneira econômica.
- **Análise Pós-Fato:** Ao armazenar dados brutos, as organizações podem realizar análises mais profundas e avançadas quando surgem novas questões ou métodos analíticos. Isso contrasta com abordagens mais tradicionais que requerem estruturação antecipada dos dados.
- **Integração com Ferramentas de Big Data:** Data Lakes são frequentemente integrados a ecossistemas de Big Data, permitindo o processamento eficiente de grandes volumes de dados usando ferramentas como Apache Spark ou Apache Hive.

## 2.1. Aplicação data lake no projeto

&emsp;&emsp; No contexto do projeto, a opção por utilizar o Amazon S3 (Amazon Simple Storage Service) como Data Lake reflete uma estratégia que se fundamenta na capacidade escalável de armazenamento, sendo ele um serviço de armazenamento na nuvem escalável, projetado para armazenar e recuperar qualquer quantidade de dados a qualquer momento. Essa abordagem permite armazenar dados em sua forma bruta, sem a necessidade imediata de estruturação, alinhando-se aos princípios de flexibilidade e eficiência característicos da computação em nuvem.

&emsp;&emsp; Essa escolha proporciona a flexibilidade necessária para futuras análises, permitindo uma integração com outras ferramentas e serviços dentro do ecossistema da AWS. Dessa maneira, ao utilizar o S3 como Data Lake, não apenas atende às necessidades imediatas de armazenamento, mas também estabelece uma base sólida para a exploração e extração de insights a partir dos dados armazenados.

## 2.2. Quantidade de dados armazenados

&emsp;&emsp; A gestão dos dados é um aspecto crucial para análises. A quantificação precisa da quantidade de dados armazenados no S3 oferece insights valiosos sobre o escopo e a complexidade do repositório. Abaixo, detalhamos a distribuição por buckets, a quantidade de arquivos e a totalidade em gigabytes.

**Quantidade de Buckets:** 8

- cnpj-datadream
- dadosinep-datadream
- dadosmec-datadream
- datasus-datadream
- ibge-datadream
- pofmain-datadream
- receita-datadream
- zipcode-datadream
  
**Quantidade de arquivos por buckets:** 80

- cnpj-datadream: 5 arquivos
- dadosinep-datadream: 3 arquivos
- dadosmec-datadream: 8 arquivos
- datasus-datadream: 41 arquivos
- ibge-datadream: 3 arquivos
- pofmain-datadream: 16 arquivos
- receita-datadream: 3 arquivos
- zipcode-datadream: 1 arquivo

**Quantidade Total de Gigabytes:** 51,3 GB

- cnpj-datadream : 4,55GB
- dadosinep-datadream : 1,04GB
- dadosmec-datadream : 7,28GB
- datasus-datadream : 14,5GB
- ibge-datadream : 0,99MB 
- pofmain-datadream : 900MB
- receita-datadream : 18,27MB
- zipcode-datadream : 409.2 kb


# <a name="c3"></a>3. OLAP (Online Analytical Processing)

&emsp;&emsp; OLAP é uma categoria de software que permite aos usuários analisar dados multidimensionais de forma rápida e eficiente. Ele é projetado para consultas e análises complexas, fornecendo uma visão multidimensional dos dados. Alguns conceitos-chave associados ao OLAP:

&emsp;&emsp;**Cubo OLAP:** Os dados em um ambiente OLAP são organizados em cubos. Cada cubo contém métricas ou medidas que podem ser analisadas, bem como dimensões que representam as várias maneiras de visualizar os dados.

&emsp;&emsp;**Dimensões:** São as categorias pelas quais os dados podem ser analisados. Por exemplo, em um cubo de vendas, as dimensões podem incluir tempo, localização geográfica, produtos e clientes.

&emsp;&emsp;**Medidas:** São os dados numéricos que podem ser analisados. No contexto de vendas, as medidas podem incluir receita, quantidade vendida e lucro.

## 3.1. OLAP na AWS

&emsp;&emsp;Na AWS, a implementação da solução OLAP foi realizadas usando o serviço Amazon Redshift. Ele oferece suporte ao processamento OLAP por meio de consultas SQL e pode integrar-se a ferramentas de visualização de dados.

## 3.2. Benefícios da Utilização de OLAP na AWS

&emsp;&emsp;**Desempenho Rápido:** O processamento OLAP na AWS, especialmente com serviços como o Amazon Redshift, oferece desempenho rápido para consultas analíticas complexas em grandes volumes de dados.

&emsp;&emsp;**Elasticidade:** Os serviços da AWS são altamente escaláveis, permitindo ajustes nos recursos conforme necessário para lidar com cargas de trabalho variáveis.

&emsp;&emsp;**Integração com Ferramentas de Visualização:** É fácil integrar soluções OLAP na AWS com ferramentas de visualização de dados populares, como Tableau, Power BI e outras, para criar relatórios e painéis interativos.


# <a name="c4"></a>4. Amazon Redshift e Escalabilidade dos Dados

&emsp;&emsp;O Amazon Redshift é um serviço de data warehouse, ou seja, ele consolida e armazena um grande volume de dados de diferentes fontes em um único local centralizado. Esse serviço fornece uma solução de armazenamento de dados na nuvem (o que contribui para esse acesso e reunião dos dados), ele é projetado para possuir escalabilidade ( é uma solução escalável e dimensionável, sendo possível começar com um cluster menor e aumentar o tamanho conforme as necessidades crescem), segurança (a AWS oferece recursos de segurança, backup e recuperação em todo ambiente fornecido pelo Redshift) e desempenho. Com todos esses atributos, a solução permite que as organizações armazenem e consultem grandes volumes de dados de maneira eficiente, o que facilita análises e relatórios em ambientes empresariais (Business Intelligence (BI)). Para o contexto do atual projeto, o Redshift facilitará a criação do ambiente OLAP (Online Analytical Processing) a partir do seguintes recursos: 

&emsp;&emsp;**SQL Aplicado:** É possível usar a linguagem SQL (Structured Query Language) no Redshift para a manipulação e consulta de bancos de dados relacionais, o que permite escrever consultas analíticas complexas.

&emsp;&emsp;A medida que as necessidades de armazenamento e processamento de dados de uma organização aumentam, é possível expandir o cluster do Redshift para lidar com essas novas demandas. Essa capacidade de escala permite que as empresas ajustem seus recursos de acordo com o volume de dados e as complexidades das consultas.

&emsp;&emsp;**Ferramentas BI:** As ferramentas de BI (como Tableau, Power BI e Looke) podem se conectar diretamente ao Redshift, permitindo aos usuários criar relatórios interativos, painéis de controle e visualização de dados sem a necessidade de manipular diretamente consultas complexas no SQL. Essa integração facilita a exploração e a interpretação dos dados para a tomada de decisão.

&emsp;&emsp;O armazenamento colunar é uma abordagem em que os dados são organizados e armazenados por coluna em vez de por linha. Isso significa que os valores de uma coluna são armazenados juntos, o que proporciona eficiência significativa em consultas analíticas, afinal, elas envolvem a recuperação de um conjunto limitado de colunas em vez de todas as colunas de uma tabela, assim, o armazenamento colunar reduz o tempo necessário para acessar e processar os dados relevantes.

&emsp;&emsp;**Paralelismo Massivo:** o Redshift possui a capacidade de distribuir uma única consulta entre vários nós de computação, fazendo com que cada um processe parte dos dados, permitindo que a consulta seja executada em paralelo. A vantagem dessa característica fica muito aparente em consultas complexas que envolvem grandes volumes de dados, pois o processamento simultâneo em várias máquinas acelera significativamente o tempo de resposta. 


## 4.1. Possibilidades Além do Amazon Redshift 

&emsp;&emsp;No dinâmico universo da computação em nuvem, a análise de dados é fundamental, e o Amazon Redshift, da AWS, destaca-se. Contudo, o leque de opções vai além. Apresenta-se alternativas ao Redshift, destacando três soluções competitivas. Ao examinar essas opções, as organizações podem encontrar alternativas que atendam melhor às suas necessidades específicas de análise de dados, proporcionando flexibilidade na otimização das operações em nuvem.

### 4.1.1. Google BigQuery

&emsp;&emsp;Desenvolvido pela Google, o **Google BigQuery**, é um serviço de data warehouse baseado em nuvem que oferece escalabilidade automática e consultas SQL rápidas para análises de dados em larga escala.

Vantagens em Relação ao AWS Redshift:

- Escalabilidade automática, permitindo consultas rápidas em grandes conjuntos de dados, sem a necessidade de gerenciar a infraestrutura.
- A integração eficiente com outros serviços da Google Cloud.
- Melhor  modelo de precificação (pay-as-you-go) do BigQuery, simplificando a previsão de custos.

Desvantagens em Relação ao Amazon Redshift:

- Maior custo para Grandes Volumes de Dados.
- Dependência de Conectividade com a Internet.
- Menos Adequado para Cargas de Trabalho Transacionais (não é a melhor escolha para transações ou atualizações frequentes).

### 4.1.2. Snowflake

&emsp;&emsp;O **Snowflake**, desenvolvido pela Snowflake Computing, é um serviço de data warehouse na nuvem conhecido por sua arquitetura multi-cluster única.

Vantagens em Relação ao AWS Redshift:

- Arquitetura multi-cluster que permite escalabilidade horizontal automática, otimizando o desempenho conforme a demanda.
- Dimensionamento de recursos de forma independente, otimizando custos conforme as necessidades específicas de armazenamento e processamento.
- Suporte à SQL padrão ANSI, facilitando a migração de bancos de dados existentes e uma experiência ainda mais familiar para os usuários.

Desvantagens em Relação ao Amazon Redshift:

- Modelagem de Custos Complexa.
- Menos integrações diretas com algumas ferramentas de BI e ecossistemas de nuvem.
- Curva de aprendizado maior para compreender completamente sua arquitetura única e aproveitar ao máximo seus recursos.

### 4.1.3. Azure Synapse Analytics

&emsp;&emsp;O Azure Synapse Analytics também é um data warehouse que oferece recursos para consultas analíticas rápidas em grandes conjuntos de dados, além de ser escalável e projetado para lidar com cargas de trabalho analíticas complexas.

Vantagens em Relação ao AWS Redshift:

- **Integração com Ecossistema Azure:** O Azure Synapse Analytics tem uma integração profunda com o ecossistema Azure, permitindo uma colaboração eficiente com outros serviços e ferramentas da plataforma. Isso pode facilitar a criação de soluções end-to-end e a implementação de arquiteturas de dados mais abrangentes.
- **Flexibilidade na Escala:** O Azure Synapse Analytics oferece uma flexibilidade significativa na escala, permitindo que você dimensione recursos de armazenamento e computação conforme necessário. Isso possibilita ajustar a capacidade de acordo com as demandas específicas do seu projeto, otimizando custos e desempenho.
- **Análise em Tempo Real:** A capacidade de realizar análises em tempo real é uma vantagem do Azure Synapse Analytics. Ele permite a ingestão e a análise de dados em tempo real, fornecendo insights mais recentes e suportando casos de uso que exigem tomada de decisões em tempo hábil.

Desvantagens em Relação ao Amazon Redshift:

- **Custo:** Em comparação com outras soluções, como o Amazon Redshift, o Azure Synapse Analytics pode ter custos mais elevados em algumas situações. O modelo de preços pode ser complexo, e os usuários precisam entender completamente como os recursos são alocados e utilizados para otimizar os custos.
- **Curva de Aprendizado:** A curva de aprendizado para usar efetivamente o Azure Synapse Analytics pode ser íngreme para usuários inexperientes. Isso se deve à sua gama de recursos e à necessidade de compreender a integração com outros serviços Azure, o que pode demandar tempo e esforço.
- **Maturidade do Serviço:** Dependendo dos requisitos específicos do seu projeto, a maturidade do Azure Synapse Analytics em comparação com soluções mais consolidadas, como o Amazon Redshift, pode ser uma consideração. A estabilidade e a maturidade da plataforma podem variar de acordo com as necessidades individuais e a evolução do serviço ao longo do tempo.

## 4.2 Criação Redshift AWS

&emsp;&emsp;Criar um cluster Amazon Redshift na AWS Lab envolve vários passos. Abaixo está um guia passo a passo que você pode seguir. Certifique-se de ter permissões adequadas para criar recursos no AWS Lab.

**Passo 1:** Acesse o Console da AWS Lab e faça login na sua conta.



**Passo 2:** No Console da AWS, pesquise em serviços por "Amazon Redshift". No menu lateral, selecione a opção "Painel de clusters provisionados".

<img src="./../../assets/passo%200.png"> Figura 01: Console da AWS Fonte: Autoria Própria

**Passo 3:** Clique no botão "Create cluster" (Criar cluster).

<img src="./../../assets/passo%201.png"> Figura 02: Console da AWS Fonte: Autoria Própria

**Passo 4:** Configuração do Cluster

- Cluster identifier: Insira um nome único para o seu cluster.
- Node type: Escolha o tipo de nó para o seu cluster.
- Number of nodes: Configure o número de nós no seu cluster.

<img src="./../../assets/passo%202.png"> Figura 03: Console da AWS Fonte: Autoria Própria

- Database name: Escolha um nome para o seu banco de dados.
- Master username e Master password: Defina um nome de usuário e uma senha para o usuário mestre.

<img src="./../../assets/passo%203.png"> Figura 04: Console da AWS Fonte: Autoria Própria

**Passo 5:** Criação IAM 

- No Console da AWS, vá para a seção "Services" (Serviços).
- Selecione "IAM" sob a categoria "Security, Identity, & Compliance".
- No painel de navegação à esquerda, escolha "Roles" e clique em "Create role" (Criar função).
- Selecione "AWS service" como o tipo de entidade de confiança e escolha "Redshift" como o serviço que será confiável.

Observação: No processo de criação da função, escolha as políticas do IAM que concederão as permissões necessárias ao Redshift. Isso pode incluir políticas como "AmazonRedshiftFullAccess" ou políticas personalizadas que você configurou.

**Passo 5.1:** Adicione a Função ao Cluster Redshift

- Volte ao Console do Amazon Redshift.
- Selecione o cluster que você criou anteriormente.
- Função do IAM Associados
- Clique em "Add IAM role" (Adicionar função IAM) e selecione a função IAM que você criou.

<img src="./../../assets/passo%204.png"> Figura 05: Função ao Cluster Redshift Fonte: Autoria Própria


**Passo 6:** Configurações Avançadas (Opcional)

- Virtual Private Cloud (VPC): Escolha a VPC na qual o cluster será lançado.
- Publicly accessible: Decida se o cluster será acessível publicamente ou apenas internamente.
- VPC security groups: Configure os grupos de segurança VPC para controlar o tráfego de rede para o cluster.
- Automated snapshots: Escolha se deseja habilitar snapshots automáticos.
- Snapshot retention period: Configure o período de retenção para os snapshots automáticos.

Observação: Revise as configurações do seu cluster. Clique em "Create cluster" para iniciar a criação do cluster.

<img src="./../../assets/passo%205.png"> Figura 06: Configurações do cluster Fonte: Autoria Própria

**Passo 7:** Aguarde a Criação

Aguarde enquanto o cluster é criado. Isso pode levar alguns minutos.

<img src="./../../assets/passo%206.png"> Figura 07: Configurações do cluster Fonte: Autoria Própria

**Passo 8:** Acesse o Cluster
Após a conclusão, vá para a lista de clusters no Console do Redshift.

<img src="./../../assets/passo%207.png"> Figura 08: Lista de clusters no Console do Redshift


# <a name="c5"></a>5. Data Warehouse

&emsp;&emsp;Um Data Warehouse é um sistema de gerenciamento de banco de dados projetado para armazenar e analisar grandes volumes de dados, provenientes de várias fontes dentro de uma organização. Ele é otimizado para consulta e análise de dados, oferecendo uma visão integrada e consolidada para facilitar a tomada de decisões.

## 5.1. Importância do Data Warehouse:

&emsp;&emsp;**Consolidação de Dados:** O Data Warehouse permite a integração de dados de diferentes fontes, proporcionando uma visão unificada e consistente das informações. Isso facilita a análise e gera insights mais precisos.

&emsp;&emsp;**Análise de Dados Históricos:** Ao armazenar grandes volumes de dados ao longo do tempo, o Data Warehouse possibilita a análise de tendências e padrões históricos, contribuindo para uma compreensão sobre o desempenho da organização.

&emsp;&emsp;**Suporte à Tomada de Decisões:** Ao fornecer um ambiente centralizado para análise de dados, o Data Warehouse capacita os tomadores de decisão a extrair informações rapidamente, promovendo decisões mais informadas e estratégicas.

## 5.2. Data Warehouse  - Contexto do Projeto

&emsp;&emsp;No contexto do projeto, destaca-se a implementação de um Data Warehouse no Amazon Redshift. A fase de carga (Load) engloba a ingestão eficiente de dados no Redshift, seguida pela organização (Organize) para assegurar que os dados estejam formatados e otimizados para consultas. Na etapa final, Descoberta (Discover), ocorre a exploração e análise de dados para extrair insights.

&emsp;&emsp;Essa integração de um Data Warehouse no Redshift não apenas simplifica a consolidação e análise de dados, mas também tira proveito da infraestrutura da AWS para garantir escalabilidade. Abaixo, encontra-se um passo a passo detalhado de como realizar o load desses dados no Redshift, oferecendo uma orientação prática para a execução bem-sucedida dessa fase do processo. Depois do último passo descrito no tópico 4.2, você deve clicar em: “Consultar dados”, isso abrirá uma aba nova com o “Query Editor” do Redshift. 

￼![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206636/288d6af0-7dfc-4856-a892-c6cab49b828d)
Figura 09: Workspace
Fonte: Autoria Própria

&emsp;&emsp; No canto superior esquerdo, é possível visualizar um botão escrito “Load Data”, é necessário clicar nele para subir os dados.

￼![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206636/a81dc310-121c-474b-bc48-d1cef25f61de)
Figura 10: Query Editor - RedShift
Fonte: Autoria Própria

&emsp;&emsp; Com o pop-up aberto, você deve selecionar se quer subir um dados que está em um Bucket S3 ou no seu computador, neste caso vamos com a primeira opção. Selecionado, podemos buscar o bucket com o botão: “Browse S3” e selecionar o arquivo único que você deseja subir no momento. Além disso, é importante verificar as informações do formato do arquivo e do seu delimitador. Com tudo selecionado e confirmado, podemos clicar em “Next”.

￼![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206636/6f8edcfd-371d-48e6-b145-aa14968f3c1e)
Figura 11: Load Data - Parte 1
Fonte: Autoria Própria

&emsp;&emsp;Agora, vamos escolher ou criar a tabela que este arquivo será inserido. Caso a tabela já esteja criada, e você deseja somente atualizar, é necessário clicar em “Load existing table”. Neste caso, vamos criar uma nova tabela, então	devemos clicar em “Load New Table”. É necessário selecionar o nome do cluster, criado no tópico 4.2, o database e o schema, este último deve ser sempre o “public”, além disso deve-se criar o nome para a sua tabela e o IAM criado. Com essas configurações, podemos clicar em “Create Table”, ela será criada e você deve clicar em “Load Data”. 

￼![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206636/4f56b03c-2841-49a9-8e8a-e699f2ac92d6)
Figura 12: Load Data - Parte 2
Fonte: Autoria Própria



## 5.3. Estrutura dos dados

### 5.3.1 Entidade Relacional (Load dos dados do S3 para o Redshift):

&emsp;&emsp;Neste modelo, os dados são estruturados em tabelas relacionais no Amazon Redshift. O processo envolve a carga (Load) dos dados do Amazon S3 para o Redshift, onde são organizados em esquemas de banco de dados relacionais.

**Vantagens:**

- Facilita consultas que envolvem relações complexas entre os dados, aproveitando as vantagens da estrutura relacional.
- Ideal para análises complexas e consultas que envolvem agregações e junções.

**Desvantagens:**

- A modelagem relacional pode ser mais complexa para dados que não se encaixam naturalmente em estruturas tabulares.
- Atualizar grandes volumes de dados pode envolver operações complexas e um maior tempo.
  
### 5.3.2 JSON (Tags):

&emsp;&emsp;Os dados são armazenados em formato JSON, permitindo uma estrutura mais flexível. O modelo inclui campos como data_ingestao, value, tag e use, e prioriza a capacidade de ter um histórico detalhado de atualizações (tagdeltas).

**Vantagens:**

- A estrutura JSON é adaptável a diferentes tipos de dados, sendo ideal para dados sem uma estrutura fixa.
- A capacidade de rastrear alterações (tagdeltas) permite um histórico detalhado das atualizações, essencial para auditorias e análises temporais.

**Desvantagens:**

- Pode ser menos eficiente para consultas que envolvem relações complexas entre dados, como junções e agregações.
- Operações analíticas que requerem estruturação intensiva podem ser mais lentas em comparação com modelos relacionais.


### 5.4. Como escolher a estrutura dos dados?

&emsp;&emsp;A escolha entre essas duas abordagens deve ser baseada nos requisitos específicos do projeto. Se a estrutura relacional é crucial para consultas complexas e operações analíticas, a carga no Redshift pode ser preferível. Se a flexibilidade e o histórico detalhado de alterações são mais importantes, o modelo JSON pode ser a escolha certa. Muitas vezes, projetos combinam ambas as abordagens para otimizar diferentes tipos de consultas e requisitos.

# <a name="c6"></a>6. Views

&emsp;&emsp;Em OLAP, uma "view" refere-se a uma visão ou perspectiva específica dos dados armazenados em um banco de dados multidimensional. Uma view em OLAP é uma representação virtual dos dados que pode ser personalizada para atender às necessidades específicas dos usuários. Essas visualizações podem incluir subconjuntos específicos de dados, agregações, cálculos e hierarquias que facilitam a análise de tendências, padrões e resumos de informações.

&emsp;&emsp;No Amazon Redshift, pode-se criar uma view usando a linguagem SQL padrão. Aqui está um exemplo de como criar uma view no Amazon Redshift:

```sql
CREATE VIEW nome_da_view AS
SELECT coluna1, coluna2, SUM(coluna3) AS soma_coluna3
FROM tabela
GROUP BY coluna1, coluna2;
```

&emsp;&emsp;Neste exemplo, você está criando uma view chamada "nome_da_view" que seleciona algumas colunas da tabela e calcula a soma da coluna3, agrupando pelos valores das colunas 1 e 2.

## 6.1 Importância das views 

&emsp;&emsp;**Simplicidade:** As views podem ser projetadas para atender às necessidades específicas dos usuários finais, tornando a análise de dados mais fácil e mais compreensível.

&emsp;&emsp;**Desempenho:** As views podem ser otimizadas para consultas frequentes, permitindo que os usuários acessem dados agregados ou resumidos sem a necessidade de consultar diretamente as tabelas subjacentes, o que pode impactar em termos de desempenho.

&emsp;&emsp;**Segurança:** Views podem ser usadas para restringir o acesso aos dados, permitindo que os usuários vejam apenas as informações relevantes para suas funções e responsabilidades.

&emsp;&emsp;**Consistência:** Ao criar views predefinidas, você garante que os usuários estejam trabalhando com conjuntos de dados consistentes e padronizados, o que ajuda a evitar interpretações divergentes dos dados.

&emsp;&emsp;**Facilidade de Manutenção:** Se houver mudanças na estrutura dos dados, as views podem ser ajustadas sem afetar diretamente as consultas dos usuários, desde que a lógica das views seja mantida.

## 6.2 Entendimento dos dados para as views

&emsp;&emsp;Nestas views, serão utilizados três conjuntos de dados:

**Dados de Localização Geográfica:**
- IBGE.
- Códigos postais.
  
**Dados com Indicadores Socioeconômicos:**
- Pesquisa de Orçamento Familiar (POF).
- ME​C, 
- Receita Federal, 
- SUS, 
- INEP
- IBGE.
  
**Dados sobre Canais de Atendimento Disponíveis:**
- CNPJ.

## 6.3 Primeiras hipóteses criadas

**Análises Simples (Utilizando apenas uma tabela)**

### 6.3.1. Distribuição de Canais de Atendimento a Partir dos CNPJs Cadastrados
   
&emsp;&emsp;A análise visa identificar a distribuição dos canais de atendimento (como mercado, café, bar, etc.) com base nos CNPJs cadastrados nos Buckets (cnpjs_1, cnpjs_2, cnpjs_3, cnpjs_4, cnpjs_5). A comparação será feita considerando a situação regional, características do canal e período.

Colunas sobre situação Regional:
- sigla_uf
- id_municipio
  
Características do Canal de Atendimento:
- identificador_matriz_filial
- cnae_fiscal_principal
- cnae_fiscal_secundaria

Período:
- data (data completa)
  

### 6.3.2. Renda Por Região a Partir do Imposto de Renda (POF)
   
&emsp;&emsp;A análise compara a soma dos valores das colunas de "Renda" com o estado indicado (Ente Federativo) e período, utilizando dados da Receita Federal nos Buckets (distribuicao-renda, distribuicao-renda-socios, distribuicao-renda-socios).

Colunas de renda:
- Rendimentos Tributáveis, 
- Isentos, etc.

Estado:
- Ente Federativo
  
Período:
- Ano-Calendário
- Análise limitada a nível estadual.

### 6.3.3. Renda Por Estado a Partir das Despesas Coletivas (POF)
   
&emsp;&emsp;A análise utiliza a tabela "despesa_coletiva" (Bucket POF) para identificar a condição socioeconômica de cada estado a partir do valor da despesa coletiva, considerando situação regional, características da despesa e período.

Colunas da situação Regional:
- UF (Estado)
- TIPO_SITUACAO_REG (Situação Urbana ou Rural)

Características da Despesa Coletiva:
- NUM_UC (Número de pessoas incluídas no conjunto de consumo)
- V9002 (Forma de Aquisição, Peso Final, Renda Total)

Período:
- V9010 (mês)
- Dados de 2010 até 2018 e análise limitada a nível estadual.

### 6.3.4. Renda Por Estado a Partir das Despesas Individuais (POF)

&emsp;&emsp;A análise utiliza a tabela "despesa_individual" (Bucket POF) para identificar a condição socioeconômica de cada estado a partir do valor da despesa individual, considerando situação regional, características da despesa individual e período.

Colunas da situação Regional:
- UF (Estado)
- TIPO_SITUACAO_REG (Situação Urbana ou Rural)

Características da Despesa Individual:
- NUM_UC (Número de pessoas incluídas no conjunto de consumo)
- V9002 (Forma de Aquisição, Peso Final, Renda Total)

Período:
- V9010 (mês)
  
### 6.3.5. Poder Socioeconômico Regional de Estados a Partir do Desenvolvimento da Indústria (IBGE)

&emsp;&emsp;A análise utiliza a tabela "gini_industria_s3" (Bucket IBGE) para identificar a condição socioeconômica de cada estado a partir do desenvolvimento da indústria local, comparando os estados brasileiros ao longo dos anos.

Colunas dos estados Brasileiros:
- Unidade da Federação (estado)
  
Desenvolvimento Industrial por Ano (Dados disponíveis para anos específicos): 
- 2002, 2003, ..., 2017, 2018


**Análises Compostas (Comparando uma ou mais tabelas)**

### 6.3.6. Potencial Mercado Consumidor em uma Região 

&emsp;&emsp;Observação: Considerando a concentração de Canais de Atendimento a Partir dos CNPJs Cadastrados e Renda a Partir do Imposto de Renda (Receita Federal). 

&emsp;&emsp;Análise envolve a soma do número de cada canal de atendimento e a soma dos rendimentos para cada estado, normalizando datas e regiões. Para fazer essa análise, é interessante fazer : 

1: uma soma do número de  cada canal de atendimento (cnae_fiscal_principal) para cada estado e cidade

2: soma dos rendimentos (Rendimentos_….) para cada estado

&emsp;&emsp;Por fim, é necessário normalizar as datas (ano) e regiões de cada tabela, para que ambos se refiram à mesma região respectiva

Comparar duas tabelas simples lado a lado também é uma opção válida.

## 6.4 Primeiras views criadas
### 6.4.1 View para produtos consumidos por estado (considerando insegurança alimentar)
&emsp;&emsp; Duas views foram criadas com o intuito definir quais são os cinco produtos mais consumidos pelas famílias que consideram ter algum grau de insegurança alimentar em cada estado do Brasil, bem como aqueles consumidos por famílias que não possuem esse problema. A partir dessa análise, o parceiro de projeto conseguirá visualizar quais são aqueles produtos que atendem tanto ao público que tem níveis de insuficiência alimentar, quanto aquele que não possui essas condições. Diante disso, é possível estabelecer estratégias comerciais que gerem lucro para a empresa e impacto social nos locais em que forem aplicadas.

**Visualização de dados referentes às famílias com insegurança alimentar**
```sql
CREATE
OR REPLACE VIEW "public"."top_produtos_por_estado_inseguranca_1" AS
SELECT
cte_top_produtos.uf,
cte_top_produtos.inseguranca_alimentar,
cte_top_produtos.produtos_consumidos,
cte_top_produtos.rank,
cte_top_produtos.frequencia
FROM
(
SELECT
cte_inseguranca.uf,
cte_inseguranca.inseguranca_alimentar,
cte_inseguranca.produtos_consumidos,
pg_catalog.row_number() OVER(
PARTITION BY cte_inseguranca.uf,
cte_inseguranca.inseguranca_alimentar
ORDER BY
cte_inseguranca.frequencia DESC
) AS rank,
cte_inseguranca.frequencia
FROM
(
SELECT
qv.uf,
qv.v701 AS inseguranca_alimentar,
ca.v9001 AS produtos_consumidos,
count(*) AS frequencia
FROM
qualidade_de_vida qv
JOIN consumo_alimentar ca ON qv.uf = ca.uf
WHERE
qv.v701 = 1
GROUP BY
qv.uf,
qv.v701,
ca.v9001
) cte_inseguranca
) cte_top_produtos
WHERE
cte_top_produtos.rank <= 5;
```
**Visualização de dados referentes às famílias que não possuem insegurança alimentar**
```sql
CREATE
OR REPLACE VIEW "public"."top_produtos_por_estado_inseguranca_0" AS
SELECT
cte_top_produtos.uf,
cte_top_produtos.inseguranca_alimentar,
cte_top_produtos.produtos_consumidos,
cte_top_produtos.rank,
cte_top_produtos.frequencia
FROM
(
SELECT
cte_seguranca.uf,
cte_seguranca.inseguranca_alimentar,
cte_seguranca.produtos_consumidos,
pg_catalog.row_number() OVER(
PARTITION BY cte_seguranca.uf,
cte_seguranca.inseguranca_alimentar
ORDER BY
cte_seguranca.frequencia DESC
) AS rank,
cte_seguranca.frequencia
FROM
(
SELECT
qv.uf,
qv.v701 AS inseguranca_alimentar,
ca.v9001 AS produtos_consumidos,
count(*) AS frequencia
FROM
qualidade_de_vida qv
JOIN consumo_alimentar ca ON qv.uf = ca.uf
WHERE
qv.v701 = 0
GROUP BY
qv.uf,
qv.v701,
ca.v9001
) cte_seguranca
) cte_top_produtos
WHERE
cte_top_produtos.rank <= 5;
```
**Tabelas correlacionadas:**

- consumo_alimentar: fornece informações sobre os principais hábitos alimentares das famílias, com dados referentes ao horário de consumo, produtos consumidos, local da alimentação, etc.
  
- qualidade_vida: fornece informações sobre os principais tópicos sobre qualidade de vida, como lazer, moradia, alimentação, situação financeira, etc.

**Relevância para o projeto:**

&emsp;&emsp; As views acima apresentadas são relevantes no processo de identificação dos principais produtos consumidos nos estados brasileiros, fazendo uma correlação entre os produtos consumidos e as situações alimentares da família que o consumiu. Diante disso, é possível fazer uma análise de localidades em que é possível atuar a partir de determinados nichos e mercados, com o intuito de atender, também, às famílias carentes daquele lugar. Além disso, é possível identificar nichos ainda inexplorados que podem ser agregados à linha de produtos ou serviços principal. 

**Exemplo de representação gráfica:**

&emsp;&emsp; O gráfico a seguir apresenta os produtos mais consumidos por famílias que sofrem com insegurança alimentar em todo o território nacional.

![Alimentos mais consumidos nos estados brasileiros](https://github.com/2023M8T4Inteli/grupo2/assets/99206817/07b7086e-e521-454c-bad5-6794693656d9)

Figura 13: gráfico contendo dados referentes à view de famílias que possuem insegurança alimentar.
Fonte: autoria própria.

&emsp;&emsp; A partir desses dados, é possível perceber que 50% dos estados brasileiros possuem a água como primeiro produto consumido por famílias com insegurança alimentar. Seguido do açúcar e dos demais produtos analisados. 

&emsp;&emsp; Abaixo é possível visualizar como fica a tabela cujos dados são referentes às famílias que não possuem insegurança alimentar. Na imagem é possível identificar a tradução do código do produto em uma coluna denominada "Alimento":

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206817/80658248-eda8-4e02-b7d6-2f55b61199a1)

Figura 14: tabela contendo dados referentes à view de famílias sem insegurança alimentar.
Fonte: autoria própria.

&emsp;&emsp; Além disso, na coluna "Frequência" é possível visualizar a quantidade de vezes que aquele alimento apareceu no respectivo estado, demonstrando a frequência de consumo dentre as pessoas que não possuem insegurança alimentar.

**Insights**

&emsp;&emsp; Diante disso, é possível perceber, por exemplo, que o açucar está entre os produtos mais consumidos no país (atrás somente da água, que é um item essencial para a sobrevivência humana), mesmo entre as famílias com algum nível de insegurança alimentar. 

### 6.4.2. View para Características de Dieta:

&emsp;&emsp;Ao unir informações sobre hábitos alimentares, preferências e características específicas de diferentes domicílios, esta view proporciona entender as escolhas alimentares em diversos estratos populacionais. Essa visão é crucial para o cliente, permitindo uma segmentação mais precisa do mercado e a adaptação de estratégias de produtos para atender às demandas específicas de diferentes grupos.

```sql
CREATE VIEW public.v_caracteristicas_dieta AS
SELECT
    cd.uf,
    cd.estrato_pof,
    cd.tipo_situacao_reg,
    cd.cod_upa,
    cd.num_dom,
    cd.num_uc,
    cd.cod_informante,
    cd.v7101,
    cd.v7102,
    cd.v71031,
    cd.v71032,
    cd.v71033,
    cd.v71034,
    cd.v71035,
    cd.v71036,
    cd.v71037,
    cd.v71038,
    cd.v7104,
    cd.v71051,
    cd.v71052,
    cd.v71053,
    cd.v71054,
    cd.v71055,
    cd.v71056,
    cd.v71a01,
    cd.v71a02,
    cd.v72c01,
    cd.v72c02,
    cd.peso,
    cd.peso_final,
    cd.renda_total
FROM public.pof_caracteristicas_dieta cd;
```

### 6.4.3. View para Características de Potêncial de consumo

&emsp;&emsp;A query abaixo cria uma view chamada consumo_potencial que mescla informações das tabelas pof_domicilio e pof_consumo_alimentar. 

```sql
CREATE VIEW public.consumo_potencial AS
SELECT
    d.uf,
    d.num_dom,
    d.v0201, 
    d.v0202,
    d.v0217,
    d.peso_final as peso_dom,

    ca.num_dom as ca_num_dom,
    ca.num_uc as ca_num_uc,
    ca.cod_unidade_medida_final,
    ca.qtd as ca_qtd,
    ca.energia_kcal,
    ca.ptn,
    ca.chotot,
    ca.fibra,
    ca.lip,
    ca.colest,
    ca.agsat,
    ca.agmono,
    ca.agpoli,
    ca.agtrans,
    ca.calcio,
    ca.ferro,
    ca.sodio,
    ca.magnesio,
    ca.fosforo,
    ca.potassio,
    ca.cobre,
    ca.zinco,
    ca.vita_rae,
    ca.tiamina,
    ca.riboflavina,
    ca.niacina,
    ca.piridoxamina,
    ca.cobalamina,
    ca.vitd,
    ca.vite,
    ca.vitc,
    ca.folato,
    ca.peso_final as peso_ca,
    ca.renda_total as renda_total_ca

FROM public."pof - domicilio" d
JOIN public."pof - consumo_alimentar" ca ON d.uf = ca.uf AND d.num_dom = ca.num_dom;
```

**Tabelas Mescladas:**

- pof_domicilio (d): Fornece informações sobre o domicílio, como localização (uf), número do domicílio (num_dom), características do domicílio (v0201, v0202, v0217), e peso final do domicílio (peso_final).

- pof_consumo_alimentar (ca): Contém informações sobre o consumo alimentar, incluindo o número do domicílio (num_dom), número da unidade consumidora (num_uc), quantidade consumida (qtd), dados nutricionais e informações sobre o peso final do consumo (peso_final) e a renda total (renda_total).

**Relevância para o Projeto:**

- A view fornece uma visão unificada do potencial de consumo, relacionando características do domicílio com detalhes específicos do consumo alimentar. Isso é essencial para entender o contexto em que o consumo ocorre.
- A análise desses dados pode ajudar o cliente a direcionar suas ações estrategicamente, como ajustar a oferta de produtos com base nas preferências do consumidor em diferentes regiões.

**Exemplo de visualização gráfica**

&emsp;&emsp;O gráfico mostra o consumo médio de cálcio por pessoa por dia nas duas unidades federativas do Brasil: Rondônia (UF 11) e Acre (UF 12). O consumo é medido em miligramas (mg) por dia.

<img src="./../../assets/UF%20X%20Número%20de%20Domicílios.png" width="400px">
Figura 15: Gráfico do consumo médio de cálcio per capita na Rondônia (UF 11) e no Acre (UF 12)
Fonte: Autoria Própria  


&emsp;&emsp;O gráfico mostra que o consumo médio de cálcio em Rondônia é de 570 mg por dia, enquanto no Acre é de 620 mg por dia. Isso significa que os habitantes do Acre consomem, em média, 50 mg de cálcio a mais por dia do que os habitantes de Rondônia.

&emsp;&emsp;A Organização Mundial da Saúde (OMS) recomenda que os adultos consumam pelo menos 1.000 mg de cálcio por dia. Portanto, tanto os habitantes de Rondônia quanto os do Acre estão abaixo da recomendação da OMS.

&emsp;&emsp;Alguns fatores que podem contribuir para o baixo consumo de cálcio nas duas unidades federativas são:

- A dieta predominante é baseada em alimentos ricos em carboidratos e pobres em nutrientes, como frutas, vegetais e laticínios.
- A falta de acesso a alimentos ricos em cálcio, como leite, queijo e iogurte.
- A falta de educação nutricional sobre a importância do consumo de cálcio.

&emsp;&emsp;Para aumentar o consumo de cálcio nas duas unidades federativas, é importante promover mudanças na dieta e na educação nutricional. Isso pode ser feito por meio de campanhas de conscientização, programas de educação alimentar e ações de incentivo ao consumo de alimentos ricos em cálcio.

&emsp;&emsp;Aqui estão algumas hipóteses para aumentar o consumo de cálcio:

- Incluir leite, queijo e iogurte na dieta diária.
- Consumir frutas secas, como amêndoas, nozes e castanhas.
- Adicionar vegetais às refeições.

&emsp;&emsp;**Observação:** Devido à restrição de aproximadamente 3000 linhas ao executar a view no Redshift, o gráfico atual exibe apenas dados de duas unidades federativas brasileiras. No entanto, na próxima sprint, quando aplicarmos isso em uma ferramenta como o Grafana, a comparação será estendida para incluir todos os estados na análise. 

# <a name="c7"></a>7. Referências
- [Documentação do Amazon Redshift](https://docs.aws.amazon.com/redshift/)
- [Diferença entre um data warehouse, data lake e data mart](https://aws.amazon.com/pt/compare/the-difference-between-a-data-warehouse-data-lake-and-data-mart/)
- [OLAP (Processamento Analítico Online)](https://aws.amazon.com/pt/what-is/olap/#:~:text=O%20processamento%20anal%C3%ADtico%20on%2Dline,medidores%20inteligentes%20e%20sistemas%20internos.)
- [CREATE VIEW - Documentação do Amazon Redshift](https://docs.aws.amazon.com/pt_br/redshift/latest/dg/r_CREATE_VIEW.html)


