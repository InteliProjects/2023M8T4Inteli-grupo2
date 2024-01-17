# 1. Receita Federal Dados Públicos
Este pacote é dedicado ao tratamento e envio para a AWS S3 de dados relacionados à pesquisa de dados da Receita Federal referentes à renda, selecionados para atender às necessidades do projeto. Seu objetivo principal é facilitar o processamento e análise desses dados, garantindo uma integração com as ferramentas da AWS. As instruções abaixo guiarão você no uso adequado deste pacote, desde a execução dos notebooks Jupyter até a realização de testes do código.
## 1.1 Arquivos do pacote
Este é um breve guia sobre os arquivos contidos neste pacote Python.
- **.env**: Arquivo de configuração de ambiente. Contém as keys da AWS Lab. 
- **.gitignore**: Arquivo de configuração do Git para ignorar o arquivo  ``.env.tmpl`` durante o versionamento.
- **inteli.ipynb**: Jupyter Notebook principal do projeto, que contém todo o processo de tratamento dos dados CSV.
- **intelidata**: Pacote Python principal.
  - **lib.py**: Módulo Python contendo funcionalidades específicas. Aqui são definidas todas as funções de processamento utilizadas no `inteli.ipynb`.
- **requirements.txt**: Lista de dependências necessárias para executar o projeto.
  
Para executar os processos principais do projeto, utilize os seguintes notebooks Jupyter:
- **inteli.ipynb**: Este notebook contém o fluxo principal de importação dos dados CSV. Basta abrir o notebook e executar suas células para processar os dados.
- **send_esus-vepi.**: Utilize este notebook para o envio dos dados processados para o Amazon S3. Abra o notebook e execute suas células para encaminhar os arquivos CSV aos buckets da AWS S3.

  Pela alta qualidade e aplicabilidade dos dados recebidos, nenhum tipo de tratamento foi necessário, isso se deve principalmente pelo tamanho do dataset. Pressupõe-se que houve uma rigorosa verificação humana antes da sua publicação online.
### 1.2 Testes
A função a ser testada consiste em uma função de importação de dados incrementada, configurando divisões de colunas e adaptando linhas irregulares:
<br>
![image](https://github.com/2023M8T4Inteli/grupo2/assets/99208815/3df81e61-837d-43b4-8e9a-d77d77cf2f30)
<br>
Na área de manipulação, existe uma lógica booleana para gerar um output dependendo do resultado:
![image](https://github.com/2023M8T4Inteli/grupo2/assets/99208815/6905a87c-e2f9-4681-9d98-92c897894ce6)
<br>
<br>
CENÁRIO 1:
<br>
Input:
```
caminho_arquivo = 'distribuicao-renda.csv'

quadro_dados = inteli.force_read(caminho_arquivo)
```
<br>
<br>
Expectativa de Sucesso: Espera-se um output da head dos dados
<br>
<br>
Output:
<br>

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99208815/556c6918-09ae-489d-921f-7ed0e4139083)

<br>
Resultado: Sucesso!
<br>
<br>
<br>
CENÁRIO 2:
<br>
Input:

```
caminho_arquivo = null
quadro_dados = inteli.force_read(caminho_arquivo)
```
<br>
<br>
Expectativa de Sucesso: Espera-se um output da head dos dados
<br>
<br>
Output:
<br>
<br>

```
Não foi possível ler o arquivo CSV.
```
<br>
<br>
Resultado: Fracasso
<br>

## 1.3 Licença
Este pacote é distribuído sob a licença [Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
