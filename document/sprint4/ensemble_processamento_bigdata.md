# Avaliação do modelo Ensemble com CRISP-DM


## 1. Entendimento do negócio 
Durante essa etapa, é crucial obtermos uma compreensão profunda dos objetivos do negócio. Estabelecer uma comunicação transparente e eficaz com nossos parceiros é essencial. É fundamental definir os critérios que determinarão o sucesso de nosso projeto e entender como agir com base neles. Em outras palavras, ao entendermos o perfil de nossos clientes e usuários, podemos, por meio de análises, extrair insights valiosos e relevantes.

## 2. Entendimento dos dados  
A fase de compreensão dos dados tem início na coleta inicial dos dados. Nesse estágio, conduzimos uma análise abrangente dos dados fornecidos pelo nosso parceiro, abrangendo informações do POF, bem como a coleta de dados considerados cruciais de fontes como Datasus, IBGE, Mec e Inep. Identificamos correlações significativas, como aquelas entre o consumo de itens do mercado e CNPJs, permitindo insights valiosos sobre áreas com maior demanda, expansão comercial, entre outros.

## 3. Preparação dos dados 
Na etapa de preparação dos dados, realizamos a limpeza e o pré-processamento dos dados coletados. Selecionamos os dados e arquivos considerados mais relevantes, realizando a escolha e transformação de variáveis essenciais. Além disso, desenvolvemos um script padronizado para todos os arquivos de dados, garantindo que passassem por um processo consistente de e processamento. Esse script envolvia a leitura de arquivos CSV, aplicação de tratamentos aos dados, remoção de linhas duplicadas, eliminação de valores nulos, entre outros. Esse procedimento foi repetido para todos os arquivos de dados, assegurando um carregamento consistente, limpeza e tratamento.

Na imagem abaixo, é possível observar um exemplo de código empregado no estágio de pré-processamento de dados, executando as devidas etapas para a realização dos testes com base nos dados.
![image](https://github.com/2023M8T4Inteli/grupo2/assets/99209712/acc0f5d5-398f-4586-8184-978677aaf8d2)
**Imagem x**: Pré-processamento dos dados <br> 
**Fonte**: Elaboração própria <br> 

## 4. Modelagem 
O processo de modelagem abrange as fases de seleção e aplicação de técnicas, como algoritmos de aprendizado de máquina, envolvendo a configuração de parâmetros e o ajuste do treinamento dos modelos. Nessa etapa, é crucial avaliar o desempenho do modelo por meio dos dados de treinamento.

No exemplo a seguir, utilizamos um notebook para ler dois arquivos de tabelas distintas da POF, empregando uma abordagem analítica com diferentes tabelas para testar duas teorias. Inicialmente, selecionamos dois índices amplamente utilizados: o IPM-NM (Índice de Pobreza Multidimensional Não Monetária) e o IVM-PN (Índice de Vulnerabilidade Municipal - Pobreza Não Monetária). O IPM-NM avalia a pobreza em diversas áreas da vida, como saúde, educação e moradia, enquanto o IVM-PN mede a vulnerabilidade e pobreza em uma cidade, considerando fatores além da renda, como acesso a serviços e qualidade de vida.

**IPM-NM** <br> 
Para a análise do IPM-NM, escolhemos um algoritmo bem conhecido para compreender e interpretar os dados: Random Forest (Floresta Aleatória), pertencente à categoria de métodos ensemble, para combinar vários modelos a fim de melhorar o desempenho e a generalização do modelo final, utilizando árvores de decisão como base.

Selecionamos uma tabela da POF que abrange aspectos cruciais nos estados do Brasil, como proporção de pessoas com algum grau de pobreza, nível de educação, saúde e moradia, para auxiliar nas análises.

A seguir, conduzimos o processo de construção, treinamento e avaliação do modelo escolhido. Inicialmente, carregamos os dados, dividindo-os em conjuntos de treinamento e teste para representar valores, variáveis e características. Em seguida, instalamos o modelo para garantir reprodutibilidade e iniciamos o treinamento com o conjunto de treinamento. Posteriormente, realizamos a previsão do modelo no conjunto de testes. Por fim, definimos várias métricas de regressão para avaliar o desempenho do modelo, incluindo Erro Quadrático Médio (MSE), Erro Quadrático Médio Raiz (RMSE), Erro Absoluto Médio (MAE) e Coeficiente de Determinação (R²).


**IVM-NM**

Para a implementação do modelo na análise do índice IVM-NM, empregamos o algoritmo Gradiente Boosting Regressor, reconhecido como uma técnica de aprendizado de máquina voltada para problemas de regressão. A concepção fundamental por trás do Gradient Boosting envolve a construção sequencial de modelos fracos, nos quais cada novo modelo é treinado para corrigir os erros do modelo anterior. Esse processo iterativo ajusta os pesos dos modelos anteriores com base nos erros residuais, sendo a otimização do gradiente descendente, onde o modelo é ajustado na direção oposta ao gradiente da função de perda em relação aos parâmetros do modelo, denominada como "Gradient".

No contexto de regressão, o Gradient Boosting Regressor demonstra eficácia especialmente em situações com relacionamentos complexos e não lineares nos dados. Sua capacidade de lidar com outliers e resistência ao overfitting contribuem para um desempenho robusto em diversas circunstâncias.

Para essa análise específica, selecionamos uma tabela da POF fornecida pelo parceiro, contendo informações diversas, como moradia, acesso aos serviços de utilidade pública, saúde e alimentação, educação, acesso a serviços financeiros e padrão de vida, entre outros. Posteriormente, procedemos com a preparação e instanciamento da aplicação do modelo, incluindo o treinamento do modelo, a predição no conjunto de teste e a escolha das mesmas métricas utilizadas no outro algoritmo para análise, visando obter insights e informações relevantes.

As métricas utilizadas para avaliação foram as mesmas do caso anterior: Erro Quadrático Médio (MSE), Erro Quadrático Médio Raiz (RMSE), Erro Absoluto Médio (MAE) e Coeficiente de Determinação (R²). Essas métricas são essenciais para compreender a qualidade do modelo na previsão do índice IVM-NM, proporcionando uma análise comparativa e aprofundada de seu desempenho.

## 5. Avaliação
O processo de avaliação inclui do modelo foi realizado com base nos critérios de sucesso definidos para compreendermos caso atingimos o objetivo do projeto. 

**IPM-NM** <br> 
O Modelo de regressão utilizando a técnica de Floresta Aleatória foi avaliado com base em diversas métricas para compreender sua eficácia na previsão do índice de pobreza multidimensional normalizado (IPM-NM). E os seguintes valores foram encontrados: 
Mean Squared Error (MSE): é a média dos quadrados dos erros entre as previsões do modelo e os valores reais. Quanto menor o MSE, melhor. Neste caso, o valor de MSE indica que, em média, os quadrados dos erros são cerca de 20.44.
 Root Mean Squared Error (RMSE): O RMSE é a raiz quadrada do MSE. Ele fornece uma interpretação mais intuitiva, pois está na mesma unidade que a variável de resposta. Neste caso, o RMSE indica que, em média, os erros são cerca de 4.52 unidades.
Mean Absolute Error (MAE): O MAE é a média dos valores absolutos dos erros entre as previsões e os valores reais. Ele mede a magnitude média dos erros sem considerar a direção. Neste caso, o MÃE indica que, em média, os erros são cerca de 4.19 unidades.
 R-squared (R²): O R-squared, ou coeficiente de determinação, mede a proporção da variabilidade na variável de resposta que é explicada pelo modelo. Um valor de 1 indica um ajuste perfeito, enquanto um valor de 0 indica que o modelo não explica nada da variabilidade. Neste caso, o R 2 de aproximadamente 0.55 sugere que o modelo explica cerca de 55% da variabilidade nos dados, o que pode ser considerado um ajuste razoável.
Após essa etapa, procedemos à criação de um gráfico de dispersão para visualizar o ajuste do modelo de regressão com a linha ideal, utilizando valores reais e previsões. A análise do gráfico revela a presença de pontos próximos à linha zero, indicando previsões precisas, mas também a existência de pontos distantes, sugerindo possíveis desbalanceamentos ou falhas no modelo.
<br> 
![image](https://github.com/2023M8T4Inteli/grupo2/assets/99209712/019bb8f9-8761-483c-9bf1-bbe433b62381)<br> 
**Imagem X**: Gráfico de dispersão <br> 
**Fonte**: Elaboração própria <br> 


Subsequentemente, realizamos a plotagem de um gráfico de resíduos, visando identificar padrões nos erros do modelo. O eixo X representa os valores reais do conjunto de testes, o eixo Y representa as diferenças entre os valores reais e as previsões do modelo, e a linha horizontal vermelha (y=0) representa a linha zero. Observamos que os resíduos estão distribuídos aleatoriamente, mas a presença de pontos distantes da linha horizontal pode indicar desafios ou falhas.
<br> 
![image](https://github.com/2023M8T4Inteli/grupo2/assets/99209712/b4154f65-a939-4f3e-ac66-030fae2ad7d1) <br> 

**Imagem X**: Gráfico de resíduos <br> 
Fonte: Elaboração própria <br> 



Finalmente, criamos um histograma de resíduos para examinar a distribuição dos resíduos de maneira mais detalhada. O eixo X (resíduos) representa os diferentes valores dos resíduos, e o eixo Y (frequência) indica a frequência com que cada valor de resíduo ocorre. Espera-se uma forma de sino, indicando uma distribuição normal dos resíduos, mas a presença de outliers ou valores extremos pode sugerir problemas ou padrões no modelo. A interpretação cuidadosa desses gráficos é fundamental para compreender se o modelo está capturando efetivamente os padrões nos dados ou se há áreas de melhoria necessárias.
![image](https://github.com/2023M8T4Inteli/grupo2/assets/99209712/4fb7a12d-5bbc-48e9-8ce9-49b385a64132)<br> 

**Imagem X**: Gráfico de resíduos <br> 
**Fonte**: Elaboração própria <br> 


**IVM-NM** 

A análise do modelo para o Índice de Vulnerabilidade Municipal (IVM) foi conduzida com base nos critérios de sucesso definidos, visando compreender a eficácia na consecução dos objetivos do projeto.

O Modelo de Regressão, utilizando a técnica de Gradient Boosting, foi submetido a uma análise detalhada, empregando diversas métricas para avaliar sua capacidade de previsão do índice de vulnerabilidade municipal (IVM). Os resultados obtidos foram os seguintes: Mean Squared Error (MSE): 7.57; Root Mean Squared Error (RMSE): 2.75; Mean Absolute Error (MAE): 2.15; R-squared (R²): 0.59. 

Essas métricas proporcionam insights cruciais sobre a qualidade do modelo. O MSE, ao representar a média dos quadrados dos erros, indica que, em média, os quadrados dos erros são aproximadamente 7.57. O RMSE, sendo a raiz quadrada do MSE, interpreta que os erros médios são cerca de 2.75 unidades. O MAE, que é a média dos valores absolutos dos erros, revela que, em média, os erros são de aproximadamente 2.15 unidades. O R², ou coeficiente de determinação, sugere que o modelo explica cerca de 59% da variabilidade nos dados.

Posteriormente, foi realizada uma análise visual por meio do gráfico intitulado 'Ajuste do Modelo de Regressão (Gradient Boosting) com Linha Ideal'. Esse gráfico evidenciou que os pontos estão próximos da linha zero, indicando que, apesar da presença de valores extremos e outliers, muitos pontos estão bem ajustados ao modelo. A proximidade à linha zero sugere previsões precisas, enquanto a presença de valores distantes pode indicar desbalanceamento ou falhas no modelo.


![image](https://github.com/2023M8T4Inteli/grupo2/assets/99209712/aaf6e104-bb22-4f17-8ecc-19abff557189)<br> 

**Imagem X**: Ajuste do modelo de Regressão - Gradient Boosting <br> 
**Fonte**: Elaboração própria <br> 


Adicionalmente, foram gerados gráficos de resíduos e um histograma de resíduos utilizando o Gradient Boosting. O gráfico de resíduos possibilitou visualizar a diferença entre os valores reais e as previsões do modelo, destacando áreas de possível desbalanceamento. O histograma de resíduos, por sua vez, contribuiu para examinar a distribuição dos resíduos, identificando padrões ou outliers que podem indicar possíveis problemas no modelo. <br> 


![image](https://github.com/2023M8T4Inteli/grupo2/assets/99209712/90966f5b-4afe-4bdf-a994-e5065d561493)<br> 
**Imagem X**: Gráfico de resíduo - Gradient Boosting <br> 
**Fonte**: Elaboração própria <br> 

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99209712/31f37933-eea3-4417-a6da-cd4df384d637)<br> 
**Imagem X**: Gráfico de resíduo - Gradient Boosting <br> 
**Fonte**: Elaboração própria <br> 
<br>

## 6. Implementação e Deploy 

Este processo é conhecido por realizar a integração do modelo em ambiente de produção. A partir disso, compreendemos que com base nos dados que foram preparados, e modelados a partir dos algoritmos escolhidos, desenvolvemos um infográfico que servirá como uma forma de representarmos em um formato visual a partir do perfil esperado pelo nosso cliente, o que pode ser tomado como conclusão. 


# Avaliação e validação do modelo de Floresta Aleatória com o CRISP-DM

**Hiperparametrização do gradient boosting**
O objetivo do código a seguir é realizar a hiperparametrização do modelo de Regressão por Gradient Boosting para melhorar seu desempenho na previsão de um índice específico ("IVM-NM") com base em um conjunto de dimensões fornecidas.

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99209712/8d605e59-1a19-48ac-8da3-fdd263b92906)

Mean Squared Error (MSE): 6.961276826408555
Root Mean Squared Error (RMSE): 2.6384231704577936
Mean Absolute Error (MAE): 2.0661330444566675
R-squared (R²): 0.6207753914149101

# Carregamento e Preparação dos Dados
No início, são carregados os dados referentes às variáveis independentes (X) e à variável dependente (y). As features escolhidas incluem informações sobre moradia, acesso a serviços públicos, saúde, educação, acesso a serviços financeiros, padrão de vida, transporte e lazer.

# Divisão dos Dados
Os dados são divididos em conjuntos de treino e teste utilizando a função train_test_split da biblioteca scikit-learn. 80% dos dados são destinados ao treino, enquanto 20% são reservados para teste.

# Definição do Modelo RandomForestRegressor
O modelo de Regressão RandomForestRegressor é escolhido devido à sua capacidade de lidar com relações não-lineares e complexas nos dados. São definidos hiperparâmetros específicos para o modelo, como o número de estimadores (500), a profundidade máxima da árvore (30), e os critérios de divisão (min_samples_split=2, min_samples_leaf=1).

# Treinamento do Modelo
O modelo é treinado utilizando o conjunto de treino. Durante esse processo, o algoritmo ajusta os parâmetros internos da floresta de árvores de decisão para melhor se adaptar aos padrões nos dados.

# Predição e Avaliação
Após o treinamento, o modelo é utilizado para realizar predições no conjunto de teste. Em seguida, diversas métricas de avaliação são calculadas para avaliar o desempenho do modelo. Essas métricas incluem o Mean Squared Error (MSE), Root Mean Squared Error (RMSE), Mean Absolute Error (MAE) e o R-squared (R²).

# Resultados
Ao comparar os resultados obtidos anteriormente com a hiperparametrização, observamos melhorias nas métricas de avaliação. O MSE, RMSE e MAE diminuíram, indicando uma redução nos erros de previsão. Além disso, o R² aumentou, sugerindo uma melhor capacidade de explicar a variabilidade nos dados.

Esse processo de otimização é fundamental para ajustar o modelo de modo a alcançar o melhor desempenho possível para o problema em questão. Experimentações adicionais e ajustes finos podem ser realizados para buscar melhorias contínuas no modelo.

# Resultados Iniciais (Sem Hiperparametrização):
**Mean Squared Error (MSE)**: 7.42497
**Root Mean Squared Error (RMSE)**: 2.72488
**Mean Absolute Error (MAE)**: 2.06260
**R-squared (R²)**: 0.59552

# Resultados Após Hiperparametrização:

**Mean Squared Error (MSE)**: 6.96128
**Root Mean Squared Error (RMSE)**: 2.63842
**Mean Absolute Error (MAE)**: 2.06613
**R-squared (R²)**: 0.62078

# Análise Comparativa:

*MSE e RMSE:*
Houve uma melhoria significativa no MSE e RMSE após a hiperparametrização, indicando uma redução nos erros médios quadráticos e na dispersão dos resíduos. Isso sugere uma melhor precisão nas previsões.

*MAE:*
Embora tenha havido um ligeiro aumento no MAE após a hiperparametrização, a diferença é mínima. O MAE continua em um nível aceitável, indicando que os erros absolutos médios permanecem razoáveis.

*R-squared (R²):*
Houve um aumento no R² após a hiperparametrização, indicando uma melhoria na capacidade do modelo explicar a variabilidade nos dados. Este é um sinal positivo de melhor ajuste do modelo aos dados de teste.

# Considerações Finais:
A hiperparametrização é uma abordagem eficaz para otimizar o desempenho do modelo e ajustar seus parâmetros para um melhor ajuste aos dados. O Random Forest demonstrou melhorias significativas nas métricas após a hiperparametrização. A análise comparativa fornece insights sobre como as mudanças nos hiperparâmetros impactaram as métricas de avaliação do modelo Random Forest.
