![FoodCare](https://lh3.googleusercontent.com/dr4TtJKIvmdQJBv1aRgMM2lt-0MvwHLiPintF255CDc3JJBw1iKIYUaNqO6aBimgvJgGcw=s141 )
# Documento de Visão
## Historico de versão
 Data | Versão | Descrição | Autor
 ---- | ------ | --------- | -----
05/09/19 | 1.0 | Abertura do documento, criação da introdução e Posicionamento | Giovanna
07/09/19 | 1.1 | Atualização da introdução e do posicionamento | Giovanna
07/09/19 | 1.1 | Criação da descrição da Parte Interessada e do Usuário | Rafaella
07/09/19 | 1.1 | Criação do tópico Visão Geral do Produto | Geraldo
07/09/19 | 1.1 | Criação do tópico Recursos do Produto | Hugo
07/09/19 | 1.1 | Criação do tópico Outros Requisitos do Produto | Lucas

# Índice
1. [Introdução](#1)
    1. [Referências](#1.1)
2. [Posicionamento](#2)
    1. [Descriação do problema](#2.1)
    2. [Posição do produto](#2.2)
3. [Descrição dos envolvidos e usuários](#3)
    1. [Perfil da parte interessada](#3.1)
    2. [Perfil do usuário](#3.2)
    3. [Demográfico de Mercado](#3.3)
    4. [Alternativas e Concorrência](#3.4)
4. [Visão Geral do Produto](#4)
    1. [Perspectivas do produto](#4.1)
    2. [Resumo das Capacidades](#4.2)
    3. [Suposições de dependências](#4.3)
    4. [Custo e precificação](#4.4)
    5. [Licenciamento e Instalação](#4.5)
5. [Recursos do produto](#5)
    1. [Cadastro](#5.1)
    2. [Criar evento](#5.2)
    3. [Pesquisar evento](#5.3)
    4. [Tipificar alimento](#5.4)
    5. [Login](#5.5)
    6. [Notificações](#5.6)
6. [Outros requisitos do produto](#6)
    1. [Requisito de usuário](#6.1)
    2. [Requisito do sistema](#6.2)

# Introdução <a name="1"></a>
Este documento tem como propósito coletar, analisar e definir necessidades e recursos de nível superior do FoodCare para a matéria Métodos de Desenvolvimento de Software (MDS) que tem como tema à Objetivos de Desenvolvimento Sustentável (ODS) 2.1. Esse objetivo defende: Fome Zero e Agricultura Sustentável - Acabar com a fome, alcançar a segurança alimentar e melhoria da nutrição e promover a agricultura sustentável.

Nesse objetivo a meta 2.1 especifica que: até 2030, irá acabar com a fome e garantir o acesso de todas as pessoas, em particular os pobres e pessoas em situações vulneráveis, incluindo crianças, a alimentos seguros, nutritivos e suficientes durante todo o ano.

O programa desenvolvido tem como intuito facilitar o acesso a alimentos para famílias em situação de risco e organizações não governamentais que distribuem comida.

## Referências <a name="1.1"></a>
* ONU. **Agenda 2030** [<http://www.agenda2030.org.br/ods/2/>](http://www.agenda2030.org.br/ods/2/). Acesso em 5 de setembro de 2019.
* Copia. **Waste Less. Feed More**. [<http://www.gocopia.com/>](http://www.gocopia.com/>). Acesso em 5 de setembro de 2019;

# Posicionamento <a name="2"></a>
## Descrição do Problema <a name="2.1"></a>
O problema é a quantidade de comida que restaurantes e/ou mercados jogam fora por deixarem de estar fresco e/ou vencido. Isso faz com que muita comida seja desperdiçada, enquanto muitas famílias carentes não conseguem garantir alimentação durante o mês.

Uma solução para essa situação é garantir que a comunidade carecida  e/ou ONG’s tenha conhecimento de quais restaurantes e/ou mercados estão doando comida.

## Posição do produto <a name="2.2"></a>
Para a comunidade que carece de recursos alimentícios. O FoodCare é uma aplicação web que facilita o acesso a comida doada. De outro modo o Cópia, além de necessitar de número de telefone internacional, é um aplicativo que deve ser baixado,  nosso FoodCare é um Progressive Web App (PWA) e não precisa instalar nenhum aplicativo. Além de oferecer notificações específicas para cada usuário cadastrado.

# Descrições dos envolvidos e usuários <a name="3"></a>
O produto visa facilitar a interação entre aqueles que possuem recursos alimentícios a serem doados e aqueles que necessitam desses produtos. Desta forma, o FoodCare terá usuários doadores e usuários receptores,  visando minimizar o problema relacionado ao desperdício de alimentos.
## Perfil da Parte Interessada <a name="3.1"></a>
* Representante: Doadores
* Descrição: O usuário doador trat

O usuário doador trata-se de supermercados e restaurantes dispostos a doar alimentos que não serão mais destinados ao que foram propostos, como alimentos perto do vencimento da validade ou sobras de “comida limpa” nos restaurantes.

* Envolvimento no projeto: Cadastrar o recurso que será disponibilizado a fim de destiná-los da melhor maneira e iniciar um evento que indique o período em que esse recurso será disponibilizado.

## Perfil do usuário <a name="3.2"></a>

* Representante: Receptor
* Descrição: O usuário receptor trata-se de ONG’s ou pessoas físicas interessadas em captar o recurso alimentício que será disponibilizado pelo doador a fim de distribuir esse alimento às pessoas necessitadas.
* Envolvimento no projeto: Cadastrar seu email para ser notificada quando um doador iniciar um evento.

## Demográficos de Mercado <a name="3.3"></a>
Atualmente, os alimentos que perdem o prazo de validade ou refeições prontas e não consumidas em restaurantes são descartados. Estima-se que por ano, no Brasil, mais de 26 milhões de toneladas de comida sejam jogadas fora.

O FoodCare ao oferecer um serviço de integração entre o doador e o receptor, faz o papel de destinar o alimento que seria perdido àqueles que necessitam.
## Alternativas e Concorrência <a name="3.4"></a>
A vantagem competitiva do FoodCare se dá no fato de poder ser acessado em qualquer rede desde que haja acesso à internet, sem a obrigatoriedade da instalação de um aplicativo.

Concorrência:
* Olio: aplicativo que conecta vizinhos com produtores locais para que os excedentes de alimentos possam ser compartilhados, assim como ferramentas de jardim e utensílios de cozinha.
* Foodcloud: conecta supermercados e instituições de caridade para doar itens alimentares não vendidos.
* Too Good to Go: Ativo em nove países europeus, este aplicativo ajuda a combater a questão dos resíduos, fornecendo uma plataforma para as lojas venderem seus excedentes a um preço reduzido.
* Karma: Aplicativo de uma startup sueca que permite que os consumidores descubram alimentos não vendidos de restaurantes, bares e cafés próximos em Londres.

# Visão Geral do Produto <a name="4"></a>
Esta seção fornece uma visualização de alto nível das capacidades do produto, interfaces para outros aplicativos e configurações dos sistemas. Esta seção, em geral, consiste em três subseções:
* Perspectiva do Produto
* Funções do Produto
* Suposições e Dependências

## Perspectivas do produto <a name="4.1"></a>
Nosso produto tem algumas semelhanças com produtos já feitos, como o aplicativo “Copia”, que é uma aplicação cujo objetivo visa diminuir o desperdício de alimentos. FoodCare é independente e totalmente auto contido.


## Resumo das Capacidades <a name="4.2"></a>
Benefício para o Cliente | Recursos de Suporte
------------------------ | -------------------
Aproxima a informação de onde e quando estão havendo doações de alimentos. | ONG’s e pessoas poderão pesquisar eventos que são no caso os de doações de alimento de acordo com a localização desejada.
Aproxima quem quer doar alimentos com quem deseja receber doações dos mesmo. | Através da criação de eventos por parte das instituições que querem doar gera-se a informação de quando e onde haverá doação para quem deseja receber doação.
Cadastro para receber notificações de assim que o evento é criado. | Notificações para os usuários (ONG’s e pessoas).
Cadastro de instituições que querem doar alimentos para que fique mais automático criar eventos com endereços cadastrados. | Após o cadastro a instituição pode ver uma lista dos endereços cadastrados.
Apresenta a localização de eventos de doação de alimentos. | Através do endereço cadastrado pelas as instituições é possível apresentar ao usuário, que deseja doações, a localização do evento .

## Suposições de dependências <a name="4.3"></a>

O FoodCare é um site que é independente de aplicativos externos e por se tratar de um site não requer muito do hardware para se obter um bom desempenho.

## Custo e precificação <a name="4.4"></a>

O único gasto previsto será com a hospedagem do site.

## Licenciamento e Instalação <a name="4.5"></a>

Por se tratar de um site não é necessário instalação do nosso software, para licença de software escolhemos a GPL - 3.0 .

# Recursos do produto <a name="5"></a>

## Cadastro <a name="5.1"></a>

O usuário poderá se cadastrar na plataforma para ter acesso às funcionalidades do software. O cadastro discrimina o tipo de usuário, podendo ele ser: empresa, Ong ou pessoa física.

Essa funcionalidade também atenderá as necessidades de edição do conteúdo informado no momento do cadastro como: endereço, idade, nome fantasia, etc.

## Criar evento <a name="5.2"></a>

Essa funcionalidade permite que uma empresa inicie um evento de doação que estará disponível no sistema, para que Ongs e pessoas físicas visualizem.

## Pesquisar evento <a name="5.3"></a>

Todos os usuários serão capazes de visualizar os eventos com status de ativo no sistema.

## Tipificar alimento <a name="5.4"></a>

A empresa doadora será capaz de adicionar informações sobre o alimento como: data de validade, quantidade, nome, categoria alimentícia, etc.

Esse recurso poderá ser visualizado pelos demais usuários da plataforma.

## Login <a name="5.5"></a>

O usuário de qualquer tipo cadastrado poderá entrar no sistema por meio de login.

## Notificações <a name="5.6"></a>

Usuários cadastrados estarão aptos a receber notificações de acordo com a sua necessidade de uso.

# Outros requisitos do produto <a name="6"></a>

## Requisito de usuário <a name="6.1"></a>

O usuário da aplicação deverá possui um dispositivo com acesso a internet e sistema de localização integrado para poder usufruir das funcionalidades disponíveis da aplicação.

## Requisistos do sistema <a name="6.2"></a>

* Utilizará o plataforma de desenvolvimento web ANGULAR 1.8
* Será usado  a linguagem TYPESCRIPT em conjunto com ANGULAR
* Terá seu padrões de desenvolvimento em conformidade para ser uma PWA
* Aplicação usará protocolo REST para comunicação com a API usando JSON
* O sistema de banco de dados será o SQLite
* A API deverá ser criada no framework DJANGO
* A conteinerização do ambiente de homologação DOCKER
* O padrão de projeto será Model-View-Template
* Para conexões será usado o padrão  Singleton
* Os testes unitários serão feitos usando a ferramenta JEST
* A arquitetura utilizará o padrão de microserviços
* Para sistema de autenticação será usado JWT
