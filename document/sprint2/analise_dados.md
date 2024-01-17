## Sumário

[1. IBGE Dados Abertos](#c1)

[2. POF (pesquisa orçamento familiar](#c2)

[3. RAIS e CAGED Microdados](#c3)

[4. Receita Federal Dados Abertos](#c4)

[5. Dados Abertos MEC](#c5)

[6. Dados Abertos INEP](#c6)

[7. Open Data SUS](#c7)

[8. From|to Zip Code to Lat-Long (all countries)](#c8)

<br>

# <a name="c1"></a>1. IBGE Dados Abertos

&emsp;&emsp; O Plano de Dados Abertos para o período de 2020-2022 é um guia que orienta a disponibilização, atualização e disseminação de informações abertas. Seu objetivo é promover a transparência, melhorar os serviços públicos e atender às necessidades da sociedade civil, permitindo o acesso aos dados publicados pela instituição. Para esse projeto, é utilizado um conjunto de dados, Produto Interno Bruto dos Municípios, disponibilizado que será descrito abaixo.

## 1.1 Tabela 5938 - Produto interno bruto a preços correntes, impostos, líquidos de subsídios, sobre produtos a preços correntes e valor adicionado bruto a preços correntes total e por atividade econômica, e respectivas participações

&emsp;&emsp; A estrutura desta tabela consiste em 3 valores: 1. Variável, que são as pequisas e seus valores, por exemplo: Produto interno bruto a preços correntes (47 pesquisas); 2. Ano, quando essa pequisa rodou no país (2002 - 2020); 3. Unidade Territorial, de onde você deseja ver a pesquisa, exemplo unidades federativas (6 opções). Abaixo, pode-se ver uma figura que demonstra a estrutura dos dados da Tabela 5938. 

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206636/a5ce38a7-bc69-41a4-9a56-bdf2e287f3f6)
Figura XX: Layout Tabela 5938
Fonte: Sidra IBGE

&emsp;&emsp; Diante de 47 pesquisas, o grupo acreditou que somente a "PIB a preços correntes (Mil Reais)" é relavante para o projeto, já que esta demonstra o valor total de bens e serviços produzidos em um país durante um determinado período, podendo avaliar o tamanho da economia desse país. Para isso, foi escolhido em cada valor: 1. Variável - **PIB a preços correntes (Mil Reais)**; 2. Ano - **2022**; 3. Unidade Territorial - **Unidade da Federação**. Os dados são: 

| Estado | Valor |
|------------|------------|
| Rondônia    | 51.598.741   | 
| Acre   | 16.476.371   | 
| Amazonas    | 116.019.139   | 
| Roraima | 16.024.276 |
|Pará | 215.935.604 |
|Amapá | 18.469.115 |
|Tocantis | 43.649.803|
|Maranhão | 106.915.962|
|Piauí | 56.391.257|
|Ceará | 166.914.536|
|Rio Grande do Norte | 71.577.107|
|Paraíba | 70.292.034|
|Pernambuco | 193.307.317|
|Alagoas | 63.202.349|
|Sergipe | 45.409.657|
|Bahia | 305.320.813|
|Minas Gerais | 682.786.116|
|Espirito Santo | 138.445.922|
|Rio de Janeiro | 753.823.711|
|São Paulo | 2.377.638.980|
|Paraná | 487.930.594|
|Santa Catarina | 349.275.016|
|Rio Grande do Sul | 470.941.846|
|Mato Grosso do Sul | 122.627.726|
|Mato Grosso | 178.649.564|
|Goiás | 224.126.112|
|Distrito Federal | 265.847.334|
<br>
Tabela XX: Dados PIB a preços correntes (Mil Reais) <br>
Fonte: IBGE

&emsp;&emsp; Além disso, foi realizado um tratamento dos dados para o PIB de todos os municípios em todos os anos (2002-2020). Assim, os valores são os seguintes: 1. Variável - **PIB a preços correntes (Mil Reais)**; 2. Ano - **Todos os anos disponíveis (2002-2020)**; 3. Unidade Territorial - **Município**. Para o tratamento, foi necessária a criação de um Notebook, onde os dados foram lidos e os valores nulos foram removidos, como mostram os códigos abaixo. Além disso, no momento de _download_ é necessário entrar no arquivo e excluir o título.

```
tabela = pd.read_csv('tabela5938.csv', delimiter=';')

tabela_sem_nan = tabela.dropna()
```

## 1.2 Tabela 5939 - Índice de Gini do produto interno bruto a preços correntes e do valor adicionado bruto a preços correntes por atividade econômica

&emsp;&emsp; A segunda tabela escolhida foi a do índice de Gini, que avalia a desigualdade na distribuição de renda ou riqueza. Este índice varia de 0 a 1, sendo que valores mais próximos de 0 indicam menor desigualdade. Esta tabela segue o mesmo layout anteriormente explicado. 

&emsp;&emsp; Diante de 5 pesquisas, o grupo acreditou que 2 delas são relavantes para o projeto: 1."Índice de Gini da distribuição do produto interno bruto a preços correntes" e 2."Índice de Gini da distribuição do valor adicionado bruto a preços correntes da indústria". O primeiro avalia esta desigualdade pela distribuição da renda ou riqueza no contexto de toda a economia de um país, já o segundo se concentra especificamente na desigualdade dentro do setor industrial do país. Já que o projeto foca em um setor específico, estes dados podem ajudar. Para isso, foi escolhido em cada valor: 1. Variável - **Índice de Gini da distribuição do produto interno bruto a preços correntes ou Índice de Gini da distribuição do valor adicionado bruto a preços correntes da indústria**; 2. Ano - **2022**; 3. Unidade Territorial - **Unidade da Federação**. Os dados são: 

_**Índice de Gini da distribuição do produto interno bruto a preços correntes**_
| Estado | Valor |
|------------|------------|
|Rondônia | 0,69 |
|Acre | 0,69 |
|Amazonas | 0,86|
|Roraima | 0,72|
|Pará | 0.74|
|Amapá | 0.75|
|Tocantis | 0,69|
|Maranhão | 0,71|
|Piauí | 0,74|
|Ceará | 0,76|
|Rio Grande do Norte | 0,77|
|Paraíba | 0,77|
|Pernambuco | 0,77|
|Alagoas | 0,69|
|Sergipe | 0,71|
|Bahia | 0,76|
|Minas Gerais | 0,80 |
|Espirito Santo | 0,75|
|Rio de Janeiro | 0,81|
|São Paulo | 0,86|
|Paraná | 0,75|
|Santa Catarina | 0,75|
|Rio Grande do Sul | 0,77|
|Mato Grosso do Sul | 0,65|
|Mato Grosso | 0,68|
|Goiás | 0,77| 
<br>
Tabela XX: Índice de Gini - Geral <br>
Fonte: IBGE
<br>

_**Índice de Gini da distribuição do valor adicionado bruto a preços correntes da indústria**_

| Estado | Valor |
|------------|------------|
|Rondônia | 0,86 |
|Acre | 0,80|
|Amazonas | 0,96|
|Roraima | 0,83|
|Pará | 0.92|
|Amapá | 0.72|
|Tocantis | 0,84|
|Maranhão | 0,90|
|Piauí | 0,86|
|Ceará | 0,87|
|Rio Grande do Norte | 0,85|
|Paraíba | 0,89|
|Pernambuco | 0,88|
|Alagoas | 0,86|
|Sergipe | 0,84|
|Bahia | 0,89|
|Minas Gerais | 0,88 |
|Espirito Santo | 0,80|
|Rio de Janeiro | 0,83|
|São Paulo | 0,84|
|Paraná | 0,86|
|Santa Catarina | 0,77|
|Rio Grande do Sul | 0,84|
|Mato Grosso do Sul | 0,79|
|Mato Grosso | 0,77|
|Goiás | 0,84|
<br>
Tabela XX: Índice de Gini - Indústria <br>
Fonte: IBGE

# <a name="c2"></a>2. Pesquisa de orçamento familiar (POF)
Os dados que serão analisados nesse documento são de caráter experimental, tendo em vista que tratam-se de novas estatísticas que ainda estão em fase de teste e sob avaliação.

**Fonte dos dados:** IBGE, Diretoria de Pesquisas, Coordenação de Pesquisas por Amostra de Domicílios, Pesquisa de Orçamentos Familiares.

**Formato:** xls e ods

**Tamanho:** o tamanho médio das tabelas de 2008-2009 é de 176 KB.

O tamanho médio das tabelas de 2017-2018 é de 176 KB.

**Frequência de atualização de cada fonte:** nos sites oficiais não foi possível encontrar uma data específica para a ocorrência de cada uma das pesquisas, principalmente porque se tratam de dados experimentais. Contudo, foi possível encontrar o tempo de duração da pesquisa (12 meses) e o tempo previsto entre o início da coleta e a divulgação dos dados (18 meses).

## 2.1 Tabelas 2017 - 2018

Abaixo encontram-se as descrições detalhadas e exemplificações com imagens de cada uma das tabelas encontradas na fonte de dados enviada. 

- **Tabela 1b:** a tabela em questão apresenta dados resumidos acerca da proporção de pessoas das famílias residentes, da proporção de pessoas com algum grau de vulnerabilidade, do índice de vulnerabilidade multidimensional não monetário e contribuições para o índice de vulnerabilidade multidimensional não monetário do Brasil segundo os condicionantes e subgrupos selecionados.
  
![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206817/9220b5f9-32de-438c-bfb6-4e6b89e7ea72)

Imagem 1: Tabela 1b - Proporção de pessoas das famílias residentes, proporção de pessoas com algum grau de vulnerabilidade, IVM-NM e contribuições para o IVM-NM do Brasil, segundo os condicionantes e subgrupos selecionados-período 2017-2018 <br>
Fonte: POF 2017 - 2018

---
- **Tabela 2b:** a tabela em questão apresenta dados resumidos acerca da proporção de pessoas das famílias residentes, da proporção de pessoas com algum grau de pobreza, do  Índice de Pobreza Multidimensional não Monetário do Brasil segundo os condicionantes e subgrupos selecionados.
  
![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206817/c358583f-5aa7-4b08-a86f-b89fe7e5158c)

Imagem 2: Tabela 2b - Proporção de pessoas das famílias residentes, proporção de pessoas com algum grau de pobreza, IPM-NM e contribuições para o IPM-NM do Brasil, segundo os condicionantes e subgrupos selecionados-período 2017-2018 <br>
Fonte: POF 2017 - 2018

---
- **Tabela 3b:** a tabela em questão apresenta dados resumidos acerca do índice de vulnerabilidade multidimensional não monetário, do efeito marginal e da contribuição para a soma dos efeitos marginais, segundo as dimensões selecionadas. 

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206817/524d4e08-b728-47c8-83c3-a9f96564573c)

Imagem 3: Tabela 3b - Índice de Vulnerabilidade Multidimensional não Monetário, efeito marginal e contribuição para a soma dos efeitos marginais, segundo as dimensões selecionadas - Brasil - período 2017-2018 <br>
Fonte: POF 2017 - 2018

---
- **Tabela 4b:** a tabela em questão apresenta o índice de pobreza multidimensional não monetário, efeito marginal e contribuição para a soma dos efeitos marginais, segundo as dimensões selecionadas.<br>
Fonte: POF 2017 - 2018

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206817/88625e9b-357e-40de-8528-15b0f6ec9567)

Imagem 4: Tabela 4b - Índice de Pobreza Multidimensional não Monetário, efeito marginal e contribuição para a soma dos efeitos marginais, segundo as dimensões selecionadas - Brasil - período 2017-2018 <br>
Fonte: POF 2017 - 2018

---
- **Tabela 5b:** a tabela em questão apresenta dados acerca da proporção de pessoas das famílias residentes, da proporção de pessoas com algum grau de vulnerabilidade, do índice de Vulnerabilidade Multidimensional não Monetário e contribuição para o total dos efeitos marginais no  Índice de Vulnerabilidade Multidimensional não Monetário, por tipo de dimensão, segundo as unidades de federação.  

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206817/d09dce51-680d-4461-a09d-d24317895241)

Imagem 5: Tabela 5b - Proporção de pessoas das famílias residentes, proporção de pessoas com algum grau de Vulnerabilidade, IVM-NM e contribuição para o total dos efeitos marginais no IVM-NM, por tipo de dimensão, segundo as Unidades da Federação - período 2017-2018 <br>
Fonte: POF 2017 - 2018

---
- **Tabela 6b:** a tabela em questão apresenta dados acerca da proporção de pessoas das famílias residentes, da proporção de pessoas com algum grau de pobreza, do Índice de Pobreza Multidimensional não Monetário e contribuição para o total dos efeitos marginais no Índice de Pobreza Multidimensional não Monetário, por tipo de dimensão, segundo as unidades da federação. 

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206817/afaf6e52-2878-4767-b303-7f3b240301c6)

Imagem 6: Tabela 6b - Proporção de pessoas das famílias residentes, proporção de pessoas com algum grau de pobreza, IPM-NM e contribuição para o total dos efeitos marginais no IPM-NM, por tipo de dimensão, segundo as Unidades da Federação - período 2017-2018 <br>
Fonte: POF 2017 - 2018

---
- **Tabela 7b:** a tabela em questão apresenta a proporção de pessoas das famílias residentes, do Índice de Pobreza Multidimensional com Componente Relativo e contribuições para o Índice de Pobreza Multidimensional com Componente Relativo do Brasil, segundo os condicionantes e subgrupos selecionados.

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206817/2f833457-6c98-402a-af4f-2da6d45dc438)

Imagem 7: Tabela 7b - Proporção de pessoas das famílias residentes, IPM-CR e contribuições para o IPM-CR do Brasil, segundo os condicionantes e subgrupos selecionados - período 2017-2018 <br>
Fonte: POF 2017 - 2018

---
- **Tabela 8b:** a tabela em questão apresenta o índice de pobreza multidimensional, com componente relativo, efeito marginal e contribuição para a soma dos efeitos marginais, segundo as dimensões selecionadas.

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206817/45820820-a639-4f49-8a24-f0fb91c62707)

Imagem 8: Tabela 8b - Índice de Pobreza Multidimensional com Componente Relativo, efeito marginal e contribuição para a soma dos efeitos marginais, segundo as dimensões selecionadas - Brasil - período 2017-2018 <br>
Fonte: POF 2017 - 2018

---
- **Tabela 9b:** a tabela em questão apresenta a proporção de pessoas das famílias residentes, o Índice de Pobreza Multidimensional com Componente Relativo e contribuição para o total dos efeitos marginais do Índice de Pobreza Multidimensional com Componente Relativo, por tipo de dimensão, segundo as unidades da federação.

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206817/f69ba9b8-303e-4949-89be-2ad2f5b510c1)

Imagem 9: Tabela 9b - Proporção de pessoas das famílias residentes, IPM-CR e contribuição para o total dos efeitos marginais no IPM-CR, por tipo de dimensão, segundo as Unidades da Federação - período 2017-2018 <br>
Fonte: POF 2017 - 2018


## 2.2 Tabelas 2008 - 2009:


- **Tabela 1b:** a tabela em questão apresenta dados resumidos acerca da proporção de pessoas das famílias residentes, da proporção de pessoas com algum grau de vulnerabilidade, do índice de vulnerabilidade multidimensional não monetário e contribuições para o índice de vulnerabilidade multidimensional não monetário do Brasil segundo os condicionantes e subgrupos selecionados. 

- **Tabela 2b:** a tabela em questão apresenta dados resumidos acerca da proporção de pessoas das famílias residentes, da proporção de pessoas com algum grau de pobreza, do  Índice de Pobreza Multidimensional não Monetário do Brasil segundo os condicionantes e subgrupos selecionados.

- **Tabela 3b:** a tabela em questão apresenta dados resumidos acerca do índice de vulnerabilidade multidimensional não monetário, do efeito marginal e da contribuição para a soma dos efeitos marginais, segundo as dimensões selecionadas. 

- **Tabela 4b:** a tabela em questão apresenta o índice de pobreza multidimensional não monetário, efeito marginal e contribuição para a soma dos efeitos marginais, segundo as dimensões selecionadas.

- **Tabela 5b:** a tabela em questão apresenta dados acerca da proporção de pessoas das famílias residentes, da proporção de pessoas com algum grau de vulnerabilidade, do índice de Vulnerabilidade Multidimensional não Monetário e contribuição para o total dos efeitos marginais no  Índice de Vulnerabilidade Multidimensional não Monetário, por tipo de dimensão, segundo as unidades de federação.  

- **Tabela 6b:** a tabela em questão apresenta dados acerca da proporção de pessoas das famílias residentes, da proporção de pessoas com algum grau de pobreza, do Índice de Pobreza Multidimensional não Monetário e contribuição para o total dos efeitos marginais no Índice de Pobreza Multidimensional não Monetário, por tipo de dimensão, segundo as unidades da federação. 

- **Tabela 7b:** a tabela em questão apresenta a proporção de pessoas das famílias residentes, do Índice de Pobreza Multidimensional com Componente Relativo e contribuições para o Índice de Pobreza Multidimensional com Componente Relativo do Brasil, segundo os condicionantes e subgrupos selecionados.

- **Tabela 8b:** a tabela em questão apresenta o índice de pobreza multidimensional, com componente relativo, efeito marginal e contribuição para a soma dos efeitos marginais, segundo as dimensões selecionadas.

- **Tabela 9b:** a tabela em questão apresenta a proporção de pessoas das famílias residentes, o Índice de Pobreza Multidimensional com Componente Relativo e contribuição para o total dos efeitos marginais do Índice de Pobreza Multidimensional com Componente Relativo, por tipo de dimensão, segundo as unidades da federação. 

Fonte para maiores esclarecimentos: [IBGE - Orçamento familiar: pesquisa de orçamentos familiares](https://ces.ibge.gov.br/apresentacao/portarias/200-comite-de-estatisticas-sociais/base-de-dados/1145-pesquisa-de-orcamentos-familiares.html).  

# <a name="c3"></a>3. RAIS e CAGED Microdados

Microdados da RAIS (Relação Anual de Informações Sociais) e do CAGED (Cadastro Geral de Empregados e Desempregados) são conjuntos de informações detalhadas sobre o emprego formal no Brasil. A RAIS coleta dados anuais, incluindo informações sobre empregados, utilizados para estatísticas e controle de benefícios. O CAGED registra admissões e demissões de trabalhadores com carteira assinada, sendo essencial para análises do mercado de trabalho e políticas públicas. Ambos fornecem uma visão detalhada da dinâmica do emprego no país. Esse critério pode ser utilizado para especular o potencial de consumo em cada região do Brasil. 
<br>
<br>
Os dados disponibilizados são anuais, começando em 1985 até 2016.
<br>
<br>
Todos os estados brasileiros são contemplados nessa análise
<br>
<br>
Os critérios e colunas são diversos, voltados para caracterizar o trabalhor/desempregado brasileiro
<br>
![image](https://github.com/2023M8T4Inteli/grupo2/assets/99208815/227cd19a-a6d1-4f02-9b6c-8eed2b7350fa)

# <a name="c4"></a>4. Receita Federal Dados Abertos

Para o objetivo do projeto, dos dados disponibilizados pelo site do governo na seção da receita federal (Dados da Receita Federal), os dados que fazem mais sentido para a ingestão são aqueles referentes à distribuição de renda. Essa escolha se baseia exatamente na necessidade do cliente de examinar o mercado consumidor de alimentos ao longo do Brasil e avaliar em qual região há um maior potencial consumidor. No caso específico das bases, essa análise do mercado consumidor se basearia no parâmetro do poder aquisitivo percebido por meio da distribuição de renda.
<br>
<br>
Tabela distribuicao-renda.csv :
<br>
  -Linhas: 46350
<br>
  -Colunas: 24
<br>
<br>
Tabela distribuicao-renda-socios.csv :
<br>
  -Linhas: 46350
<br>
  -Colunas: 24
<br>
<br>
Tabela distribuicao-renda-socios-exclusiva.csv :
<br>
  -Linhas: 46350
<br>
  -Colunas: 24
<br>
<br>
Fonte: https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/dados-abertos
<br>
# <a name="c5"></a>5. Dados Abertos MEC

O Programa Universidade para Todos (Prouni) do Ministério da Educação do Brasil oferece bolsas de estudo em instituições de ensino superior privadas. Os dados abertos do Prouni incluem informações detalhadas sobre as bolsas concedidas, perfis dos beneficiários, instituições de ensino participantes e outros dados relevantes. Os conjuntos de dados abrangem os anos de 2016 a 2020 e estão disponíveis em formato CSV.

## 5.1 Descrição dos Conjuntos de Dados

Os dados do Prouni oferecem uma visão ampla sobre a distribuição de bolsas de estudo no ensino superior privado no Brasil. Esses dados são cruciais para compreender as tendências educacionais, demográficas e socioeconômicas.

### Tabela de Relevância dos Dados do Prouni

| Relevância | Nome do Conjunto   | Tipo de Arquivo |
|------------|--------------------|-----------------|
| Alta       | Dados do Prouni 2016 | .CSV           |
| Alta       | Dados do Prouni 2017 | .CSV           |
| Alta       | Dados do Prouni 2018 | .CSV           |
| Alta       | Dados do Prouni 2019 | .CSV           |
| Alta       | Dados do Prouni 2020 | .CSV           |

## 5.2 Dados Relevantes para Análises Estratégicas

- **Distribuição Regional de Bolsas:** Informações sobre a localização geográfica dos beneficiários, incluindo estado e município, podem indicar áreas com maior potencial de mercado e poder de compra.
- **Perfil Demográfico e Socioeconômico:** Dados sobre sexo, raça, idade e tipo de bolsa (integral ou parcial) dos beneficiários fornecem insights sobre a diversidade e o perfil socioeconômico dos estudantes.

## 5.3 Potencial de Uso dos Dados

Os dados do Prouni são uma fonte valiosa para análises de mercado, desenvolvimento de políticas educacionais e estratégias de marketing. Eles podem ser utilizados para:

- Identificar regiões com alta demanda por educação superior e potencial de mercado para produtos e serviços relacionados.
- Compreender o perfil dos estudantes beneficiários para campanhas de marketing direcionadas.
- Avaliar as tendências do mercado educacional e adaptar estratégias de negócios de acordo.

## 5.4 Análises e Insights dos Dados do Prouni

A análise dos dados do Prouni revela várias tendências e padrões significativos que são cruciais para o entendimento do mercado educacional brasileiro e para o desenvolvimento de estratégias de marketing eficazes.

### 5.4.1 Distribuição Regional de Bolsas

- **Gráfico 1: Distribuição de Bolsas por Região e Estado**
- ![image](https://github.com/2023M8T4Inteli/grupo2/assets/68927480/0919d123-7f7e-4658-8284-0fda4835be82)

  - *Insight:* A distribuição desigual de bolsas entre as regiões e estados brasileiros indica áreas com maior concentração de estudantes beneficiados pelo Prouni.
  - *Aplicação Estratégica:* Identificar estados e regiões-chave para campanhas de marketing direcionadas, desenvolvimento de produtos específicos e parcerias com instituições locais.

### 5.4.2 Perfil dos Beneficiários

- **Gráfico 2: Modalidade de Ensino, Tipo de Bolsa, Raça e Sexo dos Beneficiários**
- ![image](https://github.com/2023M8T4Inteli/grupo2/assets/68927480/133663a8-faa6-40cf-917a-6be210434164)

  - *Insight:* A análise do perfil dos beneficiários mostra a proporção de estudantes em cursos presenciais versus EAD, tipos de bolsa (integral ou parcial), distribuição racial e de gênero.
  - *Aplicação Estratégica:* Desenvolver estratégias de marketing inclusivas e diversificadas que atendam às necessidades de um público variado.

 ### 5.4.3 Descrição dos dados

**Índices e Descrições:**

Cada arquivo CSV contém várias colunas (ou índices), cada uma representando um tipo específico de informação. Aqui está uma descrição de alguns dos índices chave:

- ANO_CONCESSAO: Ano em que a bolsa foi concedida.
- CODIGO_EMEC_IES: Código de identificação da instituição de ensino superior.
- NOME_IES: Nome da instituição de ensino superior.
- MUNICIPIO: Município da instituição de ensino.
- TIPO_BOLSA: Tipo da bolsa concedida (integral ou parcial).
- MODALIDADE_ENSINO: Modalidade do curso (presencial ou EAD).
- NOME_CURSO: Nome do curso para o qual a bolsa foi concedida.
- NOME_TURNO_CURSO: Turno do curso.
- CPF_BENEFICIARIO: CPF do beneficiário (anonimizado).
- SEXO_BENEFICIARIO: Sexo do beneficiário.
- RACA_BENEFICIARIO: Raça declarada pelo beneficiário.
- DATA_NASCIMENTO: Data de nascimento do beneficiário.
- BENEFICIARIO_DEFICIENTE_FISICO: Indica se o beneficiário é deficiente físico.
- REGIAO_BENEFICIARIO: Região do beneficiário.
- UF_BENEFICIARIO: Unidade Federativa do beneficiário.
- MUNICIPIO_BENEFICIARIO: Município de residência do beneficiário.

**Quantidade de Dados:**

Os dados são extensos e oferecem uma visão abrangente do programa Prouni ao longo dos anos mencionados. Abaixo está a quantidade de registros (linhas) e variáveis (colunas) em cada ano:

- 2016: O dataset contém 239.262 registros e 15 colunas.
- 2017: O dataset contém 236.636 registros e 15 colunas.
- 2018: O dataset contém 241.032 registros e 15 colunas.
- 2019: O dataset contém 241.032 registros e 15 colunas.
- 2020: O dataset contém 166.830 registros e 17 colunas.

## 5.5 Considerações Finais

A análise detalhada dos dados do Prouni oferece uma visão abrangente do setor educacional privado no Brasil. As informações obtidas são indispensáveis para organizações que buscam compreender melhor o mercado educacional, desenvolver e implementar estratégias de go-to-market focadas e bem-sucedidas.


# <a name="c6"></a>6. Dados Abertos INEP

## 6.1 ANA - Avaliação Nacional de Alfabetização

&emsp;&emsp; A Avaliação Nacional de Alfabetização, também conhecida como ANA, é uma ferramenta de avaliação utilizada no contexto educacional brasileiro para medir o nível de alfabetização e letramento de crianças em séries do ensino fundamental. Para a educação, esses dados são utilizados para acompanhar o progresso dos estudantes e para a formulação de políticas públicas e a tomada de decisões em relação ao sistema educacional, direcionando recursos e esforços para aprimorar a qualidade.

&emsp;&emsp; Para o projeto, esse dado pode ser utilizado pensando na compreensão do mercado, como a compreensão do nível de educação dos consumidores pode ajudar a adaptar estratégias de marketing e etiquetagem de produtos. Além disso, podemos cruzar as informações para compreender como a alfabetização numérica afeta as decisões de compra e consumo, e com isso ajudar na previsão de tendências de mercado e no desenvolvimento de estratégias de vendas mais eficientes.

No site do INEP, os únicos dados disponibilizados são de 2014 e 2016 e esses dois são utilizados no projeto. 

Data Summary - 2014
| dataframe | values | 
|------------|------------|
| Qnt de linhas | 49357 | 
| Qnt de colunas | 46 |
<br>
Tabela XX: Informações sobre os dados - ANA <br>
Fonte: INEP

Data Types - 2014
| Tipo de coluna | Contagem | 
|------------|------------|
| float64   | 33 | 
| int64 | 13 |
<br>
Tabela XX: Informações sobre os dados - ANA <br>
Fonte: INEP

Data Summary - 2016
| dataframe | values | 
|------------|------------|
| Qnt de linhas | 48717 | 
| Qnt de colunas | 46 |
<br>
Tabela XX: Informações sobre os dados - ANA <br>
Fonte: INEP

Data Types - 2016
| Tipo de coluna | Contagem | 
|------------|------------|
| float64   | 33 | 
| int64 | 13 |
<br>
Tabela XX: Informações sobre os dados - ANA <br>
Fonte: INEP

## 6.2 Censo da Educação Superior

&emsp;&emsp; O Censo da Educação Superior é uma pesquisa anual que tem como objetivo a coleta dos dados abrangentes sobre instituições de ensino superior, estudantes, cursos e programas acadêmicos em todo o território nacional. Esses dados são importantes para identificar tendências e preferências alimentares em diferentes grupos demográficos. Por exemplo, alunos de cursos relacionados à saúde podem preferir opções alimentares mais saudáveis. Além disso, é comprovado que pessoas formadas em algum curso da educação superior tem um maior poder de compra, então o setor alimentício se favorece com essas regiões. Foram selecionados os dados do IES, de 2009 até 2022. Abaixo, segue uma tabela demonstrando um dataframe.

Data Summary - 2022
| dataframe | values | 
|------------|------------|
| Qnt de linhas | 2595 | 
| Qnt de colunas | 81 |
<br>
Tabela XX: Informações sobre os dados - Educação Superior <br>
Fonte: INEP

Data Types - 2022
| Tipo de coluna | Contagem | 
|------------|------------|
| int64   | 33 | 
| string  | 13 |
| float64 | 1 |
<br>
Tabela XX: Informações sobre os dados - Educação Superior <br>
Fonte: INEP


## 6.3 ENCEJA

&emsp;&emsp; O Encceja, ou Exame Nacional para Certificação de Competências de Jovens e Adultos, é um exame brasileiro que certifica a conclusão do Ensino Fundamental ou Médio para jovens e adultos que não tiveram oportunidade de concluir seus estudos na idade apropriada. Para o projeto, esses dados podem ser utilizados para identificar tendências e preferências alimentares em diferentes grupos demográficos. Foi selecionado os dados de 3 anos diferentes, 2014, 2020 e 2022.


# <a name="c7"></a>7. Open Data SUS

O DATASUS disponibiliza 31 conjuntos de dados coletados e fornecidos pelo Ministério da Saúde, acessíveis através do link [DATASUS - OpenDataSUS](https://opendatasus.saude.gov.br/). Esses conjuntos de dados abrangem uma variedade de informações relacionadas à saúde da população brasileira, incluindo dados recentes e antigos. Nos próximos tópicos, exibe-se detalhes sobre esses conjuntos de dados, suas especificações e quais deles têm relevância para o projeto.

## 7.1 Descrição dos conjuntos

O DATASUS disponibiliza uma variedade de informações relacionadas à saúde, que podem ser úteis para entender os padrões de consumo de alimentos. No entanto, nem todos esses dados são igualmente relevantes para o nosso projeto. A seguir, apresentamos uma tabela dos conjuntos de dados do DATASUS, classificando-os com sua relevância para a análise de consumo alimentício. A classificação foi feita considerando a relação direta ou indireta entre os dados e o comportamento de consumo alimentar. Além disso, indicamos os tipos de arquivo associados a cada conjunto de dados para facilitar a sua identificação e acesso. 


| Relevância  | Nome do Conjunto                                                                                             | Tipo de Arquivo               |
|-------------|---------------------------------------------------------------------------------------------------------------|------------------------------|
| Menos       | SISAGUA - Vigilância em Parâmetros Básicos e outras fontes relacionadas à qualidade da água                   | .PDF .CSV                    |
| Menos       | SRAG - Banco de Dados de Síndroma Respiratória Aguda Grave                                                    | .PDF API .CSV                |
| Menos       | Febre Amarela em humanos e primatas não-humanos                                                               | .CSV                         |
| Relevante   | Notificações de Síndrome Gripal                                                                             | .CSV                         |
| Relevante   | Campanha Nacional de Vacinação contra Covid                                                                 | .PDF .CSV                    |
| Relevante   | Registro de Ocupação Hospitalar COVID                                                                       | .PDF .CSV                    |
| Relevante   | SRAG 2021 a 2023 - Banco de Dados de Síndrome Respiratória Aguda Grave (incluindo dados da COVID-19)         | .PDF .CSV                    |
| Relevante   | Sistema de Informação sobre Nascidos Vivos – Sinasc                                                          | .PDF .CSV                    |
| Relevante   | Sistema de Informação sobre Mortalidade – SIM                                                                | .PDF .CSV                    |
| Relevante   | Unidades Básicas de Saúde - UBS                                                                             | .PDF .CSV                    |
| Relevante   | CNES - Cadastro Nacional de Estabelecimentos de Saúde                                                        | .PDF .CSV                    |
| Relevante   | Notificações de Síndrome Gripal                                                                             | .PDF API                     |
| Relevante   | Notificações de Síndrome Gripal                                                                             | .ODT ZIP                    |
| Relevante   | Sistema de Atenção à Saúde Indígena (SIASI) - Módulo de Vigilância Alimentar e Nutricional (VAN)            | .ODT ZIP                    |
| Relevante   | Notificações de Síndrome Gripal - API ElasticSearch                                                          | .ODT ZIP                    |
| Menos       | SISAGUA - Vigilância Parâmetros Básicos                                                                     | .ODT ZIP                    |
| Menos       | SISAGUA - Controle Semestral                                                                                | .ODT ZIP                    |
| Menos       | SISAGUA - Vigilância - Demais parâmetros                                                                     | .ODT ZIP                    |
| Menos       | SISAGUA - Controle Mensal - Parâmetros básicos                                                               | .ODT ZIP                    |
| Menos       | SISAGUA - Vigilância - Cianobactérias e cianotoxinas                                                         | .ODT ZIP                    |
| Menos       | SISAGUA - Controle mensal - demais parâmetros                                                                | ZIP                          |
| Menos       | SISAGUA - Controle Mensal - Infraestrutura Operacional                                                       | .ODT ZIP                    |
| Menos       | SISAGUA - Controle mensal - Amostras fora do padrão                                                          | .ODT ZIP                    |
| Relevante   | Unidades Básicas de Saúde - UBS                                                                             | .PDF ZIP                     |
| Relevante   | CNES - Cadastro Nacional de Estabelecimentos de Saúde                                                        | API ZIP                      |
| Menos       | SISAGUA - População Abastecida                                                                              | .ODT ZIP                    |
| Menos       | Sistema de Vigilância Alimentar e Nutricional - SISVAN                                                        | .PDF API ZIP .CSV            |
| Menos       | SRAG 2020 - Banco de Dados de Síndrome Respiratória Aguda Grave - incluindo dados da COVID-19                | .PDF .CSV                    |
| Menos       | SISAGUA - Pontos de captação                                                                                | .CSV .ODT ZIP                |
| Menos       | Febre Amarela em humanos e primatas não-humanos                                                               | .PDF .CSV                    |
| Menos       | SRAG - Banco de Dados de Síndroma Respiratória Aguda Grave                                                    | .PDF .CSV                    |
| Menos       | SRAG - Banco de Dados de Síndrome Respiratória Aguda Grave                                                     | .PDF .CSV                    |
| Menos       | SRAG - Banco de Dados de Síndrome Respiratória Aguda Grave                                                     | .PDF .CSV                    |



## 7.2 Dados menos relevantes para análise de consumo alimentício

- **SISAGUA -** Vigilância em Parâmetros Básicos e outras fontes relacionadas à qualidade da água: Embora a qualidade da água seja importante para a saúde pública, esses dados podem ter uma influência indireta no consumo alimentar.

- **SRAG -** Banco de Dados de Síndroma Respiratória Aguda Grave: Se você já está usando os dados mais recentes da SRAG, essas versões anteriores podem não ser necessárias para a análise de consumo alimentar.

- **Febre Amarela em humanos e primatas não-humanos:** A febre amarela é uma doença transmitida por mosquitos e não está diretamente relacionada ao consumo de alimentos.

## 7.3 Dados relevantes para análise de consumo alimentício

- **Notificações de Síndrome Gripal:** Esses dados podem indicar surtos de doenças semelhantes à gripe em diferentes regiões, o que pode ser um indicativo de problemas de saúde na população. A ocorrência de surtos de doenças gripais pode afetar o comportamento do consumidor, levando a mudanças nos padrões de compra e consumo de alimentos, como maior demanda por alimentos saudáveis e suplementos vitamínicos.

- **Campanha Nacional de Vacinação contra Covid:** O sucesso das campanhas de vacinação contra a COVID-19 em diferentes áreas pode influenciar a confiança da população na segurança de sair e consumir alimentos fora de casa, como em restaurantes. Uma alta taxa de vacinação pode levar a uma maior sensação de segurança e estimular o consumo em estabelecimentos alimentícios.

- **Registro de Ocupação Hospitalar COVID:** Se os hospitais estiverem sobrecarregados, as pessoas podem optar por evitar locais com aglomerações, como restaurantes e bares, impactando o consumo nesses estabelecimentos.

- **SRAG 2021 a 2023 -** Banco de Dados de Síndrome Respiratória Aguda Grave (incluindo dados da COVID-19): O aumento dos casos de SRAG, especialmente os graves, pode resultar em medidas de isolamento e restrições de movimento, afetando o comportamento de consumo, como o aumento do uso de serviços de entrega de alimentos.

- **Sistema de Informação sobre Nascidos Vivos – Sinasc:** O aumento na taxa de nascimentos pode indicar uma necessidade de planejamento de suprimentos alimentícios nas áreas onde a população está crescendo rapidamente (demanda por alimentos em escolas, creches e outras instituições.)

- **Sistema de Informação sobre Mortalidade – SIM:** Os dados de mortalidade podem fornecer informações sobre as principais causas de morte em diferentes regiões, incluindo doenças relacionadas à dieta, como doenças cardiovasculares e diabetes.

- **Unidades Básicas de Saúde - UBS:** 
  - **Acesso a Alimentos Saudáveis:** Quando as UBS estão ausentes ou insuficientes em uma região, as pessoas podem enfrentar dificuldades no acesso a cuidados de saúde e, indiretamente, a informações sobre práticas de alimentação saudável.
  - **Desertos Alimentares:** A falta de UBS em uma área pode indicar uma possível carência de infraestrutura de saúde e, por extensão, a presença de desertos alimentares. Os desertos alimentares são áreas onde os residentes têm dificuldade em acessar alimentos frescos e saudáveis devido à falta de supermercados ou lojas que ofereçam esses produtos.

- **CNES -** Cadastro Nacional de Estabelecimentos de Saúde: Esses dados podem fornecer informações sobre a disponibilidade de serviços de saúde em diferentes áreas, que estão diretamente ligados ao acesso da população a cuidados de saúde.

## 7.4 Dados carregados na AWS S3

Os dados provenientes do Sistema Único de Saúde (SUS), constituem uma fonte rica sobre a saúde no Brasil. Esses conjuntos abrangem informações hospitalares, natalidade e vigilância epidemiológica, oferecendo uma perspectiva abrangente ao longo do tempo. Abordaremos detalhes de cada conjunto para destacar suas característicass.

### 7.4.1 Hospitais e Leitos - 2007 a 2023

Este conjunto de dados fornece informações sobre estabelecimentos hospitalares, leitos gerais e complementares, incluindo dados de contato, como endereço, telefone e e-mail. Os arquivos são disponibilizados mensal e anualmente. É importante destacar que, para garantir a conformidade com a Lei de Acesso à Informação e a Lei Geral de Proteção de Dados, os dados são divulgados de forma agregada, preservando o sigilo das informações pessoais. A seguir, apresenta-se o glossário dos dados:

| NOME DO CAMPO           | TIPO         | NOME DO CAMPO           | TIPO         | DESCRIÇÃO                                                 | DOMÍNIOS                                                |
|-------------------------|--------------|-------------------------|--------------|-----------------------------------------------------------|---------------------------------------------------------|
| COMP                    | VARCHAR(4)   |                         |              | Ano mês de competência                                   |                                                         |
| REGIAO                  | VARCHAR(50)  |                         |              | Região                                                    |                                                         |
| UF                      | VARCHAR(2)   |                         |              | Estado                                                    |                                                         |
| MUNICIPIO               | VARCHAR(60)  |                         |              | Município                                                 |                                                         |
| MOTIVO DESABILITACAO    | VARCHAR(60)  |                         |              | Motivo de Desabilitação                                   |                                                         |
| CNES                    | VARCHAR(7)   |                         |              | Código do Cadastro Nacional dos Estabelecimentos de Saúde (CNES) |                                                         |
| NOME ESTABELECIMENTO    | VARCHAR(60)  |                         |              | Nome Fantasia                                             |                                                         |
| RAZAO SOCIAL            | VARCHAR(60)  |                         |              | Razão Social                                              |                                                         |
| TP_GESTAO               | CHAR(1)      |                         |              | "M – Municipal E – Estadual D – Dupla S – Sem Gestão"      |                                                         |
| CO_TIPO_UNIDADE         | VARCHAR2(2)  | DS_TIPO_UNIDADE         | VARCHAR(60)  | Código do Tipo de Unidade                                 | Descrição do Tipo de Unidade                              |
| NATUREZA_JURIDICA       | VARCHAR(4)   | DESC_NATUREZA_JURIDICA  | VARCHAR(60)  | Código da Natureza Jurídica do Estabelecimento             | Descrição da Natureza Jurídica do Estabelecimento          |
| NO_LOGRADOURO           | VARCHAR(60)  |                         |              | Logradouro                                                |                                                         |
| NU_ENDERECO             | VARCHAR(60)  |                         |              | Endereço                                                  |                                                         |
| NO_COMPLEMENTO          | VARCHAR(4)   |                         |              | Complemento de endereço                                   |                                                         |
| NO_BAIRRO               | VARCHAR(60)  |                         |              | Bairro                                                    |                                                         |
| CO_CEP                  | VARCHAR(8)   |                         |              | Código de Endereçamento Postal                            |                                                         |
| NU_TELEFONE             | VARCHAR(40)  |                         |              | Telefone                                                  |                                                         |
| NO_EMAIL                | VARCHAR(60)  |                         |              | E-mail                                                    |                                                         |
| LEITOS EXISTENTE        | NUMBER(6)    |                         |              | Quantidade de Leitos Existentes                           |                                                         |
| LEITOS SUS              | NUMBER(6)    |                         |              | Quantidade de Leitos SUS                                  |                                                         |
| UTI TOTAL - EXIST       | NUMBER(6)    |                         |              | Quantidade de Leitos UTI - Existentes                      | Somatório de leitos (Adulto, Pediátrico, Neonatal, Queimados e Coronariana) |
| UTI TOTAL - SUS         | NUMBER(6)    |                         |              | Quantidade de Leitos UTI - SUS                             | Somatório de leitos (Adulto, Pediátrico, Neonatal, Queimados e Coronariana) |
| UTI ADULTO - EXIST      | NUMBER(6)    |                         |              | Quantidade de Leitos Existentes Adulto - (I, II e III)    |                                                         |
| UTI ADULTO - SUS        | NUMBER(6)    |                         |              | Quantidade de Leitos SUS Adulto - (I, II e III)           |                                                         |
| UTI PEDIATRICO - EXIST  | NUMBER(6)    |                         |              | Quantidade de Leitos Existentes Pediátrico - (I, II e III)|                                                         |
| UTI PEDIATRICO - SUS    | NUMBER(6)    |                         |              | Quantidade de Leitos SUS Pediátrico - (I, II e III)       |                                                         |
| UTI NEONATAL - EXIST    | NUMBER(6)    |                         |              | Quantidade de Leitos Existentes Neonatal - (I, II e III)  |                                                         |
| UTI NEONATAL - SUS      | NUMBER(6)    |                         |              | Quantidade de Leitos SUS Neonatal - (I, II e III)         |                                                         |
| UTI QUEIMADO - EXIST    | NUMBER(6)    |                         |              | Quantidade de Leitos Existentes Queimado                  |                                                         |
| UTI QUEIMADO - SUS      | NUMBER(6)    |                         |              | Quantidade de Leitos SUS Queimado                         |                                                         |
| UTI CORONARIANA - EXIST | NUMBER(6)    |                         |              | Quantidade de Leitos Existentes Coronariana - (II e III)  |                                                         |
| UTI CORONARIANA - SUS   | NUMBER(6)    |                         |              | Quantidade de Leitos SUS Coronariana - (II e III)         |                                                         |


**Limitações:**
As limitações podem surgir devido à natureza da coleta de dados, dependendo das informações fornecidas pelos gestores locais de saúde.

### 7.4.2 Sistema de Informação sobre Nascidos Vivos – Sinasc - 1996 - 2023

O Sistema de Informações sobre Nascidos Vivos (Sinasc) foi estabelecido em 1990 para coletar dados sobre nascimentos em todo o território nacional. Os registros incluem informações socioeconômicas, local de residência, ocorrência, anomalias congênitas, parto e pré-natal. Esse sistema contribui para o conhecimento da saúde da população e avaliação de políticas relacionadas à saúde materno-infantil. A seguir, apresenta-se o glossário dos dados:

| Posição | Nome do Campo | Tipo | Tamanho | Descrição |
|---------|---------------|------|---------|-----------|
| 1       | CONTADOR      | C    | 8       | Número identificador do registro |
| 2       | LOCNASC       | C    | 7       | Local de nascimento: 1 – Hospital; 2 – Outros estabelecimentos de saúde; 3 – Domicílio; 4 – Outros; 5- Aldeia Indígena. |
| 3       | CODMUNNASC    | C    | 10      | Código IBGE do município de nascimento |
| 4       | IDADEMAE      | C    | 8       | Idade da mãe |
| 5       | ESTCIVMAE     | C    | 9       | Situação conjugal da mãe: 1– Solteira; 2– Casada; 3– Viúva; 4– Separada judicialmente/divorciada; 5– União estável; 9– Ignorada. |
| 6       | ESCMAE        | C    | 6       | "Escolaridade, em anos de estudo concluídos: 1 – Nenhuma; 2 – 1 a 3 anos; 3 – 4 a 7 anos; 4 – 8 a 11 anos; 5 – 12 e mais; 9 – Ignorado." |
| 7       | CODOCUPMAE    | C    | 10      | Código de ocupação da mãe conforme tabela do CBO (Código Brasileiro de Ocupações). |
| 8       | QTDFILVIVO    | C    | 10      | Número de filhos vivos |
| 9       | QTDFILMORT    | C    | 10      | Número de perdas fetais e abortos |
| 10      | CODMUNRES     | C    | 9       | Código IBGE do município de residência |
| 11      | GESTACAO      | C    | 8       | "Semanas de gestação: 1– Menos de 22 semanas; 2– 22 a 27 semanas; 3– 28 a 31 semanas; 4– 32 a 36 semanas; 5– 37 a 41 semanas; 6– 42 semanas e mais; 9– Ignorado." |
| 12      | GRAVIDEZ      | C    | 8       | Tipo de gravidez: 1– Única; 2– Dupla; 3– Tripla ou mais; 9– Ignorado. |
| 13      | PARTO         | C    | 5       | Tipo de parto: 1– Vaginal; 2– Cesário; 9– Ignorado |
| 14      | CONSULTAS     | C    | 9       | "Número de consultas de pré‐natal. Valores: 1– Nenhuma; 2– de 1 a 3; 3– de 4 a 6; 4– 7 e mais; 9– Ignorado." |
| 15      | DTNASC        | C    | 8       | Data de nascimento: dd mm aaaa |
| 16      | SEXO          | C    | 4       | Sexo: 1- M – Masculino; 2- F – Feminino; 0- I – ignorado |
| 17      | APGAR1        | C    | 6       | Apgar no 1º minuto 00 a a10 |
| 18      | APGAR5        | C    | 6       | Apgar no 5º minuto 00 a 10 |
| 19      | RACACOR       | C    | 7       | Tipo de raça e cor do nascido: 1– Branca; 2– Preta; 3– Amarela; 4– Parda; 5– Indígena. |
| 20      | PESO          | C    | 4       | Peso ao nascer em gramas. |
| 21      | CODANOMAL     | C    | 20      | Código da anomalia (CID-10) |
| 22      | HORANASC      | C    | 8       | Horário de nascimento |
| 23      | IDANOMAL      | C    | 8       | Anomalia identificada: 1– Sim; 2– Não; 9– Ignorado |
| 24      | CODESTAB      | C    | 8       | Código do estabelecimento de saúde onde ocorreu o nascimento |
| 25      | UFINFORM      | C    | 8       | Código da UF que informou o registro.0 |
| 26      | DTCADASTRO    | C    | 10      | Data do cadastro da DN no sistema |
| 27      | DTRECEBIM     | C    | 9       | Data do último recebimento do lote, dada pelo Sisnet. |
| 28      | ORIGEM        | C    | 6       | Banco de dados de Origem 1- Oracle, 2- FTP, 3- SEAD |
| 29      | CODCART       | C    | 7       | Código do Cartório |
| 30      | NUMREGCART    | C    | 10      | Numero do Registro do Cartório |
| 31      | DTREGCART     | C    | 9       | Data do registro no cartório |
| 32      | CODPAISRES    | C    | 10      | Código do país de residência |
| 33      | NUMEROLOTE    | C    | 10      | Número do lote |
| 34      | VERSAOSIST    | C    | 10      | Versão do sistema |
| 35      | DIFDATA       | C    | 8       | Diferença entre a data de Nascimento e data do recebimento original da DN ([DTNASC] – [DTRECORIG]) |
| 36      | DTRECORIG     | C    | 9       | Data do primeiro recebimento do lote, dada pelo Sisnet. |
| 37      | NATURALMAE    | C    | 10      | Se a mãe for estrangeira, constará o código do país de nascimento. |
| 38      | CODMUNNATU    | C    | 10      | Código do município de naturalidade da mãe |


### 7.4.3 SRAG - Banco de Dados de Síndrome Respiratória Aguda Grave - incluindo dados da COVID-19
Este banco de dados contém informações epidemiológicas sobre a Síndrome Respiratória Aguda Grave (SRAG) no Brasil desde 2009, incorporando dados da COVID-19 a partir de 2020. A vigilância é realizada pela Secretaria de Vigilância em Saúde e o sistema oficial para registro é o Sistema de Informação da Vigilância Epidemiológica da Gripe (SIVEP-Gripe). Os dados são disponibilizados semanalmente, sujeitos a alterações decorrentes de investigações e correções de erros, com anonimização em conformidade com a Lei 13.709/2018. A seguir, apresenta-se o glossário dos dados:


**1° Conjunto**

| Nome do Campo | Tipo | Categoria | Descrição | Características | DBF |
|---------------|------|-----------|-----------|-----------------|-----|
| Nº | Varchar2(12) | - | Número do registro | Campo Interno | NU_NOTIFIC |
| 1-Data do preenchimento da ficha de notificação | Date DD/MM/AAAA | - | Data de preenchimento da ficha de notificação | Campo Obrigatório | DT_NOTIFIC |
| Semana Epidemiológica do preenchimento da ficha de notificação | Varchar2(6) | - | Semana Epidemiológica do preenchimento da ficha de notificação | Campo Interno | SEM_NOT |
| 2-Data de 1ºs sintomas | Date DD/MM/AAAA | - | Data de 1º sintomas do caso | Campo Obrigatório | DT_SIN_PRI |
| Semana Epidemiológica dos Primeiros Sintomas | Varchar2(6) | - | Semana Epidemiológica do início dos sintomas | Campo Interno | SEM_PRI |
| 3-UF | Varchar2(2) | Tabela com código e siglas das UF padronizados pelo IBGE | Unidade Federativa onde está localizada a Unidade que realizou a notificação | Campo Obrigatório | SG_UF_NOT |
| 4-Município Código (IBGE) | Varchar2(6) | Tabela com código e nomes dos Municípios padronizados pelo IBGE | Município onde está localizada a Unidade que realizou a notificação | Campo Obrigatório | ID_MUNICIP OU CO_MUN_NOT |
| Regional de Saúde de Notificação Código (IBGE) | Varchar2(6) | Tabela com código e nomes das Regionais de Saúde dos municípios de notificação padronizados pelo IBGE | Regional de Saúde onde está localizado o Município realizou a notificação | Campo Interno | ID_REGIONA OU CO_REGIONA |
| 5-Unidade de Saúde Código (CNES) | Varchar2(7) | Tabela com códigos CNES e nomes das Unidades cadastradas no sistema | Unidade que realizou o atendimento, coleta de amostra e registro do caso | Campo Obrigatório | ID_UNIDADE OU CO_UNI_NOT |
| 6- Tem CPF? | Varchar(1) | 1-Sim 2-Não | Informar se o paciente notificado dispõe de Número do Cadastro de Pessoa Física (CPF) | Campo Obrigatório | TEM_CPF |
| 7-CPF do paciente | Varchar2(15) | Numérico (11 dígitos) | Número do Cadastro de Pessoa Física (CPF) do paciente notificado | Campo Obrigatório | NU_CPF |
| 8- Estrangeiro | Varchar(1) | 1-Sim 2-Não | Informar se o paciente é estrangeiro | Campo Obrigatório | ESTRANG |
| 9- Cartão Nacional de Saúde (CNS) | Varchar2(15) | Numérico (14 dígitos) | Preencher com o número do Cartão Nacional de Saúde do paciente | Campo Obrigatório | NU_CNS |
| 10-Nome | Varchar2(70) | - | Nome completo do paciente (sem abreviações) | Campo Obrigatório | NM_PACIENT |
| 11-Sexo | Varchar2(1) | 1-Masculino 2-Feminino 9-Ignorado | Sexo do paciente | Campo Obrigatório | CS_SEXO |
| 12-Data de nascimento | Date DD/MM/AAAA | - | Data de nascimento do paciente | Campo Essencial | DT_NASC |
| 13-(ou) Idade | Varchar2(3) | - | Idade informada pelo paciente quando não se sabe a data de nascimento. Na falta desse dado é registrada a idade aparente. | Campo Obrigatório | NU_IDADE_N |
| (ou) Tipo/Idade | Varchar2(1) | 1-Dia 2-Mês 3-Ano | Campo Obrigatório. Calculado automaticamente considerando a diferença entre a data de nascimento e os primeiros sintomas. | TP_IDADE |
| 14-Gestante | Varchar2(1) | 1-1º Trimestre 2-2º Trimestre ... 9-Ignorado | Idade gestacional da paciente. | Campo Obrigatório. Condições de preenchimento específicas. | CS_GESTANT |
| 15-Raça/Cor | Varchar2(2) | 1-Branca 2-Preta ... 9-Ignorado | Cor ou raça declarada pelo paciente. | Campo Obrigatório | CS_RACA |
| 16-Se indígena, qual etnia? | Varchar2(4) | Tabela SIASI | Nome e código da etnia do paciente quando indígena. | Campo Essencial. Habilitado se Raça/Cor = 5-Indígena. | CS_ETINIA |
| 17- É membro de povo ou comunidade tradicional? | Varchar2(1) | 1-Sim 2-Não | Informar se o paciente é membro de algum povo ou comunidade tradicional. | Campo Obrigatório | POV_CT |
| 18- Se sim, qual? | Varchar2(100) | Tabela Povos e Comunidades Tradicionais | Informar o povo ou comunidade tradicional. | Campo Obrigatório. Habilitado se 17- É membro de povo ou comunidade tradicional? = 1-Sim. | TP_POV_CT |
| 19-Escolaridade | Varchar2(1) | 0-Sem escolaridade/.../5-Não se aplica 9-Ignorado | Nível de escolaridade do paciente. | Campo Essencial. Condições específicas de preenchimento. | CS_ESCOL_N |
| 20- Ocupação | Varchar2(6) | Tabela CBO | Ocupação profissional do paciente. | Campo Essencial | PAC_COCBO ou PAC_DSCBO |
| 21-Nome da mãe | Varchar2(70) | - | Nome completo da mãe do paciente. | Campo Essencial | NM_MAE_PAC |
| 22-CEP | Varchar2(8) | - | CEP de residência do paciente. | Campo Essencial. Validado a partir da tabela de CEP dos Correios. | NU_CEP |
| 23-UF | Varchar2(2) | Tabela UF | Unidade Federativa de residência do paciente. | Campo Obrigatório. Se preenchido o CEP, UF é preenchido automaticamente. | SG_UF |
| Regional de Saúde de Residência Código (IBGE) | Varchar2(6) | Tabela de Regionais de Saúde | Regional de Saúde onde está localizado o Município de residência do paciente. | Campo Interno. Preenchido automaticamente. | ID_RG_RESI OU CO_RG_RESI |
| 24-Município Código (IBGE) | Varchar2(6) | Tabela de Municípios | Município de residência do paciente. | Campo Obrigatório. Se preenchido o CEP, Município e seu código IBGE são preenchidos automaticamente. | ID_MN_RESI OU CO_MUN_RES |
| 25-Bairro | Varchar2(72) | Tabela de Bairros dos Correios | Bairro de residência do paciente. | Campo Essencial. Se preenchido o CEP, Bairro é preenchido automaticamente. | NM_BAIRRO |
| 26-Logradouro (Rua, Avenida, etc.) | Varchar2(50) | Tabela de Logradouros dos Correios | Logradouro (rua, avenida, quadra, travessa, etc.) do endereço de residência do paciente. | Campo Essencial. Se preenchido o CEP, Logradouro é preenchido automaticamente. | NM_LOGRADO |
| 27-Nº | Varchar2(8) | - | Número do logradouro (nº da casa ou do edifício). | Campo Essencial | NU_NUMERO |
| 28-Complemento (apto, casa, etc.) | Varchar2(15) | - | Complemento do logradouro (bloco, apto, casa, etc.). | Campo Essencial | NM_COMPLEM |
| 29-(DDD) Telefone | Varchar2(4) | Varchar2(10) | Código DDD e número de telefone para contato do paciente. | Campo Essencial | NU_DDD_TEL OU NU_TELEFON |
| 30-Zona | Varchar2(1) | 1-Urbana 2-Rural 3-Periurbana 9-Ignorado | Zona geográfica do endereço de residência do paciente. | Campo Essencial | CS_ZONA |
| 31-País (se residente fora do Brasil) | Varchar2(3) | Tabela de Países | País de residência do paciente. | Campo Obrigatório. Se preenchido o CEP, ou selecionada uma UF, País é preenchido automaticamente. | ID_PAIS OU CO_PAIS |
| 32-Trata-se de caso nosocomial (infecção adquirida no hospital)? | Varchar2(1) | 1-Sim 2-Não 9-Ignorado | Caso de SRAG com infecção adquirida após internação. | Campo Essencial. Permitido digitar data de início dos sintomas posterior a data de internação se 32 for igual a 1. | NOSOCOMIAL |
| 33- Paciente trabalha ou tem contato direto com aves, suínos, ou outro animal? | Varchar2(1) | 1-Sim 2-Não 9-Ignorado | Caso com contato direto com aves ou suínos. | Campo Essencial | AVE_SUINO |
| 33-Paciente trabalha ou tem contato direto com aves, suínos/Outro animal (especificar) | Varchar2(60) | - | Informar o animal que o paciente teve contato se selecionada a opção 3. | Campo Essencial. Habilitado se 33-Contato com outro animal = 3 (Outro). | OUT_ANIM |



**2° Conjunto**


| Nome do Campo | Tipo | Descrição | Condições/Validações |
|---------------|------|-----------|-----------------------|
| 34-Sinais e Sintomas/Febre | Varchar2(1) | Paciente apresentou febre? | Campo Essencial. FEBRE |
| 34-Sinais e Sintomas/Tosse | Varchar2(1) | Paciente apresentou tosse? | Campo Essencial. TOSSE |
| 34-Sinais e Sintomas/Dor de Garganta | Varchar2(1) | Paciente apresentou dor de garganta? | Campo Essencial. GARGANTA |
| 34-Sinais e Sintomas/Dispneia | Varchar2(1) | Paciente apresentou dispneia? | Campo Essencial. DISPNEIA |
| 34-Sinais e Sintomas/Desconforto Respiratório | Varchar2(1) | Paciente apresentou desconforto respiratório? | Campo Essencial. DESC_RESP |
| 34-Sinais e Sintomas/Saturação O2< 95% | Varchar2(1) | Paciente apresentou saturação O2< 95%? | Campo Essencial. SATURACAO |
| 34-Sinais e Sintomas/Diarreia | Varchar2(1) | Paciente apresentou diarreia? | Campo Essencial. DIARREIA |
| 34-Sinais e Sintomas/Vômito | Varchar2(1) | Paciente apresentou vômito? | Campo Essencial. VOMITO |
| 34-Sinais e Sintomas/Dor abdominal | Varchar2(1) | Paciente apresentou dor abdominal? | Campo Essencial. DOR_ABD |
| 34-Sinais e Sintomas/Fadiga | Varchar2(1) | Paciente apresentou fadiga? | Campo Essencial. FADIGA |
| 34-Sinais e Sintomas/Perda do Olfato | Varchar2(1) | Paciente apresentou perda do olfato? | Campo Essencial. PERD_OLFT |
| 34-Sinais e Sintomas/Perda do Paladar | Varchar2(1) | Paciente apresentou perda do paladar? | Campo Essencial. PERD_PALA |
| 34-Sinais e Sintomas/Outros | Varchar2(1) | Paciente apresentou outro(s) sintoma(s)? | Campo Essencial. OUTRO_SIN |
| 34-Sinais e Sintomas/Outros (Descrição) | Varchar2(30) | Listar outros sinais e sintomas apresentados pelo paciente. Habilitado se selecionada categoria 1-Sim em Sinais e Sintomas/Outros. | Campo Essencial. Habilitado se selecionada categoria 1-Sim em Sinais e Sintomas/Outros. OUTRO_DES |
| 35-Fatores de risco | Varchar2(1) | Paciente apresenta algum fator de risco? | Campo Essencial. FATOR_RISC |
| 35-Fatores de risco/ Puérpera | Varchar2(1) | Paciente é puérpera ou parturiente (mulher que pariu recentemente – até 45 dias do parto)? | Campo Essencial. Habilitado se selecionado no campo 8- Sexo Feminino. PUERPERA |
| 35-Fatores de risco/ Doença Cardiovascular Crônica | Varchar2(1) | Paciente possui Doença Cardiovascular Crônica? | Campo Essencial. CARDIOPATI |
| 35-Fatores de risco/ Doença Hematológica Crônica | Varchar2(1) | Paciente possui Doença Hematológica Crônica? | Campo Essencial. HEMATOLOGI |
| 35-Fatores de risco/ Síndrome de Down | Varchar2(1) | Paciente possui Síndrome de Down? | Campo Essencial. SIND_DOWN |
| 35-Fatores de risco/ Doença Hepática Crônica | Varchar2(1) | Paciente possui Doença Hepática Crônica? | Campo Essencial. HEPATICA |
| 35-Fatores de risco/ Asma | Varchar2(1) | Paciente possui Asma? | Campo Essencial. ASMA |
| 35-Fatores de risco/ Diabetes mellitus | Varchar2(1) | Paciente possui Diabetes mellitus? | Campo Essencial. DIABETES |
| 35-Fatores de risco/ Doença Neurológica Crônica | Varchar2(1) | Paciente possui Doença Neurológica? | Campo Essencial. NEUROLOGIC |
| 35-Fatores de risco/ Outra Pneumatopatia Crônica | Varchar2(1) | Paciente possui outra pneumopatia crônica? | Campo Essencial. PNEUMOPATI |
| 35-Fatores de risco/ Imunodeficiência ou Imunodepressão | Varchar2(1) | Paciente possui Imunodeficiência ou Imunodepressão (diminuição da função do sistema imunológico)? | Campo Essencial. IMUNODEPRE |
| 35-Fatores de risco/ Doença Renal Crônica | Varchar2(1) | Paciente possui Doença Renal Crônica? | Campo Essencial. RENAL |
| 35-Fatores de risco/ Obesidade | Varchar2(1) | Paciente possui obesidade? | Campo Essencial. OBESIDADE |
| 35-Fatores de risco/ Obesidade (Descrição IMC) | Varchar2(3) | Valor do IMC (Índice de Massa Corporal) do paciente calculado pelo profissional de saúde. Habilitado se selecionado categoria 1-Sim em Fatores de risco/Obesidade. | Campo Essencial. Habilitado se selecionado categoria 1-Sim em Fatores de risco/Obesidade. OBES_IMC |
| 35-Fatores de risco/ Outros | Varchar2(1) | Paciente possui outro(s) fator(es) de risco? | Campo Essencial. OUT_MORBI |
| 35-Fatores de risco/ Outros (Descrição) | Varchar2(30) | Listar outro(s) fator(es) de risco do paciente. Habilitado se selecionado categoria 1-Sim em Fatores de risco/Outros. | Campo Essencial. Habilitado se selecionado categoria 1-Sim em Fatores de risco/Outros. MORB_DESC |
| 36- Recebeu vacina COVID-19? | Varchar(1) | Informar se o paciente recebeu vacina COVID-19, após verificar a documentação / caderneta. | Campo Obrigatório. Integração com a Base Nacional de Vacinação. VACINA_COV |
| 37- Data 1ª dose da vacina COVID-19 | Varchar(10) | Informar a data em que o paciente recebeu a 1ª dose da vacina COVID-19. Habilitado se campo 36- Recebeu vacina COVID-19? for igual a 1. | Campo Essencial. Integração com a Base Nacional de Vacinação. DOSE_1_COV |
| 37- Data 2ª dose da vacina COVID-19 | Varchar(10) | Informar a data em que o paciente recebeu a 2ª dose da vacina COVID-19. Habilitado se campo 36- Recebeu vacina COVID-19? for igual a 1. | Campo Essencial. Integração com a Base Nacional de Vacinação. DOSE_2_COV |
| 37- Data da dose reforço da vacina COVID-19 | Varchar(10) | Informar a data em que o paciente recebeu a dose reforço da vacina COVID-19. Habilitado se campo 36- Recebeu vacina COVID-19? for igual a 1. | Campo Essencial. Integração com a Base Nacional de Vacinação. DOSE_REF |
| 37- Data da 2ª dose reforço da vacina COVID-19 | Varchar(10) | Informar a data em que o paciente recebeu a 2ª dose reforço da vacina COVID-19. Habilitado se campo 36- Recebeu vacina COVID-19? for igual a 1. | Campo Essencial. Integração com a Base Nacional de Vacinação. DOSE_2REF |
| 38- Fabricante 1ª dose da vacina COVID-19 | Varchar(80) | Informar o fabricante da vacina, que o paciente recebeu na primeira dose. Habilitado se campo 36- Recebeu vacina COVID-19? for igual a 1. | Campo Essencial. Integração com a Base Nacional de Vacinação. FAB_COV1 |
| 38- Fabricante 2ª dose da vacina COVID-19 | Varchar(80) | Informar o fabricante da vacina, que o paciente recebeu na segunda dose. Habilitado se campo 36- Recebeu vacina COVID-19? for igual a 1. | Campo Essencial. Integração com a Base Nacional de Vacinação. FAB_COV2 |
| 38- Fabricante dose reforço da vacina COVID-19 | Varchar(80) | Informar o fabricante da vacina, que o paciente recebeu na dose reforço. Habilitado se campo 36- Recebeu vacina COVID-19? for igual a 1. | Campo Essencial. Integração com a Base Nacional de Vacinação. FAB_COVRF |
| 38- Fabricante 2ª dose reforço da vacina COVID-19 | Varchar(80) | Informar o fabricante da vacina, que o paciente recebeu na 2ª dose reforço. Habilitado se campo 36- Recebeu vacina COVID-19? for igual a 1. | Campo Essencial. Integração com a Base Nacional de Vacinação. FAB_COVRF2 |
| 39- Lote da vacina COVID-19: Lote 1ª Dose | Varchar(20) | Informar o Lote da 1ª dose da vacina COVID-19, que o paciente recebeu. Habilitado se campo 36- Recebeu vacina COVID-19? for igual a 1. | Campo Essencial. Integração com a Base Nacional de Vacinação. LOTE_1_COV |
| 39- Lote da vacina COVID-19: Lote 2ª Dose | Varchar(20) | Informar o Lote da 2ª dose da vacina COVID-19, que o paciente recebeu. Habilitado se campo 36- Recebeu vacina COVID-19? for igual a 1. | Campo Essencial. Integração com a Base Nacional de Vacinação. LOTE_2_COV |
| 39- Lote da vacina COVID-19: Lote dose reforço | Varchar(20) | Informar o Lote da dose reforço da vacina COVID-19, que o paciente recebeu. Habilitado se campo 36- Recebeu vacina COVID-19? for igual a 1. | Campo Essencial. Integração com a Base Nacional de Vacinação. LOTE_REF_COV |
| 39- Lote da vacina COVID-19: Lote 2ª dose reforço | Varchar(20) | Informar o Lote da 2ª dose reforço da vacina COVID-19, que o paciente recebeu. Habilitado se campo 36- Recebeu vacina COVID-19? for igual a 1. | Campo Essencial. Integração com a Base Nacional de Vacinação. LOTE_2REF_COV |
| 39- Fonte dos dados/informação sobre a vacina COVID-19 | Varchar(1) | Campo Interno. Número gerado automaticamente pelo sistema. Preenchido de acordo com a fonte dos dados/informação sobre a vacina COVID-19, se foi digitada manualmente ou recuperada via integração com a Base Nacional de Vacinação. | - |
| 40-Recebeu vacina contra Gripe na última campanha? | Varchar2(1) | Informar se o paciente foi vacinado contra gripe na última campanha, após verificar a documentação/caderneta. Caso o paciente não tenha a caderneta, direcionar a pergunta para ele ou responsável e preencher o campo com o código correspondente a resposta. | Campo Essencial. |

**Limitações:**	
Os dados podem estar sujeitos a alterações devido a investigações em curso. A anonimização é aplicada para cumprir as regulamentações de privacidade.

**Observação:** 
Pelo grande número de glossário para esse conjunto de dados, pode-se acessar o arquivo completo [Dicionário de Dados SRAG Hospitalizado - 19.09.2022](https://s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/SRAG/pdfs/Dicionario_de_Dados_SRAG_Hospitalizado_19.09.2022.md)


### 7.4.4 Registro de Ocupação Hospitalar COVID-19

Implementado devido à pandemia, este banco de dados fornece informações sobre a ocupação de leitos clínicos e de UTI SUS destinados a pacientes com casos suspeitos ou confirmados de COVID-19. A coleta é realizada por meio do Sistema ESUS Notifica-Módulo Internações SUS, iniciado em abril de 2020. A partir de 2022, novos campos foram acrescentados para descrever a ocupação dos leitos. Não se é oferecido glossário dos dados.

**Limitações:** Devido ao grande volume de registros, alguns estados têm mais de um milhão de entradas, registros anteriores a 2022 podem não conter os novos campos preenchidos.

# <a name="c7"></a>8. Conjunto de dados de Códigos Postais Mundiais

O B4a (BackForApp), cloud de dados disponibilizou uma base de dados abrangente com informações sobre códigos postais de todos os países do mundo que pode ser conferido no link a seguir: [https://www.back4app.com/database/back4app/zip-codes-all-countries-in-the-world). 
Os dados foram extraidos do site [http://www.geonames.org/], no qual cada conjunto de dados representa um país e inclui as seguintes informações:

* Número do Código Postal em formato de string
* Nome do Local em formato de string
* Geolocalização em formato de ponto geográfico
* Precisão da Geolocalização em formato de string
* Código Administrativo em formato de string
* Nome Administrativo em formato de string

O conjunto de dados disponibilizado abrange os códigos postais de 97 países diferentes. No entanto, em atendimento a solicitação específica de nosso parceiro, estaremos concentrando nossos esforços na análise exploratória dos dados referentes exclusivamente ao Brasil. Dessa forma, os dados relativos aos demais países serão desconsiderados durante este processo de análise. 

Esta abordagem visa encontrar insights precisos e valiosos que atendam às necessidades e expectativas específicas delineadas em nosso projeto. Essa estratégia permite uma análise mais aprofundada e personalizada dos dados, maximizando o impacto de nossos esforços de análise exploratória no contexto brasileiro.

No conjunto de dados há um total de 11 colunas distintas, cada uma oferecendo informações específicas sobre os códigos postais. Abaixo, estão detalhadas as definições de cada coluna:

1. accuracy (precisão):
* Descrição: Indica a precisão da latitude e longitude.
*Valores: 1=estimado, 4=geonameid, 6=centroide de endereços ou forma.

2. admin name1 (nome administrativo 1):
*Descrição: Representa a subdivisão de 1ª ordem (estado).
*Tipo: varchar(100) - String com até 100 caracteres.

3. admin code1 (código administrativo 1):
*Descrição: Código correspondente à subdivisão de 1ª ordem (estado).
*Tipo: varchar(20) - String com até 20 caracteres.

4.admin name2 (nome administrativo 2):
*Descrição: Representa a subdivisão de 2ª ordem (condado/província).
*Tipo: varchar(100) - String com até 100 caracteres.

5.admin code2 (código administrativo 2):
*Descrição: Código correspondente à subdivisão de 2ª ordem (condado/província).
*Tipo: varchar(20) - String com até 20 caracteres.

6. admin name3 (nome administrativo 3):
* Descrição: Representa a subdivisão de 3ª ordem (comunidade).
* Tipo: varchar(100) - String com até 100 caracteres.

7. admin code3 (código administrativo 3):
* Descrição: Código correspondente à subdivisão de 3ª ordem (comunidade).
* Tipo: varchar(20) - String com até 20 caracteres.

8.country code (código do país):
* Descrição: Código ISO de 2 caracteres referente ao país.
* Tipo: 2 caracteres.

9.geoposition (geoposição):
* Descrição: Coordenadas geográficas que representam a latitude e longitude estimadas.
* Tipo: cordenates - latitude: estimated latitude (wgs84), longitude: estimated longitude (wgs84).

10. postal code (código postal):
* Descrição: Código postal.
* Tipo: varchar(20) - String com até 20 caracteres.

11. place name (nome do local):
* Descrição: Nome do local associado ao código postal.
* Tipo: varchar(180) - String com até 180 caracteres.

