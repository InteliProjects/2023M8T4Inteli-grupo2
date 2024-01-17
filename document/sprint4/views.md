## Sumário

[1. Introdução](#c1)

[2. Aréas com maior demanda](#c2)

[3. Identificar as categorias de produtos mais vendidas em cada estado](#c3)

[4. Empresas com a maior quantidade de vendas em um período específico](#c4)

[5. Potencial de Expansão Empresarial](#c5)

[6. Encontrar as Empresas com o Maior Valor Total de Vendas](#c6)

[7. Análise de Correlação entre Número de Estabelecimentos e Valor Total de Vendas](#c7)

[8. Empresas com a Maior Quantidade de Estabelecimentos](#c8)

[9. Correlação Econômica no Setor Alimentício](#c9)

[10. Produtos mais consumidos em diferentes classes sociais](#c10)

[11. Quantidade de CNPJs com determinados CNAEs](#c11)

[12. Quantidade de estabelecimentos alimentícios por estados brasileiros](#c12)

[13. CNAES mais presentes por estados brasileiros](#c13)

<br>

# <a name="c1"></a>1. Introdução

### Descrição
&emsp;&emsp; No Amazon Redshift, as _views_ são estruturas que permitem aos usuários criar consultas predefinidas e reutilizáveis. Elas são essencialmente consultas salvas como objetos no banco de dados, proporcionando uma maneira de organizar e simplificar consultas complexas. 

# <a name="c2"></a>2. Aréas com maior demanda

### Descrição
&emsp;&emsp; A view _alimentos_mais_consumidos_por_estado_ agrega dados da tabela ```consumo_alimentar_pof```, contabilizando a quantidade de alimentos consumidos e o total de gramas por estado. A ordenação é feita pela quantidade de alimentos consumidos em ordem decrescente.

```
CREATE VIEW alimentos_mais_consumidos_por_estado AS
SELECT
    unidade_federacao_translated,
    codigo_alimento_traduzido,
    COUNT(*) AS qnt_alimentos_consumidos,
    SUM(qnt_gramas) AS total_gramas_consumidos
FROM
    consumo_alimentar_pof
GROUP BY
    unidade_federacao_translated,
    codigo_alimento_traduzido
ORDER BY
    unidade_federacao_translated,
    qnt_alimentos_consumidos DESC;
```

# <a name="c3"></a>3. Identificar as categorias de produtos mais vendidas em cada estado

### Descrição
&emsp;&emsp; A view _categorias_mais_vendidas_por_estado_ conecta informações de três tabelas: ```cnpjs # deve ser aplicado nos 5 arquivos```, ```dados_sale```, e ```dados_categoria```. Esta apresenta o número de vendas por categoria, agrupadas por estado (sigla_uf), com ordenação descendente pelo número de vendas.

```
CREATE VIEW categorias_mais_vendidas_por_estado AS
SELECT
    c.sigla_uf AS Estado,
    cat.id AS IdCategoria,
    cat.nome_categoria,
    COUNT(*) AS VendasPorCategoria
FROM
    cnpjs_4 c
JOIN
    dados_sale s ON c.idCNPJ = s.idCNPJ  -- Assumindo que há uma coluna que vincula CNPJ com vendas
JOIN
    dados_category cat ON s.idCategory = cat.id
GROUP BY
    c.sigla_uf,
    cat.id,
    cat.nome_categoria
ORDER BY
    c.sigla_uf,
    VendasPorCategoria DESC;
```


# <a name="c4"></a>4. Empresas com a maior quantidade de vendas em um período específico

### Descrição
&emsp;&emsp; Esta _view_ calcula a soma de vendas para cada CNPJ e nome fantasia da tabela ```cnpjs # deve ser aplicado nos 5 arquivos``` e ```dados_sale```. A condição WHERE filtra as vendas para o intervalo de datas entre janeiro de 2021 e dezembro de 2022. Os resultados são ordenados pela soma de vendas em ordem decrescente.

```
SELECT
    c.cnpj,
    c.nome_fantasia,
    SUM(s.total_vendas) AS soma_vendas
FROM
    cnpjs_4 c
JOIN
    dados_sale s ON c.cnpj = s.cnpj
WHERE
    s.data_venda BETWEEN DATE '2021-01-01' AND DATE '2022-12-31'  -- Exemplo para os últimos dois anos
GROUP BY
    c.cnpj,
    c.nome_fantasia
ORDER BY
    soma_vendas DESC;
```

# <a name="c5"></a> 5. Potencial de Expansão Empresarial

### Descrição
&emsp;&emsp; A _view_ `potencial_expansao_empresarial` é projetada para identificar áreas com potencial para expansão empresarial no setor de supermercados. Ela correlaciona o consumo de alimentos em gramas com o número de supermercados existentes em cada unidade federativa. Esta análise é feita cruzando dados da tabela `consumo_alimentar_pof` com informações de empresas da tabela `cnpj1`, filtrando especificamente pelo CNAE de supermercados.

### Consulta SQL
```sql
CREATE OR REPLACE VIEW "public"."potencial_expansao_empresarial" AS
SELECT
    p.unidade_federacao,
    p.codigo_alimento_traduzido,
    SUM(p.qnt_gramas) AS total_consumo,
    COUNT(c.cnpj) AS total_empresas,
    p.unidade_federacao_translated
FROM
    consumo_alimentar_pof p
    LEFT JOIN cnpj1 c ON p.unidade_federacao = c.sigla_uf AND c.cnae_fiscal_principal = '4711-3/02'
GROUP BY
    p.unidade_federacao,
    p.codigo_alimento_traduzido,
    p.unidade_federacao_translated;
```
### Detalhes da View

- **Objetivo**: Identificar regiões com alta demanda por produtos alimentícios e menor densidade de supermercados.
- **Dados Utilizados**: Combinação de dados de consumo de alimentos (tabela `consumo_alimentar_pof`) com a presença de empresas do setor de supermercados (tabela `cnpj1`).
- **Agrupamento e Ordenação**: Os dados são agrupados por unidade federativa e código de alimento traduzido, e a ordenação é feita pela unidade federativa e pelo total de consumo.
- **Filtro Específico**: Utiliza o CNAE '4711-3/02' para focar em supermercados.


# <a name="c6"></a> 6. Encontrar as Empresas com o Maior Valor Total de Vendas

### Descrição
&emsp;&emsp; Esta _view_ identifica as empresas com o maior valor total de vendas. A análise é realizada ao agregar os dados de vendas de cada empresa e somar os valores totais, proporcionando uma visão clara das empresas com maior volume de vendas.

### Consulta SQL
```sql
CREATE VIEW empresas_maior_valor_vendas AS
SELECT
    c.cnpj,
    SUM(d.value) AS total_vendas
FROM
    cnpj1 c
    JOIN dados_sale d ON c.cnpj = d.cnpj
GROUP BY
    c.cnpj
ORDER BY
    total_vendas DESC;
```
### Detalhes da View

- **Objetivo**: Identificar as empresas com o maior volume total de vendas.
- **Dados Utilizados**: Combinação dos dados de vendas (tabela `dados_sale`) com as informações das empresas (tabela `cnpj1`).
- **Agrupamento e Ordenação**: Os dados são agrupados por CNPJ e ordenados pelo valor total de vendas em ordem decrescente.
- **Cálculo de Vendas**: A soma dos valores de vendas (`SUM(d.value)`) representa o volume total de vendas para cada empresa.

# <a name="c7"></a> 7. Análise de Correlação entre Número de Estabelecimentos e Valor Total de Vendas

### Descrição
&emsp;&emsp; Esta _view_ explora a possível correlação entre o número de estabelecimentos de uma empresa e seu valor total de vendas. A análise é realizada combinando dados de vendas e o número de estabelecimentos para cada empresa.

### Consulta SQL
```sql
CREATE OR REPLACE VIEW "public"."correlacao_vendas_estabelecimentos" AS
SELECT
    c.cnpj,
    SUM(s.value) AS total_vendas,
    COUNT(e.cnpj) AS numero_estabelecimentos
FROM
    cnpj1 c
    LEFT JOIN dados_sale s ON c.cnpj = s.cnpj
    LEFT JOIN dados_establishment e ON c.cnpj = e.cnpj
GROUP BY
    c.cnpj;
```
### Detalhes da View

- **Objetivo**: Avaliar se existe uma correlação entre o número de estabelecimentos que uma empresa possui e seu valor total de vendas.
- **Dados Utilizados**: Integração de dados de vendas (tabela `dados_sale`), informações das empresas (tabela `cnpj1`) e dados de estabelecimentos (tabela `dados_establishment`).
- **Agrupamento**: Os dados são agrupados por CNPJ para calcular o total de vendas e o número de estabelecimentos para cada empresa.
- **Análise**: A correlação é analisada observando-se as tendências entre o volume total de vendas e o número de estabelecimentos.


# <a name="c8"></a> 8. Empresas com a Maior Quantidade de Estabelecimentos

### Descrição
&emsp;&emsp; Esta _view_ identifica as empresas com a maior quantidade de estabelecimentos. Utiliza dados da tabela `cnpj1` para contar e listar as empresas com base no número de estabelecimentos que possuem, proporcionando uma visão clara das empresas com a maior presença física.

### Consulta SQL
```sql
CREATE OR REPLACE VIEW "public"."empresas_maior_quantidade_estabelecimentos" AS
SELECT
    c.cnpj,
    COUNT(e.cnpj) AS total_estabelecimentos
FROM
    cnpj1 c
    LEFT JOIN dados_establishment e ON c.cnpj = e.cnpj
GROUP BY
    c.cnpj
ORDER BY
    total_estabelecimentos DESC;
```
### Detalhes da View

- **Objetivo**: Identificar as empresas com o maior número de estabelecimentos.
- **Dados Utilizados**: Integração dos dados das empresas (tabela `cnpj1`) com os dados de estabelecimentos (tabela `dados_establishment`).
- **Agrupamento e Ordenação**: Os dados são agrupados por CNPJ, com uma contagem do número de estabelecimentos, e ordenados em ordem decrescente do total de estabelecimentos.
- **Utilidade da Análise**: A view é útil para análises de mercado e estratégias de expansão, identificando empresas com ampla presença no mercado.


# <a name="c9"></a> 9. Correlação Econômica no Setor Alimentício

### Descrição
&emsp;&emsp; Esta _view_ analisa a correlação entre a saúde econômica das regiões (como representada pela renda média) e a presença de empresas do setor alimentício. Utiliza dados do consumo alimentar da POF e informações do CNPJ para investigar essa relação.

### Consulta SQL
```sql
CREATE OR REPLACE VIEW "public"."correlacao_economica_setor_alimenticio" AS
SELECT
   p.unidade_federacao,
   AVG(p.renda_bruta_mensal_total) AS media_renda,
   COUNT(c.cnpj) AS total_empresas_alimenticias,
   p.unidade_federacao_translated
FROM
   consumo_alimentar_pof p
   LEFT JOIN cnpj1 c ON p.unidade_federacao:: text = c.sigla_uf:: text
   AND c.cnae_fiscal_principal:: text = '4711-3/02':: text
GROUP BY
   p.unidade_federacao,
   p.unidade_federacao_translated;
```

### Detalhes da View

- **Objetivo**: Analisar a relação entre a saúde econômica de regiões (renda) e a presença de empresas do setor alimentício.
- **Dados Utilizados**: Combinação dos dados econômicos da POF (tabela `consumo_alimentar_pof`) com informações das empresas (tabela `cnpj1`).
- **Filtro de Dados**: Utilização do CNAE '4711-3/02' para focar em supermercados.
- **Análise Realizada**: A correlação é avaliada observando a média de renda e o número total de empresas alimentícias em cada unidade federativa.


## <a name="c10"></a>10. Produtos mais consumidos em diferentes classes sociais

### Descrição
A _view_ `produtos_mais_consumidos_classe_a` tem como objetivo identificar os alimentos mais consumidos por domicílios da classe A, onde a renda bruta mensal total é superior a R$ 22.000,00. A consulta utiliza dados da tabela `consumo_alimentar_pof` e `outros_rendimentos`.

### Consulta SQL
```sql
CREATE OR REPLACE VIEW "public"."produtos_mais_consumidos_classe_a" AS
SELECT
   cap.codigo_alimento_traduzido,
   count(cap.codigo_alimento_traduzido) AS quantidade_consumida
FROM
   consumo_alimentar_pof cap
   JOIN outros_rendimentos orr ON cap.numero_domicilio = orr.numero_domicilio
WHERE
   orr.renda_bruta_mensal_total > 22000:: double precision
GROUP BY
   cap.codigo_alimento_traduzido
ORDER BY
   count(cap.codigo_alimento_traduzido) DESC
LIMIT
   10;
```
### Detalhes da View
- **Objetivo:** Identificar os 10 alimentos mais consumidos por domicílios da classe A.
- **Dados Utilizados:** Tabelas consumo_alimentar_pof e outros_rendimentos.
- **Filtragem Específica:** Considera apenas domicílios com renda bruta mensal total superior a R$ 22.000,00.
- **Agrupamento e Ordenação:** Agrupa por código de alimento traduzido e ordena pela quantidade consumida em ordem decrescente.

## <a name="c11"></a>11. Quantidade de CNPJs com determinados CNAEs

Descrição
A view quantidade_cnpjs_por_cnae tem como objetivo contabilizar a quantidade de CNPJs por categoria de CNAE fiscal principal. A consulta utiliza dados de várias tabelas, como cnpj1, cnpj2, cnpj3, cnpj4, e cnpj5.

### Consulta SQL
``` sql
CREATE OR REPLACE VIEW "public"."quantidade_cnpjs_por_cnae" AS
SELECT
  CASE
  WHEN all_cnpjs.cnae_fiscal_principal:: text = '5611201':: text THEN 'Restaurantes e Similares':: text
  WHEN all_cnpjs.cnae_fiscal_principal:: text = '4711301':: text THEN 'Minimercados, Mercearias e Armazéns':: text
  -- ... (outros casos) ...
  ELSE 'Outros':: text END AS nome_cnae,
  count(DISTINCT all_cnpjs.cnpj) AS quantidade_total_cnpjs
FROM
  (
    -- União de CNPJs de várias tabelas
  ) all_cnpjs
GROUP BY
  CASE
  WHEN all_cnpjs.cnae_fiscal_principal:: text = '5611201':: text THEN 'Restaurantes e Similares':: text
  WHEN all_cnpjs.cnae_fiscal_principal:: text = '4711301':: text THEN 'Minimercados, Mercearias e Armazéns':: text
  -- ... (outros casos) ...
  ELSE 'Outros':: text END;
```
### Detalhes da View
- **Objetivo:**  Contar a quantidade total de estabelecimentos por estado.
- **Dados Utilizados:** Combinação de CNPJs de diferentes tabelas (cnpj1, cnpj2, cnpj3, cnpj4, e cnpj5).
- **Agrupamento e Ordenação:** Agrupa por categoria de CNAE e conta a quantidade total de CNPJs.

## <a name="c12"></a>12. Quantidade de estabelecimentos alimentícios por estados brasileiros
### Descrição
A view quantidade_estabelecimentos_por_estado visa contabilizar a quantidade total de estabelecimentos por estado. A consulta utiliza dados de várias tabelas, como cnpj1, cnpj2, cnpj3, cnpj4, e cnpj5.

### Consulta SQL
```sql
CREATE
OR REPLACE VIEW "public"."quantidade_estabelecimentos_por_estado" AS
SELECT
  all_estabelecimentos.sigla_uf,
  count(DISTINCT all_estabelecimentos.cnpj) AS quantidade_total_estabelecimentos,
  CASE
  WHEN all_estabelecimentos.sigla_uf:: text = 'RO':: text THEN 11
  WHEN all_estabelecimentos.sigla_uf:: text = 'AC':: text THEN 12
  WHEN all_estabelecimentos.sigla_uf:: text = 'AM':: text THEN 13
  WHEN all_estabelecimentos.sigla_uf:: text = 'RR':: text THEN 14
  WHEN all_estabelecimentos.sigla_uf:: text = 'PA':: text THEN 15
  WHEN all_estabelecimentos.sigla_uf:: text = 'AP':: text THEN 16
  WHEN all_estabelecimentos.sigla_uf:: text = 'TO':: text THEN 17
  WHEN all_estabelecimentos.sigla_uf:: text = 'MA':: text THEN 21
  WHEN all_estabelecimentos.sigla_uf:: text = 'PI':: text THEN 22
  WHEN all_estabelecimentos.sigla_uf:: text = 'CE':: text THEN 23
  WHEN all_estabelecimentos.sigla_uf:: text = 'RN':: text THEN 24
  WHEN all_estabelecimentos.sigla_uf:: text = 'PB':: text THEN 25
  WHEN all_estabelecimentos.sigla_uf:: text = 'PE':: text THEN 26
  WHEN all_estabelecimentos.sigla_uf:: text = 'AL':: text THEN 27
  WHEN all_estabelecimentos.sigla_uf:: text = 'SE':: text THEN 28
  WHEN all_estabelecimentos.sigla_uf:: text = 'BA':: text THEN 29
  WHEN all_estabelecimentos.sigla_uf:: text = 'MG':: text THEN 31
  WHEN all_estabelecimentos.sigla_uf:: text = 'ES':: text THEN 32
  WHEN all_estabelecimentos.sigla_uf:: text = 'RJ':: text THEN 33
  WHEN all_estabelecimentos.sigla_uf:: text = 'SP':: text THEN 35
  WHEN all_estabelecimentos.sigla_uf:: text = 'PR':: text THEN 41
  WHEN all_estabelecimentos.sigla_uf:: text = 'SC':: text THEN 42
  WHEN all_estabelecimentos.sigla_uf:: text = 'RS':: text THEN 43
  WHEN all_estabelecimentos.sigla_uf:: text = 'MS':: text THEN 50
  WHEN all_estabelecimentos.sigla_uf:: text = 'MT':: text THEN 51
  WHEN all_estabelecimentos.sigla_uf:: text = 'GO':: text THEN 52
  WHEN all_estabelecimentos.sigla_uf:: text = 'DF':: text THEN 53
  ELSE NULL:: integer END AS codigo_estado
FROM
  (
    (
      (
        (
          SELECT
            cnpj1.cnpj,
            cnpj1.sigla_uf
          FROM
            cnpj1
          UNION ALL
          SELECT
            cnpj2.cnpj,
            cnpj2.sigla_uf
          FROM
            cnpj2
        )
        UNION ALL
        SELECT
          cnpj3.cnpj,
          cnpj3.sigla_uf
        FROM
          cnpj3
      )
      UNION ALL
      SELECT
        cnpj4.cnpj,
        cnpj4.sigla_uf
      FROM
        cnpj4
    )
    UNION ALL
    SELECT
      cnpj5.cnpj,
      cnpj5.sigla_uf
    FROM
      cnpj5
  ) all_estabelecimentos
GROUP BY
  all_estabelecimentos.sigla_uf;
```
### Detalhes da View
- **Objetivo:** Contar a quantidade de CNPJs por categoria de CNAE fiscal principal.
- **Dados Utilizados:** Combinação de estabelecimentos de diferentes tabelas (cnpj1, cnpj2, cnpj3, cnpj4, e cnpj5).
- **Agrupamento e Ordenação:** Agrupa por sigla do estado e conta a quantidade total de estabelecimentos.
- **Código do Estado:** Atribui códigos numéricos aos estados para facilitar análises.

## <a name="c13"></a>13. CNAES mais presentes por estados brasileiros 
### Descrição
A view top_3_cnaes_por_estado identifica os três CNAEs (Classificação Nacional de Atividades Econômicas) principais com a maior quantidade de estabelecimentos por estado. A consulta utiliza dados de várias tabelas, como cnpj1, cnpj2, cnpj3, cnpj4, e cnpj5.

### Consulta sql 
```sql
CREATE
OR REPLACE VIEW "public"."top_3_cnaes_por_estado" AS
SELECT
  top_cnaes.sigla_uf,
  top_cnaes.cnae_fiscal_principal,
  top_cnaes.quantidade_estabelecimentos,
  top_cnaes.rank
FROM
  (
    SELECT
      ranked_cnaes.sigla_uf,
      ranked_cnaes.cnae_fiscal_principal,
      ranked_cnaes.quantidade_estabelecimentos,
      pg_catalog.rank() OVER(
        PARTITION BY ranked_cnaes.sigla_uf
        ORDER BY
          ranked_cnaes.quantidade_estabelecimentos DESC
      ) AS rank
    FROM
      (
        SELECT
          all_estabelecimentos.sigla_uf,
          all_estabelecimentos.cnae_fiscal_principal,
          count(DISTINCT all_estabelecimentos.cnpj) AS quantidade_estabelecimentos
        FROM
          (
            (
              (
                (
                  SELECT
                    cnpj1.cnpj,
                    cnpj1.sigla_uf,
                    cnpj1.cnae_fiscal_principal
                  FROM
                    cnpj1
                  UNION ALL
                  SELECT
                    cnpj2.cnpj,
                    cnpj2.sigla_uf,
                    cnpj2.cnae_fiscal_principal
                  FROM
                    cnpj2
                )
                UNION ALL
                SELECT
                  cnpj3.cnpj,
                  cnpj3.sigla_uf,
                  cnpj3.cnae_fiscal_principal
                FROM
                  cnpj3
              )
              UNION ALL
              SELECT
                cnpj4.cnpj,
                cnpj4.sigla_uf,
                cnpj4.cnae_fiscal_principal
              FROM
                cnpj4
            )
            UNION ALL
            SELECT
              cnpj5.cnpj,
              cnpj5.sigla_uf,
              cnpj5.cnae_fiscal_principal
            FROM
              cnpj5
          ) all_estabelecimentos
        GROUP BY
          all_estabelecimentos.sigla_uf,
          all_estabelecimentos.cnae_fiscal_principal
      ) ranked_cnaes
  ) top_cnaes
WHERE
  top_cnaes.rank <= 3;
```
### Detalhes da View
- **Objetivo:** Identificar os três CNAEs principais com a maior quantidade de estabelecimentos por estado.
- **Dados Utilizados:** Combinação de estabelecimentos de diferentes tabelas (cnpj1, cnpj2, cnpj3, cnpj4, e cnpj5).
- **Agrupamento e Ordenação:** Agrupa por sigla do estado e CNAE fiscal principal, contando a quantidade total de estabelecimentos. Em seguida, atribui um rank com base na quantidade de estabelecimentos por estado.
- **Filtro do Top 3:** A view retorna apenas os três principais CNAEs por estado, ordenados pela quantidade de estabelecimentos.
