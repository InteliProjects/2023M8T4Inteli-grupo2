# Documentação da Estrutura de Ingestão de Dados com Armazenamento

# Etapas de extração dos dados 
# Mapear fluxos do ETL

# Serviços da AWS e justificar as escolhas 
A Amazon Web Services (AWS) é uma plataforma de serviços em nuvem. Ela disponibiliza uma extensa gama de serviços, abrangendo armazenamento de dados, computação, análise de dados, aprendizado de máquina, etc. 
<br>
<br>
Para o atual estágio do projeto, o serviço do S3 (Amazon Simple Storage Service) pareceu o mais adequado. A sua organização de dados se dá através do "buckets": containers virtuais que armazenam os dados da solução. Essa atividade é essencial por conta da dispersão dos dados das fontes disponibilizadas, a aplicação do S3 é exatamente um meio para reuni-los.
<br>
<br>
As principais vantagens do S3 são sua confiabilidade e escalabilidade. Essa solução de armazenamento em nuvem oferece alta disponibilidade, durabilidade e capacidade de escalonamento para atender às demandas significativas de armazenamento de dados. Além disso, os recursos avançados de segurança e gerenciamento de acesso tornam o S3 uma escolha confiável para garantir a integridade e a privacidade dos dados. 
<br>
<br>
![image](https://github.com/2023M8T4Inteli/grupo2/assets/99208815/9d364283-651a-43b2-b523-ebe4d47489c1)



# Aspectos de segurança
Estamos implementando uma robusta arquitetura de ingestão de dados com armazenamento, utilizando a tecnologia IAM (Identity and Access Management) da AWS, uma tecnologia que oferece uma camada adicional de segurança através da dupla autenticação. Este sistema de autenticação é projetado para atender as diferentes necessidades dos funcionários e por envolver dois métodos distintos. O primeiro método é destinado aos analistas de dados e consultores de marketing e vendas da integration em que a autenticação se baseia em um login de usuário e senha, fornecendo uma camada inicial de segurança. Esta abordagem visa simplificar o acesso para usuários que necessitam de informações específicas e têm a necessidade de interação com diferentes partes do sistema.
<br> 
<br> 

Além disso, para um nível de segurança mais avançado, foi implementada uma segunda autenticação exclusiva para os analistas de dados. Essa autenticação abrange todo o código do sistema, garantindo que apenas usuários autorizados tenham acesso total às informações contidas na plataforma. 
Vale ressaltar que, considerando a diversidade de habilidades técnicas, os consultores de vendas e marketing terão acesso a um formato mais visual e intuitivo das informações por meio de um infográfico. Essa abordagem proporciona uma interface simplificada que atende às suas necessidades específicas.
Dessa forma, entendemos a importância da conformidade e segurança na gestão de dados então tivemos bastante cautela e cuidado para garantir a integridade e confidencialidade dos dados. Assim, agindo com as melhores práticas de segurança da AWS, abrangendo criptografia de dados, controle de acesso e monitoramento proativo. Consequentemente oferecendo uma plataforma que não apenas atenda aos padrões de segurança exigidos por muitos, mas também que dê maior confiança aos usuários da nossa solução. 

<br> 

![image](https://github.com/2023M8T4Inteli/grupo2/assets/99209712/9ca98b75-bfa3-49ab-8b15-ac6642ce3591)
Figura XX: IAM - AWS

# Plano de monitoramento e gerenciamento da estrutura de ETL.

# 
 
