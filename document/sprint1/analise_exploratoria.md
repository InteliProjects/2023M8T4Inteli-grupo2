## Sumário

[1. CNPJs](#c1)

[2. Dados do Governo](#c2)

<br>

# <a name="c1"></a>1. CNPJs

&emsp;&emsp; A primeira análise exploratória feita foi a dos dados do Cadastro Nacional de Pessoas Jurídicas, ou CNPJ, sendo um processo fundamental para qual é a estrutura dos _csv_ disponibilizado pelo parceiro. O CNPJ é um registro obrigatório para todas as empresas ativas, o que o torna uma fonte rica de informações sobre a economia e o mercado de trabalho de uma nação. Para este projeto, foi disponibilizado 5 arquivos _csv_ com informações de empresas de 10 CNAEs diferentes. O primeiro passo é realizar a configuração do Setup, que inclui a preparação e organização do ambiente, ou seja, realizar a conexão com o Drive, baixar as bibliotecas e acessar o arquivo. A seguir é realizada a análise que coleta informações sobre os dados disponibilizados. Abaixo há uma descrição sobre cada arquivo. 

## 1.1 CNPJ 1

&emsp;&emsp; Este _dataset_ contém as empresas cadastradas somente com o CNAE: "5611201", referente à "Restaurantes e similares", de acordo com o Contabilizei. Além disso, há 515.874 CNPJs neste arquivo. O primeiro gráfico feito foi feito de acordo com a coluna _sigla_uf_, com o código abaixo.

```
cnpjs_1['sigla_uf'].value_counts().plot(kind='bar')
plt.title("Distribuição por UF")
plt.xlabel("UF")
plt.ylabel("Contagem")
plt.show()
```

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206636/498c5bb0-f07a-4aa1-9de1-c0b61fe84aa9) <br>
Figura 1: Gráfico “Distribuição por UF” - CNPJ1

&emsp;&emsp; Com esse gráfico é possível observar que os três estados que mais tem "Restaurantes e similares" cadastrados são: São Paulo, Rio de Janeiro e Minas Gerais, respectivamente. Além disso, há uma inconsistência nos dados, já que o último UF mostrado no gráfico é "EX", que significa "Exterior", este dado não deveria aparecer, já que o CNPJ é um documento brasileiro. O mesmo pode-se observar no gráfico a seguir.

```
cnpjs_1['id_pais'].value_counts().plot(kind='bar')
plt.title("Distribuição por País")
plt.xlabel("ID do País")
plt.ylabel("Contagem")
plt.show()
```

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206636/6757de59-2eb6-4af6-9a2a-b2e3223b4c13) <br>
Figura 2: Gráfico “Distribuição por País” - CNPJ1

&emsp;&emsp; O gráfico "Distribuição por País" comprova que há, pelo menos, 11 CNPJs que estão cadastrados em outro país. A primeira coluna, com o ID de "105", é o Brasil. O gráfico a seguir mostra quais empresas são matrizes e quais são filiais. 

```
cnpjs_1['identificador_matriz_filial'].value_counts().plot(kind='bar')
plt.title("Matriz e Filial")
plt.xlabel("ID")
plt.ylabel("Contagem")
plt.show()
```

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206636/c0d53073-05da-4a48-8435-60b7a6d273c1) <br>
Figura 3: Gráfico “Matriz e Filial” - CNPJ1

&emsp;&emsp; É importante ressaltar neste gráfico que o ID "1" é Matriz, e o ID "2" é Filial. Com isso, pode-se observar que a grande parte dos restaurantes são matrizes do CNPJ. 

## 1.2 CNPJ 2

&emsp;&emsp; Este _dataset_ contém as empresas cadastradas somente com o CNAE: "5611203", referente à "Lanchonetes, casas de chá, de sucos e similares", de acordo com o Contabilizei. Além disso, há 577.735 CNPJs neste arquivo. O primeiro gráfico feito foi feito de acordo com a coluna _sigla_uf_, com o código abaixo.

```
cnpjs_1['sigla_uf'].value_counts().plot(kind='bar')
plt.title("Distribuição por UF")
plt.xlabel("UF")
plt.ylabel("Contagem")
plt.show()
```

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206636/fc8bf36a-de75-4709-98d4-203084704ab3) <br>
Figura 4: Gráfico “Distribuição por UF” - CNPJ2

&emsp;&emsp; Com esse gráfico é possível observar que os três estados que mais tem "Lanchonetes, casas de chá, de sucos e similares" cadastrados são: São Paulo, Minas Gerais e Rio de Janeiro, respectivamente. Além disso, há uma inconsistência nos dados, já que o último UF mostrado no gráfico é "EX", que significa "Exterior", este dado não deveria aparecer, já que o CNPJ é um documento brasileiro. O mesmo pode-se observar no gráfico a seguir.

```
cnpjs_1['id_pais'].value_counts().plot(kind='bar')
plt.title("Distribuição por País")
plt.xlabel("ID do País")
plt.ylabel("Contagem")
plt.show()
```

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206636/48644f99-5c93-4738-b572-a6c3b75fa6a4) <br>
Figura 5: Gráfico “Distribuição por País” - CNPJ2

&emsp;&emsp; O gráfico "Distribuição por País" comprova que há, pelo menos, 3 CNPJs que estão cadastrados em outro país. A primeira coluna, com o ID de "105", é o Brasil. O gráfico a seguir mostra quais empresas são matrizes e quais são filiais. 

```
cnpjs_1['identificador_matriz_filial'].value_counts().plot(kind='bar')
plt.title("Matriz e Filial")
plt.xlabel("ID")
plt.ylabel("Contagem")
plt.show()
```

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206636/0ade519a-6512-46a9-804d-9b7abc46a937) <br>
Figura 6: Gráfico “Matriz e Filial” - CNPJ2

&emsp;&emsp; É importante ressaltar neste gráfico que o ID "1" é Matriz, e o ID "2" é Filial. Com isso, pode-se observar que a grande parte das lanchonetes são matrizes do CNPJ. 

## 1.3 CNPJ 3

&emsp;&emsp; Este _dataset_ contém as empresas cadastradas somente com o CNAE: "5611204", referente à "Bares e outros estabelecimentos especializados em servir bebidas, sem entretenimento", de acordo com o Contabilizei. Além disso, há 184.274 CNPJs neste arquivo. O primeiro gráfico feito foi feito de acordo com a coluna _sigla_uf_, com o código abaixo.

```
cnpjs_1['sigla_uf'].value_counts().plot(kind='bar')
plt.title("Distribuição por UF")
plt.xlabel("UF")
plt.ylabel("Contagem")
plt.show()
```

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206636/86ed1764-8f7d-4af1-8362-e4edf559a6f5) <br>
Figura 7: Gráfico “Distribuição por UF” - CNPJ3

&emsp;&emsp; Com esse gráfico é possível observar que os três estados que mais tem "Bares e outros estabelecimentos especializados em servir bebidas, **sem** entretenimento" cadastrados são: São Paulo, Minas Gerais e Rio de Janeiro, respectivamente. O gráfico a seguir demonstra que a inconsistência encontrada nos últimos arquivos não foi encontrado neste.

```
cnpjs_1['id_pais'].value_counts().plot(kind='bar')
plt.title("Distribuição por País")
plt.xlabel("ID do País")
plt.ylabel("Contagem")
plt.show()
```

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206636/62160f90-fc56-4b92-b1a1-2f03b7894606) <br>
Figura 8: Gráfico “Distribuição por País” - CNPJ3

&emsp;&emsp; A única coluna, com o ID de "105", é o Brasil. O gráfico a seguir mostra quais empresas são matrizes e quais são filiais. 

```
cnpjs_1['identificador_matriz_filial'].value_counts().plot(kind='bar')
plt.title("Matriz e Filial")
plt.xlabel("ID")
plt.ylabel("Contagem")
plt.show()
```

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206636/596bb92b-bf5f-42eb-90e1-70eff7e2dfe1) <br>
Figura 9: Gráfico “Matriz e Filial” - CNPJ3

&emsp;&emsp; É importante ressaltar neste gráfico que o ID "1" é Matriz, e o ID "2" é Filial. Com isso, pode-se observar que a praticamente todos dos bares são matrizes do CNPJ. 

## 1.4 CNPJ 4

&emsp;&emsp; Este _dataset_ contém as empresas cadastradas somente com o CNAE: "5611205", referente à "Bares e outros estabelecimentos especializados em servir bebidas, **com** entretenimento", de acordo com o Contabilizei. Além disso, há 92.612 CNPJs neste arquivo. O primeiro gráfico feito foi feito de acordo com a coluna _sigla_uf_, com o código abaixo.

```
cnpjs_1['sigla_uf'].value_counts().plot(kind='bar')
plt.title("Distribuição por UF")
plt.xlabel("UF")
plt.ylabel("Contagem")
plt.show()
```

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206636/3541729f-e45e-49c8-aaeb-5e65054d6e89) <br>
Figura 10: Gráfico “Distribuição por UF” - CNPJ4

&emsp;&emsp; Com esse gráfico é possível observar que os três estados que mais tem "Bares e outros estabelecimentos especializados em servir bebidas, com entretenimento" cadastrados são: São Paulo, Minas Gerais e Rio de Janeiro, respectivamente. O gráfico a seguir demonstra que a inconsistência encontrada nos últimos arquivos não foi encontrado neste.

```
cnpjs_1['id_pais'].value_counts().plot(kind='bar')
plt.title("Distribuição por País")
plt.xlabel("ID do País")
plt.ylabel("Contagem")
plt.show()
```

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206636/e56a882f-66b3-4cbf-87e0-02fade704905) <br>
Figura 11: Gráfico “Distribuição por País” - CNPJ4

&emsp;&emsp; A única coluna, com o ID de "105", é o Brasil. O gráfico a seguir mostra quais empresas são matrizes e quais são filiais. 

```
cnpjs_1['identificador_matriz_filial'].value_counts().plot(kind='bar')
plt.title("Matriz e Filial")
plt.xlabel("ID")
plt.ylabel("Contagem")
plt.show()
```

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206636/b7c162cf-a6d5-4fe0-bba5-1162433c2c35) <br>
Figura 12: Gráfico “Matriz e Filial” - CNPJ4

&emsp;&emsp; É importante ressaltar neste gráfico que o ID "1" é Matriz, e o ID "2" é Filial. Com isso, pode-se observar que a praticamente todos dos bares são matrizes do CNPJ. 

## 1.5 CNPJ 5

&emsp;&emsp; Este _dataset_ contém as empresas cadastradas com os CNAEs são: 
- "4712100" - "Comércio varejista de mercadorias em geral, com predominância de produtos alimentícios - **minimercados, mercearias e armazéns**";
- "4711302" - "Comércio varejista de mercadorias em geral, com predominância de produtos alimentícios - **supermercados**";
- "4711301" - "Comércio varejista de mercadorias no geral, com predominância de produtos alimentícios - **hipermercados**";
- "4691500" - "Comércio atacadista de mercadorias em geral, com predominância de produtos alimentícios";
- "4637107" - "Comércio atacadista de chocolares, confeitos, balas, bombons e semelhantes";

&emsp;&emsp; Essas atividades foram buscadas no site do Contabilizei. Além disso, há 651.730 CNPJs neste arquivo. O primeiro gráfico feito foi feito de acordo com a coluna _sigla_uf_, com o código abaixo.

```
cnpjs_1['sigla_uf'].value_counts().plot(kind='bar')
plt.title("Distribuição por UF")
plt.xlabel("UF")
plt.ylabel("Contagem")
plt.show()
```

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206636/e34dea24-6127-451b-bc36-3048b9f6b874) <br>
Figura 13: Gráfico “Distribuição por UF” - CNPJ5

&emsp;&emsp; Com esse gráfico é possível observar que os três estados que mais tem essas atividades cadastradas são: São Paulo, Bahia e Minas Gerais, respectivamente. Além disso, há uma inconsistência nos dados, já que o último UF mostrado no gráfico é "EX", que significa "Exterior", este dado não deveria aparecer, já que o CNPJ é um documento brasileiro. O mesmo pode-se observar no gráfico a seguir.

```
cnpjs_1['id_pais'].value_counts().plot(kind='bar')
plt.title("Distribuição por País")
plt.xlabel("ID do País")
plt.ylabel("Contagem")
plt.show()
```

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206636/b400dc3b-26ea-477e-85a2-189ec8088931) <br>
Figura 14: Gráfico “Distribuição por País” - CNPJ5

&emsp;&emsp; O gráfico "Distribuição por País" comprova que há, pelo menos, 14 CNPJs que estão cadastrados em outro país. A primeira coluna, com o ID de "105", é o Brasil. O gráfico a seguir mostra quais empresas são matrizes e quais são filiais. 

```
cnpjs_1['identificador_matriz_filial'].value_counts().plot(kind='bar')
plt.title("Matriz e Filial")
plt.xlabel("ID")
plt.ylabel("Contagem")
plt.show()
```

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206636/83270a34-2c82-4f4d-8919-bd13336ba3c4) <br>
Figura 15: Gráfico “Matriz e Filial” - CNPJ5

&emsp;&emsp; É importante ressaltar neste gráfico que o ID "1" é Matriz, e o ID "2" é Filial. Com isso, pode-se observar que há uma predominância de matrizes do CNPJ. 

# <a name="c2"></a>2. Dados do Governo

&emsp;&emsp; A segunda análise exploratória feita foi a dos dados disponibilizados pelo governo sobre o POF, Pesquisa de Orçamentos Familiares, os arquivos que serão explicados a seguir estão separados e serão juntados em um próximo momento. Além disso, foi disponibilizado um arquivo Excel que contém o dicionário de variáveis e colunas, que será utilizado para a substituição de valores _int_ para _object_. 

&emsp;&emsp; O primeiro passo é realizar a configuração do Setup, que inclui a preparação e organização do ambiente, ou seja, realizar a conexão com o Drive, baixar as bibliotecas e acessar o arquivo. A seguir é realizada a análise que coleta informações sobre os dados disponibilizados. Abaixo há uma descrição sobre cada arquivo. 

## 2.1 Aluguel Estimado

&emsp;&emsp; O _dataset aluguel_estimado_ contém informações sobre os domicílios do Brasil que são alugados e informações sobre. Este é composto por 19 colunas e quase 50 mil linhas de dados. Acessando o dicionário de variáveis, foi realizado um _.replace_ em 3 colunas que foram consideradas mais importantes para uma primeira análise, o código a seguir demonstra essa mudança. 

```
aluguel_estimado['UF'] = aluguel_estimado['UF'].replace({11: 'Rondônia', 12: 'Acre', 13: 'Amazonas', 14: 'Roraima', 15: 'Pará', 16: 'Amapá', 17:'Tocantins', 21:'Maranhão', 22:'Piauí', 23:'Ceará', 24:'Rio Grande do Norte', 25:'Paraíba', 26:'Pernambuco', 27:'Alagoas', 28:'Sergipe', 29:'Bahia', 31:'Minas Gerais', 32:'Espírito Santo', 33:"Rio de Janeiro", 35:'São Paulo', 41:'Paraná', 42:'Santa Catarina', 43:'Rio Grande do Sul', 50:'Mato Grosso do Sul', 51:'Mato Grosso', 52: 'Goiás', 53:'Distrito Federal'})
```

&emsp;&emsp; Um detalhe que foi reparado é que os números dos estados estão divididos nas regiões, por exemplo: ```31:'Minas Gerais', 32:'Espírito Santo', 33:"Rio de Janeiro", 35:'São Paulo'```, todos começam com "3" pois são da região Sudeste. Com o código acima, foi realizado a substituição dos valores inteiros para _object_. Abaixo, segue o código e o gráfico desta coluna. 

```
aluguel_estimado['UF'].value_counts().plot(kind='bar')
plt.title("Distribuição por UF")
plt.xlabel("UF")
plt.ylabel("Contagem")
plt.show()
```

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206636/8471eacd-496c-4b5b-a9a9-344d72ed1c3a) <br>
Figura 16: Gráfico “Distribuição por UF” - Aluguel Estimado

&emsp;&emsp; Com esse gráfico, pode-se classificar que os estados que mais tem imovéis alugados são, respectivamente: Minas Gerais, São Paulo e Bahia. O código a seguir foi feito o mesmo processo, só que na coluna "TIPO_SITUACAO_REG", onde mostra se o domicílio se localiza em uma cidade, Urbano, ou em uma área Rural, a seguir é feito o gráfico mostrando essa diferença. 

```
aluguel_estimado['TIPO_SITUACAO_REG'] = aluguel_estimado['TIPO_SITUACAO_REG'].replace({1: 'Urbano', 2: 'Rural'})
```
```
aluguel_estimado['TIPO_SITUACAO_REG'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Tipo de situação regional")
plt.gca().set_ylabel('')
plt.show()
```

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206636/d2152918-fa64-4597-a336-268b80d39e87) <br>
Figura 17: Gráfico “Tipo de situação regional” - Aluguel Estimado

&emsp;&emsp; O gráfico acima demonstra que mais de 73% das casas alugadas estão na cidade, enquanto 26% delas estão na zona rural. Este dado reflete que mesmo que a maioria das pessoas do Brasil moram na cidade, ainda que há um número significativo na zona rural. A seguir, o código que também segue o mesmo processo, mas com a coluna "COD_IMPUT_VALOR", mostrando se o valor do aluguel foi ou não imputado, além do gráfico do mesmo. 

```
aluguel_estimado['COD_IMPUT_VALOR'] = aluguel_estimado['COD_IMPUT_VALOR'].replace({0: ' Valor não foi imputado', 1: 'Valor foi imputado'})
```
```
aluguel_estimado['COD_IMPUT_VALOR'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("O valor do aluguel estimado foi imputado")
plt.gca().set_ylabel('')
plt.show()
```

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206636/09f50a1c-279b-485f-a812-1df4d08f3cc9) <br>
Figura 18: Gráfico “O valor do aluguel estimado foi imputado” - Aluguel Estimado

&emsp;&emsp; Com esse gráfico é possível observar que a maior parte do Brasil não teve o seu valor imputado, isso demonstra a realidade do país. 

## 2.2 Domicílio

&emsp;&emsp; O _dataset domicilio_ contém informações sobre os domicílios do Brasil. Este é composto por 38 colunas e mais de 57 mil linhas de dados. Acessando o dicionário de variáveis, foi realizado um _.replace_ em 5 colunas que foram consideradas mais importantes para uma primeira análise, o código a seguir demonstra essa mudança. 

```
aluguel_estimado['UF'] = aluguel_estimado['UF'].replace({11: 'Rondônia', 12: 'Acre', 13: 'Amazonas', 14: 'Roraima', 15: 'Pará', 16: 'Amapá', 17:'Tocantins', 21:'Maranhão', 22:'Piauí', 23:'Ceará', 24:'Rio Grande do Norte', 25:'Paraíba', 26:'Pernambuco', 27:'Alagoas', 28:'Sergipe', 29:'Bahia', 31:'Minas Gerais', 32:'Espírito Santo', 33:"Rio de Janeiro", 35:'São Paulo', 41:'Paraná', 42:'Santa Catarina', 43:'Rio Grande do Sul', 50:'Mato Grosso do Sul', 51:'Mato Grosso', 52: 'Goiás', 53:'Distrito Federal'})
```

&emsp;&emsp; Com o código acima, foi realizado a substituição dos valores inteiros para _object_. Abaixo, segue o código e o gráfico desta coluna. 

```
aluguel_estimado['UF'].value_counts().plot(kind='bar')
plt.title("Distribuição por UF")
plt.xlabel("UF")
plt.ylabel("Contagem")
plt.show()
```

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206636/d7f9607b-f1a8-4415-b53e-3a51c1f6ff72) <br>
Figura 19: Gráfico “Distribuição por UF” - Domicílio

&emsp;&emsp; Com esse gráfico, pode-se classificar que os estados com mais domicílios são, respectivamente: Minas Gerais, São Paulo e Rio de Janeiro, lembrando que isso não significa que há mais habitantes. O código a seguir foi feito o mesmo processo, só que na coluna "TIPO_SITUACAO_REG", onde mostra se o domicílio se localiza em uma cidade, Urbano, ou em uma área Rural, a seguir é feito o gráfico mostrando essa diferença. 

```
aluguel_estimado['TIPO_SITUACAO_REG'] = aluguel_estimado['TIPO_SITUACAO_REG'].replace({1: 'Urbano', 2: 'Rural'})
```
```
aluguel_estimado['TIPO_SITUACAO_REG'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Tipo de situação regional")
plt.show()
```

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206636/a2b6381c-9de0-4db5-8127-f2bfcc001e49) <br>
Figura 20: Gráfico “Tipo de situação regional” - Domicílio

&emsp;&emsp; O gráfico acima demonstra que mais de 77% das casas estão na cidade, enquanto 22% delas estão na zona rural. Este dado reflete que mesmo que a maioria das pessoas do Brasil moram na cidade, mas ainda há um número significativo na zona rural. A seguir, o código que também segue o mesmo processo, mas com a coluna "V0201", indicando o tipo de domicílio. 

```
domicilio['V0201'] = domicilio['V0201'].replace({1: 'Casa', 2: 'Apartamento', 3:'Habitação em casa de cômodos, cortiço ou cabeça de porco'})
```
```
domicilio['V0201'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Distribuição por tipo de domicilio")
plt.show()
```

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206636/6720238b-cceb-4dfe-b1a0-10c5ac80aa51) <br>
Figura 21: Gráfico “Distribuição por tipo de domicilio” - Domicílio

&emsp;&emsp; Com esse gráfico é possível observar que a maior parte da população brasileira, cerca de 90%, habita em Casa, e mais de 8% mora em Apartamento. A seguir a coluna "V0217", que indica a propriedade do domicílio, passa pelo mesmo processo.  

```
domicilio['V0217'] = domicilio['V0217'].replace({1: 'Próprio de algum morador – já pago', 2: 'Próprio de algum morador – ainda pagando', 3:'Alugado', 4:'Cedido por empregador', 5:'Cedido por familiar', 6:'Cedido de outra forma', 7:'Outra condição'})
```
```
domicilio['V0217'].value_counts().plot(kind='bar')
plt.title("Este domicilio é:")
plt.show()
```

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206636/e3a31b68-09c3-4ce6-9549-f9c7fa12a674) <br>
Figura 22: Gráfico “Propriedade do Domicílio” - Domicílio

&emsp;&emsp; Com esse gráfico pode-se concluir que grande parte da população brasileira tem casa própria, e que já está paga. A seguir a coluna "V6199", que indica o nível de segurança alimentar dentro de casa, passa pelo mesmo processo.  

```
domicilio['V6199'] = domicilio['V6199'].replace({1: 'Segurança', 2: 'Insegurança leve', 3:'Insegurança moderada', 4:'Insegurança grave'})
```
```
domicilio['V6199'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Situação de segurança alimentar")
plt.show()
```

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206636/e4f2516d-5fc1-4063-abe6-613c22f17a57) <br>
Figura 23: Gráfico “Situação de segurança alimentar” - Domicílio

&emsp;&emsp; Esse gráfico demonstra como as pessoas se sentem seguras em trazer comida dentro de casa, e pode-se observar que mais de metade se sente confortável, esse valor apesar de ser expressivo, ainda não é o ideal, porque os outros 40% ainda sofrem de alguma tipo de insegurança. O último processo é aplicar o código _.fillna_ em colunas que tem valores nulos, mas estes significam alguma coisa, que pode ser utilizado em um segundo momento da análise. É importante ressaltar que foi feita uma avaliação para entender quais valores poderiam ser substituidos. 

```
domicilio['V02101'].fillna(0, inplace=True)
domicilio['V02102'].fillna(0, inplace=True)
domicilio['V02103'].fillna(0, inplace=True)
domicilio['V02104'].fillna(0, inplace=True)
domicilio['V02105'].fillna(0, inplace=True)
domicilio['V02113'].fillna(0, inplace=True)
domicilio['V0212'].fillna(0, inplace=True)
domicilio['V0215'].fillna(0, inplace=True)
domicilio['V0219'].fillna(0, inplace=True)
```

## 2.3 Inventário

&emsp;&emsp; O _dataset inventario_ contém informações sobre bens duráveis nos domicílios do Brasil. Este é composto por 16 colunas e mais de 870 mil linhas de dados. Acessando o dicionário de variáveis, foi realizado um _.replace_ em 3 colunas que foram consideradas mais importantes para uma primeira análise, o código a seguir demonstra essa mudança. 

```
aluguel_estimado['UF'] = aluguel_estimado['UF'].replace({11: 'Rondônia', 12: 'Acre', 13: 'Amazonas', 14: 'Roraima', 15: 'Pará', 16: 'Amapá', 17:'Tocantins', 21:'Maranhão', 22:'Piauí', 23:'Ceará', 24:'Rio Grande do Norte', 25:'Paraíba', 26:'Pernambuco', 27:'Alagoas', 28:'Sergipe', 29:'Bahia', 31:'Minas Gerais', 32:'Espírito Santo', 33:"Rio de Janeiro", 35:'São Paulo', 41:'Paraná', 42:'Santa Catarina', 43:'Rio Grande do Sul', 50:'Mato Grosso do Sul', 51:'Mato Grosso', 52: 'Goiás', 53:'Distrito Federal'})
```

&emsp;&emsp; Com o código acima, foi realizado a substituição dos valores inteiros para _object_. Abaixo, segue o código e o gráfico desta coluna. 

```
aluguel_estimado['UF'].value_counts().plot(kind='bar')
plt.title("Distribuição por UF")
plt.xlabel("UF")
plt.ylabel("Contagem")
plt.show()
```

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206636/fb9fbffa-451b-4735-9d73-eb7e72539f26) <br>
Figura 24: Gráfico “Distribuição por UF” - Inventário

&emsp;&emsp; Com esse gráfico, pode-se classificar que os estados com a maior quantidade de produtos em domicílios são, respectivamente: Minas Gerais, São Paulo e Rio Grande do Sul. O código a seguir foi feito o mesmo processo, só que na coluna "TIPO_SITUACAO_REG", onde mostra se o domicílio se localiza em uma cidade, Urbano, ou em uma área Rural, a seguir é feito o gráfico mostrando essa diferença. 

```
aluguel_estimado['TIPO_SITUACAO_REG'] = aluguel_estimado['TIPO_SITUACAO_REG'].replace({1: 'Urbano', 2: 'Rural'})
```
```
aluguel_estimado['TIPO_SITUACAO_REG'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Tipo de situação regional")
plt.show()
```

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206636/ee0430e4-382e-48bd-8814-e57124cb9e2d) <br>
Figura 25: Gráfico “Tipo de situação regional” - Inventário

&emsp;&emsp; A seguir, o código que também segue o mesmo processo, mas com a coluna "V9002", indicando o tipo de domicílio. 

```
inventario['V9002'] = inventario['V9002'].replace({1: 'Monetária à vista para a Unidade de Consumo', 2: 'Monetária à vista para outra Unidade de Consumo', 3:'Monetária a prazo para a Unidade de Consumo', 4:'Monetária a prazo para outra Unidade de Consumo', 5:'Cartão de crédito à vista para a Unidade de Consumo', 6:'Cartão de crédito à vista para outra Unidade de Consumo', 7:'Doação', 8:'Retirada do Negócio', 9:'Troca', 10:'Produção Própria', 11:'Outra'})
```
```
domicilio['V0201'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Distribuição por tipo de domicilio")
plt.show()
```

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99206636/bf36861d-1c88-4253-bf21-d7ee4d0a4eec) <br>
Figura 26: Gráfico “Distribuição por tipo de domicilio” - Domicílio


## 2.4 Serviço Não Monetário 

&emsp;&emsp; O _dataset Serviço Não Monetário_ contém informações sobre a renda brasileira, destando detalhes como a região e distriubuição mensal. Acessando o dicionário de variáveis, foi realizado um _.replace_ em 2 colunas que foram consideradas mais importantes para uma primeira análise, o código a seguir demonstra essa mudança:  

```
dados['UF'] = dados['UF'].replace({11: 'Rondônia', 12: 'Acre', 13: 'Amazonas', 14: 'Roraima', 15: 'Pará', 16: 'Amapá', 17:'Tocantins', 21:'Maranhão', 22:'Piauí', 23:'Ceará', 24:'Rio Grande do Norte', 25:'Paraíba', 26:'Pernambuco', 27:'Alagoas', 28:'Sergipe', 29:'Bahia', 31:'Minas Gerais', 32:'Espírito Santo', 33:"Rio de Janeiro", 35:'São Paulo', 41:'Paraná', 42:'Santa Catarina', 43:'Rio Grande do Sul', 50:'Mato Grosso do Sul', 51:'Mato Grosso', 52: 'Goiás', 53:'Distrito Federal'})

dados
```
<em> Substituição das variáveis dos estados brasileiros </em>
<br> 

```
dados['TIPO_SITUACAO_REG'] = dados['TIPO_SITUACAO_REG'].replace({1: 'Urbano', 2: 'Rural'})

dados
```
<em> Aplicação do dicionário da região campo/urbano </em>
<br> 

GRÁFICOS: 
```
import pandas as pd
import matplotlib.pyplot as plt
import calendar

# Renomeia as colunas para facilitar o acesso
dados.rename(columns={"V9010": "mes", "RENDA_TOTAL": "renda"}, inplace=True)

# Agrupa os dados pelo mês e calcula a soma dos gastos em cada mês
gastos_por_mes = dados.groupby("mes")["renda"].sum()

# Converte os números do mês para nomes de mês usando o módulo calendar
meses = [calendar.month_name[int(mes)] for mes in gastos_por_mes.index]

# Lista de valores de gastos para o eixo y do gráfico
gastos = gastos_por_mes.values

# Cria o gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(meses, gastos, color='forestgreen')
plt.xlabel('Mês')
plt.ylabel('Renda')
plt.title('Renda por Mês')
plt.xticks(rotation=45)  # Rotaciona os rótulos do eixo x para melhor visualização
plt.tight_layout()  # Ajusta o layout para evitar cortar rótulos
plt.show()
```

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99208815/c35354ed-8f28-467c-8cef-9e587ef71a29)
<em> O gráfico acima compara a renda total dos brasileiros versus o respectivo mês do ano. O tipo de gráfico de colunas foi escolhido por conta da fácil comparação lado a lado de dados, além de não exister tantas variáveis para essa análise. Fazendo uma análise, é perceptível que a renda brasileira sofre um grande aumento no início do ano, provavelmente por conta do décimo terceiro, depois cai aos poucos e estabiliza. </em>
<br>
<br>
```
import pandas as pd
import matplotlib.pyplot as plt

# Renomeia as colunas para facilitar o acesso
dados.rename(columns={"UF": "Estado", "RENDA_TOTAL": "renda"}, inplace=True)

# Agrupa os dados pelo estado e calcula a soma dos gastos em cada estado
gastos_por_estado = dados.groupby("Estado")["renda"].sum()

# Lista de estados para o eixo x do gráfico
estados = gastos_por_estado.index.tolist()

# Lista de valores de gastos para o eixo y do gráfico
gastos = gastos_por_estado.values

# Cria o gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(estados, gastos, color='darkcyan')
plt.xlabel('Estado')
plt.ylabel('Renda')
plt.title('Renda por Estado')
plt.xticks(rotation=45)  # Rotaciona os rótulos do eixo x para melhor visualização
plt.tight_layout()  # Ajusta o layout para evitar cortar rótulos
plt.show()

```

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99208815/952ba23b-8836-41e7-992b-6e7d25a3ffff)
<em> O gráfico acima compara a renda total de cada estado brasileiro. O tipo de gráfico de colunas foi escolhido novamente por conta da fácil comparação lado a lado de dados, além de não exister tantas variáveis para essa análise. Fazendo uma análise, é perceptível que o estado de São Paulo é o mais rico (indústria), acompanhado logo em seguida pelo Mato Grosso do Sul (agropecuária). </em>

```
import pandas as pd
import matplotlib.pyplot as plt
import calendar

# Renomeia as colunas para facilitar o acesso
dados.rename(columns={"V9010": "Mes", "UF": "Estado", "RENDA_TOTAL": "renda"}, inplace=True)

# Remove linhas com valores NaN na coluna de mês
dados = dados.dropna(subset=["mes"])

# Converte os números do mês para nomes de mês usando o módulo calendar
dados["mes"] = dados["mes"].apply(lambda x: calendar.month_name[int(x)])

# Cria o gráfico de barras empilhadas para mostrar o gasto por mês em cada estado
plt.figure(figsize=(12, 6))
dados.pivot_table(index='mes', columns='Estado', values='renda', aggfunc='sum').plot(kind='bar', stacked=True)
plt.xlabel('Mês')
plt.ylabel('Renda')
plt.title('Renda por Mês e Estado')
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend(title='Estado', bbox_to_anchor=(1.05, 1), loc='upper left')  # Move a legenda para fora do gráfico
plt.show()


```

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99208815/119ce35d-cdda-4a30-be70-45a70d9c80b9)

<em> O gráfico acima compara a renda total de cada estado brasileiro versus o mês. O tipo de gráfico de colunas empilhadas foi escolhido por conta da fácil comparação lado a lado de dados agregado à subcomparação em cada coluna. Fazendo uma análise, é perceptível que alguns estados mantém um bom nível de renda durante todo ano (SP, RJ) enquanto outros não (AM).</em>

<br>

## 2.5 Restrição Produtos Serviços Saúde

&emsp;&emsp; O _dataset Restrição Produtos Serviços Saúde_ contém informações sobre as razões da população brasileira não conseguir comprar determinados produtos. Acessando o dicionário de variáveis, foi realizado um _.replace_ em 3 colunas que foram consideradas mais importantes para uma primeira análise, o código a seguir demonstra essa mudança:  

```
dados['UF'] = dados['UF'].replace({11: 'Rondônia', 12: 'Acre', 13: 'Amazonas', 14: 'Roraima', 15: 'Pará', 16: 'Amapá', 17:'Tocantins', 21:'Maranhão', 22:'Piauí', 23:'Ceará', 24:'Rio Grande do Norte', 25:'Paraíba', 26:'Pernambuco', 27:'Alagoas', 28:'Sergipe', 29:'Bahia', 31:'Minas Gerais', 32:'Espírito Santo', 33:"Rio de Janeiro", 35:'São Paulo', 41:'Paraná', 42:'Santa Catarina', 43:'Rio Grande do Sul', 50:'Mato Grosso do Sul', 51:'Mato Grosso', 52: 'Goiás', 53:'Distrito Federal'})
```
<em> Substituição das variáveis dos estados brasileiros </em>
<br> 

```
dados['TIPO_SITUACAO_REG'] = dados['TIPO_SITUACAO_REG'].replace({1: 'Urbano', 2: 'Rural'})

dados
```
<em> Aplicação do dicionário da região campo/urbano </em>
<br> 

```
dados['V9013'] = dados['V9013'].replace({1: 'Falta de dinheiro', 2: 'Indisponibilidade do produto', 3: 'Dificuldade para Chegar a algum local de aquisição', 4: 'Outros motivos'})

dados
```
<em> Dicionário para razões da não compra </em>
<br> 
GRÁFICOS:
```
import pandas as pd
import matplotlib.pyplot as plt

# Calcula as proporções dos dados usando value_counts() e normalize=True
proporcoes = dados['TIPO_SITUACAO_REG'].value_counts(normalize=True)

# Cria o gráfico de setores (pizza) com as proporções calculadas
plt.figure(figsize=(8, 8))
plt.pie(proporcoes, labels=proporcoes.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribuição de Proporção para dificuldade em Compra')
plt.show()
```
![image](https://github.com/2023M8T4Inteli/grupo2/assets/99208815/7e48bc19-f3ac-4a50-94a9-792134bc4e44)
<br>

<em> O gráfico compara a porcentagem da origem local brasileira versus o casos de dificuldade de compra. O tipo de gráfico utilizado é o de pizza por conta do baixo número de conjuntos sendo comparado (apenas 2), além disso, uma distribuição em porcentagem também complementa o gráfico. Já em uma análise, tendo em vista a baixa população rural do Brasil (16% total do país), há uma maior ocorrência proporcional de dificuldades nessa região (25%) </em>
<br>
```
import pandas as pd
import matplotlib.pyplot as plt

# Calcula as proporções totais da coluna V9013
proporcoes_totais = dados['V9013'].value_counts(normalize=True)

# Cria o gráfico de barras para mostrar as proporções totais
plt.figure(figsize=(10, 6))
proporcoes_totais.plot(kind='bar', color='skyblue')
plt.xlabel('Motivos para Não Compra')
plt.ylabel('Proporção')
plt.title('Distribuição de Dificuldade de Compra (Brasil)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

```

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99208815/28fe8441-a544-4540-9526-fef1a9b7481b)

<em> Nesse gráfico é observável que a falta de dinheiro é o principal motivo para o brasileiro não adquirir um item de consumo. O gráfico em barras tem a melhor capacidade de fazer essa comparação lado a lado</em>

```
# Filtra os dados onde o estado é 'São Paulo'
dados_sp = dados[dados['UF'] == 'São Paulo']

# Calcula as proporções totais da coluna V9013 para o estado de São Paulo
proporcoes_totais_sp = dados_sp['V9013'].value_counts(normalize=True)

# Cria o gráfico de barras para mostrar as proporções totais para São Paulo
plt.figure(figsize=(10, 6))
proporcoes_totais_sp.plot(kind='bar', color='goldenrod')
plt.xlabel('Motivos para Não Compra')
plt.ylabel('Proporção')
plt.title('Distribuição de Dificuldade de Compra em São Paulo')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

```

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99208815/389e3f75-9591-44f7-a27f-b11847c7335a)

<em> Em São Paulo, o motivo para a não compra de um produto já se altera. Ele também está muito relacionado à indisponibilidade do produto. Novamente, o gráfico de barras é o melhor para essa comparação </em>

## 2.5 Despesa Coletiva

&emsp;&emsp; O _dataset despesa coletiva_ contém informações sobre a despesa coletiva referente às famílias brasileiras. Acessando o dicionário de variáveis, foi realizado um _.replace_ em 3 colunas que foram consideradas mais importantes para uma primeira análise, o código a seguir demonstra essa mudança:  

```
dados['UF'] = dados['UF'].replace({11: 'Rondônia', 12: 'Acre', 13: 'Amazonas', 14: 'Roraima', 15: 'Pará', 16: 'Amapá', 17:'Tocantins', 21:'Maranhão', 22:'Piauí', 23:'Ceará', 24:'Rio Grande do Norte', 25:'Paraíba', 26:'Pernambuco', 27:'Alagoas', 28:'Sergipe', 29:'Bahia', 31:'Minas Gerais', 32:'Espírito Santo', 33:"Rio de Janeiro", 35:'São Paulo', 41:'Paraná', 42:'Santa Catarina', 43:'Rio Grande do Sul', 50:'Mato Grosso do Sul', 51:'Mato Grosso', 52: 'Goiás', 53:'Distrito Federal'})
```
<em> Substituição das variáveis dos estados brasileiros </em>
<br>
GRÁFICOS:
<br> 
```
import pandas as pd
import matplotlib.pyplot as plt
import calendar

# Renomeia as colunas para facilitar o acesso
dados.rename(columns={"V9010": "mes", "V8000": "gasto"}, inplace=True)

# Agrupa os dados pelo mês e calcula a soma dos gastos em cada mês
gastos_por_mes = dados.groupby("mes")["gasto"].sum()

# Converte os números do mês para nomes de mês usando o módulo calendar
meses = [calendar.month_name[int(mes)] for mes in gastos_por_mes.index]

# Lista de valores de gastos para o eixo y do gráfico
gastos = gastos_por_mes.values

# Cria o gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(meses, gastos, color='skyblue')
plt.xlabel('Mês')
plt.ylabel('Gasto')
plt.title('Gastos por Mês (Despesa Coletiva)')
plt.xticks(rotation=45)  # Rotaciona os rótulos do eixo x para melhor visualização
plt.tight_layout()  # Ajusta o layout para evitar cortar rótulos
plt.show()

```

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99208815/5409de6f-0d7f-4461-90d7-6982c7120bb9)

<em> Distribuição em gráficos da renda por mês. Comparando com gráficos anteriores de renda, é possível perceber que o gasto é proporcional à renda, reflexo do tipo de consumo brasileiro. O gráfico de barras é o melhor para essa comparação lado a lado </em>
<br>
```
import pandas as pd
import matplotlib.pyplot as plt

# Renomeia as colunas para facilitar o acesso
dados.rename(columns={"UF": "Estado", "V8000": "gasto"}, inplace=True)

# Agrupa os dados pelo estado e calcula a soma dos gastos em cada estado
gastos_por_estado = dados.groupby("Estado")["gasto"].sum()

# Lista de estados para o eixo x do gráfico
estados = gastos_por_estado.index.tolist()

# Lista de valores de gastos para o eixo y do gráfico
gastos = gastos_por_estado.values

# Cria o gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(estados, gastos, color='skyblue')
plt.xlabel('Estado')
plt.ylabel('Gasto')
plt.title('Gastos por Estado')
plt.xticks(rotation=45)  # Rotaciona os rótulos do eixo x para melhor visualização
plt.tight_layout()  # Ajusta o layout para evitar cortar rótulos
plt.show()

```

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99208815/c7198ee7-7042-4e33-89dd-6ff4a5b8746c)


<em> Distribuição em gráficos da renda por estado. Comparando com o gráficos, é possível perceber que o estado de São Paulo possuí a maior renda mas, olhando agora, o maior custo também. Essa lógica se aplica à todos os outros estados. O gráfico de barras continua sendo o melhor para comparações minuciosas assim. </em>


















