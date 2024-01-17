## Sumário

[1. Mapeamento do fluxo](#c1)

[2. Serviços](#c2)

[3. Processo de ETL - Monitoramento e Gerenciamento](#c3) 

<br>

# <a name="c1"></a>1. Mapeamento do fluxo

&emsp;&emsp; O processo ETL, Extract, Transform, Load (Extrair, Transformar, Carregar), é utilizado no gerenciamento de dados, especialmente em ambientes de _data warehousing_. Ao lidar com informações provenientes de diversas fontes, como arquivos CSV e APIs, a execução eficiente do ETL se torna crucial para garantir a qualidade e a utilidade dos dados no contexto de um projeto.

## 1.1 Extração
&emsp;&emsp; Na fase inicial de extração, os dados são coletados de fontes heterogêneas, arquivos CSV. É fundamental garantir a integridade dos dados nesse processo, identificando e corrigindo possíveis inconsistências ou erros nas fontes. Esta etapa estabelece a base para as transformações subsequentes.

## 1.2 Transformação
&emsp;&emsp; A transformação representa a refinada arte de moldar dados brutos em informações úteis e coerentes. Inicia-se com a limpeza, abrangendo correção de erros, eliminação de duplicatas e tratamento de valores ausentes. Além disso, os dados são formatados de modo a garantir consistência e conformidade, incorporando regras de negócios específicas do projeto.

## 1.3 Carregamento
&emsp;&emsp; A etapa final, o carregamento, conduz os dados transformados ao seu destino final: um data warehouse. Inicialmente, um carregamento completo é efetuado, seguido pela possibilidade de atualizações incrementais. O data warehouse organiza os dados de maneira eficiente, oferecendo a base sólida necessária para análises avançadas e a geração de relatórios significativos.

## 1.4 Monitoramento do Processo ETL
&emsp;&emsp; A monitorização contínua durante cada etapa do processo ETL é vital para garantir o desempenho, a integridade e a disponibilidade dos dados. A próxima seção abordará especificamente as práticas de monitoramento e gerenciamento adotadas para alcançar esses objetivos.

# <a name="c2"></a>2. Serviços

&emsp;&emsp; A Amazon Web Services (AWS) é amplamente reconhecida por sua ampla gama de serviços, proporcionando a capacidade de construir pipelines de ETL (Extração, Transformação e Carga) e sistemas de armazenamento de dados altamente escaláveis e eficientes. O processo de ETL abrange as fases de extração, transformação e carga de dados, e a AWS oferece diversas ferramentas destinadas a otimizar cada uma dessas etapas, resultando em pipelines de dados robustos e flexíveis. Esses serviços foram estrategicamente empregados na implementação de um pipeline de ETL personalizado, ajustado às necessidades específicas do projeto em questão. 

&emsp;&emsp; **Amazon S3**:  O Amazon S3 é um serviço de armazenamento de objetos escalável que pode ser utilizado no processo de armazenar dados brutos e processados. Dessa forma, podem servir como um local intermediário para dados processados antes de serem carregados em um data warehouse.

&emsp;&emsp; **Amazon EC2** (Elastic Compute Cloud): Este serviço oferece capacidade de computação na nuvem, desempenhando um papel essencial na fase de transformação, especialmente para dados complexos que demandam recursos computacionais significativos. Permitindo com que os usuários criem e executem máquinas virtuais em servidores da AWS, proporcionando flexibilidade e escalabilidade.

&emsp;&emsp; **AWS Lambda**: O AWS Lambda, projetado para execução eficiente de código sem a necessidade de gerenciar infraestrutura, é útil para transformações de dados simples e menos complexas, permitindo a criação e implantação de funções que respondem a eventos e executam tarefas específicas.

&emsp;&emsp; **Amazon Redshift**:  O Amazon Redshift é um serviço de data warehouse gerenciado, que oferece alta performance para análise de dados. Após a etapa de ETL, os dados podem ser carregados no Redshift, possibilitando a execução de consultas analíticas para obter insights valiosos a partir dos dados processados.


# <a name="c3"></a>3. Aspectos de Segurança, Privacidade e Conformidade

&emsp;&emsp; A segurança, privacidade e conformidade dos dados são de importância crítica em qualquer ambiente de ETL. Abaixo estão as práticas adotadas para garantir a integridade e a proteção dos dados sensíveis:

## 3.1 Segurança
&emsp;&emsp; - **Controle de Acesso**: Implementação rigorosa de políticas de controle de acesso para garantir que apenas usuários autorizados tenham acesso aos dados durante as diferentes fases do ETL.
&emsp;&emsp; - **Encriptação de Dados**: Utilização de técnicas robustas de criptografia para proteger dados em trânsito e em repouso, garantindo a confidencialidade.

## 3.2 Privacidade
&emsp;&emsp; - **Anonimização e Pseudonimização**: Aplicação de técnicas de anonimização e pseudonimização para proteger a identidade de indivíduos, especialmente quando os dados envolvidos são sensíveis.

## 3.3 Conformidade
&emsp;&emsp; - **Auditorias Regulares**: Realização de auditorias regulares para garantir a conformidade com regulamentações de privacidade e segurança de dados.
&emsp;&emsp; - **Políticas de Retenção de Dados**: Implementação de políticas claras de retenção de dados para garantir conformidade com as regulamentações relevantes.

&emsp;&emsp; Essas práticas asseguram que o processo de ETL está alinhado com os mais altos padrões de segurança, privacidade e conformidade.

Mais informações de segurança, acesse o documento <a href="../sprint3/seguranca_e_protecao_de_dados.md">Segurança e Proteção de Dados</a>


# <a name="c4"></a>4. Processo de ETL - Monitoramento e Gerenciamento

## 4.1 Visão Geral
&emsp;&emsp; A seguir, descreveremos as práticas de monitoramento e gerenciamento do processo de ETL em um ambiente AWS, utilizando o serviço AWS Redshift Serverless e as ferramentas de monitoramento do Amazon CloudWatch.

## 4.2 Informações do Ambiente

- Namespace: workspace-cubo-data-dream  
- ID do Namespace: 2b23c6b1-fdf0-4011-aae6-a6e56387d063  
- ARN do Namespace: arn:aws:redshift-serverless:us-east-1:185405266895:namespace/2b23c6b1-fdf0-4011-aae6-a6e56387d063  
- Status: Disponível  
- Data de Criação: 21 de Novembro de 2023  
- Usuário Admin: admin  
- Nome do Banco de Dados: dev  
- Armazenamento Utilizado: 153.5 GB  
- Contagem Total de Tabelas: 92

## 4.3 Monitoramento com Amazon CloudWatch
&emsp;&emsp; O Amazon CloudWatch é utilizado para monitorar métricas vitais relacionadas ao processo de ETL, as quais incluem o número de objetos e o tamanho do bucket em bytes. As métricas são visualizadas em gráficos que demonstram a média diária, proporcionando uma análise de tendências e comportamento dos dados ao longo do tempo.

### 4.3.1 Métricas Monitoradas
- **NumberOfObjects:** Esta métrica representa a contagem média de objetos em diferentes buckets de dados, categorizados por fontes de dados como cnjp-data-dream, dadosinep-data-dream, dadosmec-data-dream, entre outros.


- **BucketSizeBytes:** Esta métrica representa o tamanho médio em bytes dos buckets mencionados, permitindo a avaliação da utilização do armazenamento. A métrica BucketSizeBytes revela uma disparidade notável entre os tamanhos dos buckets. Especificamente, o bucket associado ao datasus-data-dream destaca-se por ter um tamanho significativamente maior em comparação com os demais. Isso indica que os dados provenientes do DATASUS são substancialmente maiores, o que pode refletir a complexidade e a riqueza dos conjuntos de dados de saúde, exigindo uma atenção especial em termos de processamento e análise.


### 4.3.2 Implicações e Ações
- **Avaliação de Capacidade:** A discrepância no tamanho dos buckets, especialmente para datasus-data-dream, sugere a necessidade de uma avaliação de capacidade e performance, para assegurar que o ambiente está dimensionado adequadamente.

- **Análise de Custo:** A gestão do tamanho dos buckets é essencial para otimizar os custos. O bucket datasus-data-dream pode necessitar de estratégias de compactação de dados ou arquivamento para controlar os gastos.

- **Priorização de Processamento:** Dados do datasus-data-dream podem requerer mais recursos durante as etapas de transformação devido ao seu volume, o que deve ser considerado no planejamento de capacidade do ETL.

### 4.3.3 Alarmes e Notificações
- **Alarmes de Utilização:** Configurados para notificar a equipe caso o número de objetos diminua ou aumente drasticamente, indicando potenciais problemas de ingestão ou exclusão de dados.

- **Alarmes de Capacidade:** Acionados se o tamanho do bucket exceder um limite específico, o que pode indicar uma necessidade de escalar recursos ou investigar a eficiência do processo de transformação de dados.

## 4.4 Gerenciamento e Otimização
&emsp;&emsp; O gerenciamento proativo do ambiente é realizado por meio da revisão contínua das métricas coletadas, garantindo que o processo de ETL esteja otimizado para performance e custo.

### 4.4.1 Ações de Gerenciamento
- **Análise de Tendências:** Realizada semanalmente para identificar padrões de crescimento de dados e ajustar processos de ETL conforme necessário.

- **Otimização de Recursos:** Baseada nas métricas, recursos como capacidade de armazenamento e computação são ajustados para atender à demanda dinâmica.

## 4.5 Monitoramento

### 4.5.1 Métricas de Desempenho

- **Tempo de Execução do ETL:** Monitoramos o tempo de execução do processo de ETL para garantir que esteja dentro dos limites aceitáveis. Qualquer aumento significativo é investigado para otimização.
- **Taxa de Sucesso da Transformação:** A taxa de sucesso da transformação é monitorada para identificar possíveis falhas ou erros na fase crítica de transformação de dados.

### 4.5.1 Métricas de Integridade

- **Logs de Erro:** Mantemos logs detalhados de erros para rastrear e corrigir quaisquer problemas que possam comprometer a integridade dos dados.

### 4.5.1 Métricas de Disponibilidade

- **Tempo de Inatividade do Sistema:** Monitoramos o tempo de inatividade do sistema para garantir alta disponibilidade. Qualquer tempo de inatividade não planejado é imediatamente abordado.
- **Recuperação de Falhas:** Implementamos backups para lidar com falhas e garantir a continuidade do processo de ETL.

## 4.6 Conclusão
&emsp;&emsp; Em resumo, o ambiente **workspace-cubo-data-dream** está estruturado para garantir uma operação de ETL segura. Através do monitoramento constante e das práticas de gerenciamento adotadas, buscamos assegurar a integridade dos processos. A análise detalhada das métricas no Amazon CloudWatch, especialmente no que diz respeito ao notável aumento no tamanho do bucket **datasus-data-dream**, destaca a importância de adaptar dinamicamente nossa capacidade para lidar com conjuntos de dados desafiadores, como os relacionados à saúde. Ao realizar análises semanais de tendências e ajustes contínuos com base nas métricas coletadas, procuramos otimizar o desempenho e controlar efetivamente os custos. Em suma, nosso ambiente de ETL está preparado para evoluir conforme necessário, mantendo a qualidade e a confiabilidade dos dados ao longo do tempo.



# Observação:

Se não houver localizado informações pertinentes no presente documento, por favor, consulte o link a seguir, que direciona à documentação oficial.

<a href="https://docs.google.com/document/d/18IWwAVmbsr7sUm45ySdnJtWkj1H6QQnC/edit?usp=sharing&ouid=112389543027386593098&rtpof=true&sd=true">Documentação Oficial</a>