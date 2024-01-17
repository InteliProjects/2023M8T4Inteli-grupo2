## Sumário

[1. Mapeamento do fluxo](#c1)

[2. Serviços](#c2)

[3. Processo de ETL - Monitoramento e Gerenciamento](#c3) 

<br>

# <a name="c1"></a>1. Mapeamento do fluxo

&emsp;&emsp; O processo ETL, Extract, Transform, Load (Extrair, Transformar, Carregar), é utilizado no gerenciamento de dados, especialmente em ambientes de _data warehousing_. Ao lidar com informações provenientes de diversas fontes, como arquivos CSV e APIs, a execução eficiente do ETL se torna crucial para garantir a qualidade e a utilidade dos dados no contexto de um projeto.

## 1.1 Extração
&emsp;&emsp; Na fase inicial, a extração é realizada a partir de fontes heterogêneas, abrangendo desde bancos de dados SQL e NoSQL até arquivos CSV e sistemas de CRM ou ERP. É imperativo atentar para a integridade dos dados durante esse processo, considerando a possibilidade de inconsistências ou erros nas fontes. Essa etapa estabelece a base para as transformações subsequentes.

## 1.2 Transformação
&emsp;&emsp; A transformação representa a refinada arte de moldar dados brutos em informações úteis e coerentes. Inicia-se com a limpeza, abrangendo correção de erros, eliminação de duplicatas e tratamento de valores ausentes. Além disso, os dados são formatados de modo a garantir consistência e conformidade, incorporando regras de negócios específicas do projeto.

## 1.3 Carregamento
&emsp;&emsp; A etapa final, o carregamento, conduz os dados transformados ao seu destino final: um data warehouse. Inicialmente, um carregamento completo é efetuado, seguido pela possibilidade de atualizações incrementais. O data warehouse organiza os dados de maneira eficiente, oferecendo a base sólida necessária para análises avançadas e a geração de relatórios significativos.

&emsp;&emsp; Essas fases do processo ETL não apenas formam a espinha dorsal de projetos de Big Data, mas também garantem que os dados, desde sua origem até o armazenamento final, estejam preparados para análises robustas, promovendo insights valiosos para a tomada de decisões estratégicas.


# <a name="c2"></a>2. Serviços

&emsp;&emsp; A Amazon Web Services (AWS) é amplamente reconhecida por sua ampla gama de serviços, proporcionando a capacidade de construir pipelines de ETL (Extração, Transformação e Carga) e sistemas de armazenamento de dados altamente escaláveis e eficientes. O processo de ETL abrange as fases de extração, transformação e carga de dados, e a AWS oferece diversas ferramentas destinadas a otimizar cada uma dessas etapas, resultando em pipelines de dados robustos e flexíveis. Esses serviços foram estrategicamente empregados na implementação de um pipeline de ETL personalizado, ajustado às necessidades específicas do projeto em questão. 


&emsp;&emsp; **AWS Glue**: O AWS Glue destaca-se como um serviço que facilita a extração e transformação de dados, automatizando o processo de preparação e carga para análises, e armazenamento no Amazon S3. Ele oferece recursos de catalogação  e uma interface visual que permite a criação de transformações ETL sem a necessidade de codificação, dessa forma facilitando a criação de pipelines de dados complexos, realizando uma abordagem mais gráfica. Desempenhando um papel crucial nas fases de extração e transformação.

&emsp;&emsp; **Amazon S3**:  O Amazon S3 é um serviço de armazenamento de objetos escalável que pode ser utilizado no processo de armazenar dados brutos e processados. Dessa forma, podem servir como um local intermediário para dados processados antes de serem carregados em um data warehouse. 

&emsp;&emsp; **O Amazon EC2** (Elastic Compute Cloud) oferece capacidade de computação na nuvem, desempenhando um papel essencial na fase de transformação, especialmente para dados complexos que demandam recursos computacionais significativos.Permitindo com que os usuários criem e executem máquinas virtuais em servidores da AWS, proporcionando flexibilidade e escalabilidade.

&emsp;&emsp;**AWS Lambda**: O AWS Lambda, projetado para execução eficiente de código sem a necessidade de gerenciar infraestrutura, é útil para transformações de dados simples e menos complexas, permitindo a criação e implantação de funções que respondem a eventos e executam tarefas específicas.

&emsp;&emsp;**Amazon Redshift**:  O Amazon Redshift é um serviço de data warehouse gerenciado, que oferece alta performance para análise de dados. Após a etapa de ETL, os dados podem ser carregados no Redshift, possibilitando a execução de consultas analíticas para obter insights valiosos a partir dos dados processados

# <a name="c3"></a>3. Processo de ETL - Monitoramento e Gerenciamento

## 3.1 Visão Geral
&emsp;&emsp; A seguir, descreveremos as práticas de monitoramento e gerenciamento do processo de ETL em um ambiente AWS, utilizando o serviço AWS Redshift Serverless e as ferramentas de monitoramento do Amazon CloudWatch.

## 3.2 Informações do Ambiente

![image](https://github.com/2023M8T4Inteli/grupo2/assets/68927480/805100bb-a681-4922-a97c-2765758cbbe2)
*Figura 1:* Informações do Ambiente.
**Fonte:** AWS Console.


- Namespace: workspace-cubo-data-dream  
- ID do Namespace: 2b23c6b1-fdf0-4011-aae6-a6e56387d063  
- ARN do Namespace: arn:aws:redshift-serverless:us-east-1:185405266895:namespace/2b23c6b1-fdf0-4011-aae6-a6e56387d063  
- Status: Disponível  
- Data de Criação: 21 de Novembro de 2023  
- Usuário Admin: admin  
- Nome do Banco de Dados: dev  
- Armazenamento Utilizado: 153.5 GB  
- Contagem Total de Tabelas: 92

## 3.3 Monitoramento com Amazon CloudWatch
&emsp;&emsp; O Amazon CloudWatch é utilizado para monitorar métricas vitais relacionadas ao processo de ETL, as quais incluem o número de objetos e o tamanho do bucket em bytes. As métricas são visualizadas em gráficos que demonstram a média diária, proporcionando uma análise de tendências e comportamento dos dados ao longo do tempo.

### 3.3.1 Métricas Monitoradas
- **NumberOfObjects:** Esta métrica representa a contagem média de objetos em diferentes buckets de dados, categorizados por fontes de dados como cnjp-data-dream, dadosinep-data-dream, dadosmec-data-dream, entre outros.

![image](https://github.com/2023M8T4Inteli/grupo2/assets/68927480/06804287-9b15-4f4c-a838-b4eeb8dcfb8b)
*Figura 2:* Number Of Objects.
**Fonte:** Amazon CloudWatch.

- **BucketSizeBytes:** Esta métrica representa o tamanho médio em bytes dos buckets mencionados, permitindo a avaliação da utilização do armazenamento. A métrica BucketSizeBytes revela uma disparidade notável entre os tamanhos dos buckets. Especificamente, o bucket associado ao datasus-data-dream destaca-se por ter um tamanho significativamente maior em comparação com os demais. Isso indica que os dados provenientes do DATASUS são substancialmente maiores, o que pode refletir a complexidade e a riqueza dos conjuntos de dados de saúde, exigindo uma atenção especial em termos de processamento e análise.

![image](https://github.com/2023M8T4Inteli/grupo2/assets/68927480/0bb87920-72d3-4778-92d2-f9d2fa1f344e)
*Figura 3:* Bucket Size Bytes.
**Fonte:** Amazon CloudWatch.

### 3.3.2 Implicações e Ações
- **Avaliação de Capacidade:** A discrepância no tamanho dos buckets, especialmente para datasus-data-dream, sugere a necessidade de uma avaliação de capacidade e performance, para assegurar que o ambiente está dimensionado adequadamente.

- **Análise de Custo:** A gestão do tamanho dos buckets é essencial para otimizar os custos. O bucket datasus-data-dream pode necessitar de estratégias de compactação de dados ou arquivamento para controlar os gastos.

- **Priorização de Processamento:** Dados do datasus-data-dream podem requerer mais recursos durante as etapas de transformação devido ao seu volume, o que deve ser considerado no planejamento de capacidade do ETL.

### 3.3.3 Alarmes e Notificações
- **Alarmes de Utilização:** Configurados para notificar a equipe caso o número de objetos diminua ou aumente drasticamente, indicando potenciais problemas de ingestão ou exclusão de dados.

- **Alarmes de Capacidade:** Acionados se o tamanho do bucket exceder um limite específico, o que pode indicar uma necessidade de escalar recursos ou investigar a eficiência do processo de transformação de dados.

## 3.4 Gerenciamento e Otimização
&emsp;&emsp; O gerenciamento proativo do ambiente é realizado por meio da revisão contínua das métricas coletadas, garantindo que o processo de ETL esteja otimizado para performance e custo.

### 3.4.1 Ações de Gerenciamento
- **Análise de Tendências:** Realizada semanalmente para identificar padrões de crescimento de dados e ajustar processos de ETL conforme necessário.

- **Otimização de Recursos:** Baseada nas métricas, recursos como capacidade de armazenamento e computação são ajustados para atender à demanda dinâmica.

## 3.5 Conclusão
&emsp;&emsp; Em resumo, o ambiente **workspace-cubo-data-dream** está estruturado para garantir uma operação de ETL segura. Através do monitoramento constante e das práticas de gerenciamento adotadas, buscamos assegurar a integridade dos processos. A análise detalhada das métricas no Amazon CloudWatch, especialmente no que diz respeito ao notável aumento no tamanho do bucket **datasus-data-dream**, destaca a importância de adaptar dinamicamente nossa capacidade para lidar com conjuntos de dados desafiadores, como os relacionados à saúde. Ao realizar análises semanais de tendências e ajustes contínuos com base nas métricas coletadas, procuramos otimizar o desempenho e controlar efetivamente os custos. Em suma, nosso ambiente de ETL está preparado para evoluir conforme necessário, mantendo a qualidade e a confiabilidade dos dados ao longo do tempo.




