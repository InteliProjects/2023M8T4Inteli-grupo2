## Sumário

[1. Introdução](#c1)

[2. S3 e Redshift](#c2)

[3. Atração Visual](#c2)

<br>

# <a name="c1"></a>1. Introdução

Tal documentação apresenta um panorama detalhado das práticas e estratégias adotadas em um projeto que faz uso dos serviços da Amazon Web Services (AWS), especificamente o Amazon S3 e o Amazon Redshift. A seção inicial aborda o uso do S3 e do Redshift, enfatizando a importância de seguir diretrizes específicas para a organização, manutenção e compreensão dos objetos. Estas diretrizes são essenciais para facilitar o trabalho de desenvolvedores e analistas de dados.

Na seção dedicada ao Amazon S3, são discutidos padrões de nomenclatura de buckets, estrutura de diretórios, e práticas para nomear arquivos de maneira descritiva. Estes elementos são fundamentais para a governança de dados e eficiência na gestão de projetos de dados, abrangendo aspectos como armazenamento de dados brutos, processados e backups.

Seguindo para o Amazon Redshift, o texto detalha padrões para a criação de tabelas, a importância das chaves primárias e estrangeiras para garantir a integridade referencial, e orientações para nomear views e objetos de forma clara e funcional.

Por fim, a seção sobre Atração Visual introduz um componente de visualização de dados: um mapa interativo. Este mapa é projetado para aprimorar a análise e visualização de informações relacionadas à distribuição de renda e consumo alimentício nas diferentes regiões do Brasil. A seção explora as principais características do mapa interativo, incluindo sua capacidade de exibir dados sobre renda e consumo, e sua compatibilidade com as views criadas anteriormente. Os benefícios esperados desta abordagem visual são discutidos, destacando como ela pode facilitar a compreensão de disparidades econômicas e padrões de consumo, além de auxiliar na tomada de decisões informadas e proporcionar uma experiência de usuário consistente e interativa.

# <a name="c2"></a>2. S3 e Redshift

O projeto está utilizando como parte do ppipeline os serviços S3 e Redshift da AWS, sendo necessário seguir diretrizes que auxiliam na organização, manutenção e compreensão dos objetos, facilitando o trabalho de desenvolvedores e analistas de dados. 

## 2.1. Amazon S3

**Padrão de Nomenclatura de Buckets**


- Os nomes dos buckets tem que ser únicos e descritivos.
- Utilizando prefixos do parceiro ou projeto para evitar conflitos.
- Como padrão, o ideal é os nomes estarem em letras minúsculas.
- Utilize hífens para separar palavras.

```Python
# Exemplo (empresa-projeto-dados)
integration-bigdata-cnpj
```

**Estrutura de Diretórios**

A organização dos dados em uma estrutura hierárquica é uma prática para manter a clareza na governança dos dados e otimizar a eficiência no gerenciamento de projetos de dados. Essa abordagem envolve a utilização de pastas, "raw" (bruto), "processado" e "backup", cada uma desempenhando um papel específico no ciclo de vida dos dados.

- **Raw (Bruto):**

  - **Propósito:** Armazenar os dados brutos na forma como foram adquiridos, sem transformações significativas.
  - **Benefícios:** Preserva a integridade original dos dados e facilita o reprocessamento ou recarregamento de dados brutos, se necessário.

- **Processado:**

  - **Propósito:** Armazenar dados que passaram por processamento, limpeza e transformação.
  - **Benefícios**: Fornece uma versão refinada dos dados, pronta para análises ou carregamento em sistemas de armazenamento de dados, além de facilitar consultas e análises subsequentes.

- **Backup:**

  - **Propósito:** Armazenar cópias de segurança dos dados para garantir a resiliência contra perda de dados.
  - **Benefícios:** Protege contra exclusões acidentais ou corrupção de dados e permite a recuperação rápida em caso de falhas ou incidentes.
  
```Python
# Exemplo

integration-bigdata-cnpj/
    ├── raw/
    │   ├── cnpj/
    ├── processado/
    │   ├── cnpj_agregados/
    │   └── cnpj_limpos/
    └── backup/
        └── cnpj_backup/
```

**Nomes Descritivos**

- Dê nomes descritivos aos seus arquivos.
- Utilize datas, versões ou outros identificadores.

```Python
# Exemplo
raw/cnpj/cnpj_1.csv
```

## 2.2. Amazon Redshift

**Padrão de Criação de Tabelas**

- Utilize prefixos que indiquem o propósito da tabela.

```SQL
-- Exemplo
CREATE TABLE cnpj_agregados (
    id INT,
    ...
);
```

**Chaves Primárias e Estrangeiras**

- A definição de chaves primárias e estrangeiras é fundamental para garantir integridade referencial*.

*Integridade referencial em bancos de dados relacionais é a garantia de consistência e validade nas relações entre tabelas.

```SQL
-- Exemplo

CREATE TABLE cnpj_agregados (
    cnpj_id INT PRIMARY KEY,
    ...
);

CREATE TABLE cep_regioes (
    cep_id INT PRIMARY KEY,
    cnpj_id INT REFERENCES cnpj_agregados(cnpj_id),
    ...
);
```

**Nome de Views e Objetos**

- Utilize nomes claros que indiquem a função da view/objeto.

```SQL
-- Exemplo

CREATE VIEW vw_vendas_regiao AS
SELECT
    cnpj.nome,
    COUNT(venda.venda_id) AS total_vendas
FROM
    fato_vendas venda
JOIN
    cnpj_agregados cnpj ON venda.cnpj_id = cnpj.cnpj_id
GROUP BY
    cnpj.nome;
```

# <a name="c3"></a>3. Atração Visual

Visando aprimorar a análise e visualização dos dados relacionados à distribuição de renda e consumo alimentício nas diferentes regiões do Brasil. Adicionou-se ao infográfico um mapa interativo para representação visual clara e intuitiva dessas informações. 

## 3.1. Principais características 

**Mapa Interativo**

O gráfico de mapa oferece uma interface interativa, permitindo que os usuários explorem visualmente as diferentes regiões do Brasil.

**Distribuição de Renda**

A visualização inclui dados sobre a distribuição de renda, destacando áreas com diferentes níveis econômicos por meio de cores e marcadores específicos.

**Consumo por Região**

Além da renda, o mapa também exibe informações sobre o consumo, proporcionando insights sobre padrões de gastos alimentícios em cada região.

**Compatibilidade com Views Criadas**

O gráfico de mapa é integrado de forma a suportar as views criadas anteriormente, permitindo que os usuários visualizem a distribuição de diferentes dados, por todo o território brasileiro.

## 3.2. Benefícios Esperados

**Compreensão Visual**

Facilita a compreensão das disparidades na distribuição de renda e padrões de consumo em todo o país.

**Tomada de Decisões Informada**

Capacita os usuários a tomar decisões mais informadas com base em insights visuais sobre as tendências econômicas regionais.

**Facilidade de Exploração**

A interatividade do mapa permite que os usuários explorem detalhes específicos de cada região com facilidade.

**Integração com Análises Preexistentes**

A funcionalidade está integrada de maneira coesa com as views criadas anteriormente, proporcionando uma experiência de usuário consistente.


# Observação:

Se não houver localizado informações pertinentes no presente documento, por favor, consulte o link a seguir, que direciona à documentação oficial.

<a href="https://docs.google.com/document/d/18IWwAVmbsr7sUm45ySdnJtWkj1H6QQnC/edit?usp=sharing&ouid=112389543027386593098&rtpof=true&sd=true">Documentação Oficial</a>