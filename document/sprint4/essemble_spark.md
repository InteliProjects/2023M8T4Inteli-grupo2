# Spark - O que é e sua Importância

## O que é Spark?

Apache Spark é um framework de processamento de dados distribuído, projetado para lidar com grandes volumes de dados de forma eficiente e escalável. Ele fornece APIs em várias linguagens, incluindo Python, para processamento de dados em lote e em tempo real.

## Funcionalidades do Spark:

1. **Processamento Distribuído:** Permite processar dados em clusters para maior velocidade e escalabilidade.
2. **Suporte a Diversos Tipos de Dados:** Pode lidar com dados estruturados e não estruturados.
3. **Módulos Integrados:** Inclui módulos para processamento de SQL, machine learning, streaming, etc.
4. **Resiliência e Tolerância a Falhas:** Oferece alta disponibilidade e capacidade de recuperação em caso de falhas.

## Importância do Spark:

1. **Processamento Rápido:** O Spark é conhecido por seu processamento rápido de dados, sendo até 100 vezes mais rápido que o Hadoop MapReduce.
2. **Facilidade de Uso:** Oferece APIs simples e abstratas para facilitar o desenvolvimento.
3. **Versatilidade:** Pode ser usado para uma variedade de casos, incluindo análise de dados, machine learning e processamento de streaming.
4. **Escalabilidade:** Pode escalar horizontalmente para lidar com grandes volumes de dados.


# Configuração do Ambiente Spark

O código inicia ajustando as configurações do ambiente Spark, configurando a quantidade de memória do executor para 2 gigabytes.

1. Inicialização do Spark no Jupyter usando findspark

A biblioteca `findspark` é utilizada para inicializar o Spark no ambiente Jupyter.

2. Criação da Sessão Spark

Uma sessão Spark é criada com o nome "RandomFlorestIPMNMSpark". Configurações adicionais, como a porta do driver e a configuração do executor, são definidas.

3. Carregamento dos Dados no DataFrame Spark

O DataFrame Spark, `pof6_spark`, é criado a partir do DataFrame Pandas `pof6`.

4. Seleção de Colunas Necessárias

São selecionadas as colunas relevantes para o modelo preditivo.

5. Conversão das Features em um Vetor usando VectorAssembler

As features são combinadas em um único vetor usando `VectorAssembler`.

6. Divisão do DataFrame em Conjuntos de Treinamento e Teste

O DataFrame é dividido em conjuntos de treinamento e teste (80% e 20%, respectivamente).

7. Configuração do Modelo RandomForestRegressor

Um modelo de regressão RandomForest é configurado com 100 árvores de decisão.

8. Ajuste do Modelo aos Dados de Treinamento

O modelo é treinado com os dados de treinamento.

9. Previsões nos Dados de Teste

O modelo faz previsões nos dados de teste.

10. Avaliação do Modelo usando Métricas

O desempenho do modelo é avaliado usando métricas como Mean Squared Error (MSE), Root Mean Squared Error (RMSE), Mean Absolute Error (MAE) e R-squared (R²).

11. Exibição das Métricas

As métricas calculadas são exibidas para avaliação do desempenho do modelo.

12. Finalização da Sessão Spark

A sessão Spark é encerrada para liberar recursos.






