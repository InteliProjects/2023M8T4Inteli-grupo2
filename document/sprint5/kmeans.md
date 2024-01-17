## Sumário

[1. Introdução](#c1)

[2. Conexão com o RedShift](#c2)

[3. Criação do Gráfico de Cotovelo](#c3) 

[4. K-Means e PCA](#c4)

<br>

# <a name="c1"></a>1. Introdução

&emsp;&emsp; O método K-means é um algoritmo de clustering utilizado em análise de dados e aprendizado de máquina. Sua finalidade é agrupar dados similares em clusters, facilitando a identificação de padrões e insights nos conjuntos de dados. O algoritmo funciona particionando os dados em K clusters, onde K é um número pré-definido.

&emsp;&emsp; Neste documento, abordaremos a aplicação do método K-means em um contexto prático, utilizando dados relacionados a rendimentos e empregos por estado, pib e gini. Primeiramente, será apresentada a conexão com um banco de dados Redshift e a criação de uma view no ambiente de desenvolvimento Colab (aplicado somente para ```rendimento_emprego```). Em seguida, a criação do gráfico do cotovelo para determinar o número ideal de clusters. Por fim, o K-means em conjunto com a Análise de Componentes Principais (PCA) para visualizar e interpretar os resultados do clustering.

# <a name="c2"></a>2. Conexão com o RedShift

&emsp;&emsp; Este trecho de código estabelece uma conexão com um banco de dados Redshift, utilizado neste projeto para estruturar os dados e criar as views. Utilizando a biblioteca psycopg2, o código realiza uma consulta SQL para extrair dados específicos relacionados aos rendimentos e empregos por estado, este é uma view que foi criado no RedShift. Em seguida, os resultados são transformados em um DataFrame do pandas e salvos em um arquivo CSV. O código abaixo está disponível em: ```src/ensemble/kmeans```

Obs: este código somente é utilizado para views, já que não existe um arquivo csv para elas. 

```
dbname=''
user=''
password=''
host=''
port='' 

conn_string = f"dbname='{dbname}' user='{user}' host='{host}' port='{port}' password='{password}'"

conn = psycopg2.connect(conn_string)

cursor = conn.cursor()

query = """
SELECT
   rendimento_trabalho_.uf,
   avg(rendimento_trabalho_.renda_total) AS media_rendimento,
   count(*) AS total_empregados
FROM
   rendimento_trabalho_
WHERE
   rendimento_trabalho_.v5302 = 1
GROUP BY
   rendimento_trabalho_.uf;
"""

cursor.execute(query)

colunas = [desc[0] for desc in cursor.description]
resultados = cursor.fetchall()
df = pd.DataFrame(resultados, columns=colunas)

cursor.close()
conn.close()

caminho_do_arquivo_csv = './dados/nome.csv'  # Substitua pelo caminho desejado
df.to_csv(caminho_do_arquivo_csv, index=False)
```

# <a name="c3"></a>3. Criação do Gráfico do Cotovelo

&emsp;&emsp; O código abaixo aborda a determinação do número ideal de clusters (K) através da criação do gráfico do cotovelo. A soma dos quadrados das distâncias dos pontos ao centróide (inércia) é calculada para diferentes valores de K, e o gráfico resultante ajuda a identificar o ponto de inflexão, indicando o número ótimo de clusters. O código abaixo está disponível em: ```src/ensemble/kmeans```

```
df = pd.read_csv('./dados/nome_arquivo.csv')

X = df[['media_rendimento', 'total_empregados']]

inercias = []

K_range = range(1, 11)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    inercias.append(kmeans.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(K_range, inercias, '-o')
plt.title('Método do Cotovelo para Determinar o Número Ideal de Clusters')
plt.xlabel('Número de Clusters (K)')
plt.ylabel('Inércia')
plt.xticks(K_range)
plt.show()
```

# <a name="c4"></a>4. K-means e PCA

&emsp;&emsp; Por último, o código aplica o método K-means em conjunto com a Análise de Componentes Principais (PCA). Os dados são escalados e reduzidos para duas dimensões usando PCA, facilitando a visualização. Em seguida, o K-means é aplicado aos componentes principais para realizar a clusterização. O código abaixo está disponível em: ```src/ensemble/kmeans```

```
dados = pd.read_csv('./dados/visao_media_rendimento_emprego_por_estado.csv')

X = dados[['media_rendimento', 'total_empregados']]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA(n_components=2)  # Reduzir para 2 componentes para visualização 2D
X_pca = pca.fit_transform(X_scaled)

kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_pca)

dados['PCA1'] = X_pca[:, 0]
dados['PCA2'] = X_pca[:, 1]
dados['Cluster'] = kmeans.labels_

plt.figure(figsize=(10, 8))
scatter = plt.scatter(dados['PCA1'], dados['PCA2'], c=dados['Cluster'], cmap='viridis', s=100)

offset_x = 0.1  # Deslocamento na direção x
offset_y = 0.1  # Deslocamento na direção y

for i, uf in enumerate(dados['uf']):
    plt.text(dados['PCA1'].iloc[i] + offset_x, dados['PCA2'].iloc[i] + offset_y, str(uf), ha='right', va='center')

plt.title('Rendimento e emprego por estado')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.legend(*scatter.legend_elements(), title="Clusters")
plt.show()
```

# Observação:

Se não houver localizado informações pertinentes no presente documento, por favor, consulte o link a seguir, que direciona à documentação oficial.

<a href="https://docs.google.com/document/d/18IWwAVmbsr7sUm45ySdnJtWkj1H6QQnC/edit?usp=sharing&ouid=112389543027386593098&rtpof=true&sd=true">Documentação Oficial</a>