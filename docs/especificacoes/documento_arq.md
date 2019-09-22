# Documento de Arquitetura
## Historico de versão
 Data | Versão | Descrição | Autor
 ---- | ------ | --------- | -----
19/09/19 | 1.0 | Abertura do documento, criação da introdução| Lucas , Geraldo
20/09/19 | 1.1 | Adiciona Requisitos mínimos dos sistemas | Giovanna
21/09/19 | 1.2 | Adiciona visão de dados | Giovanna
21/09/19 | 1.3 | Adiciona introdução e representação de arquitetura| Geraldo
<<<<<<< HEAD
21/09/19 | 1.4 | Adiciona diagrama de sequência doador| Lucas
=======
22/09/19 | 1.4 | Atualiza introdução e representação de arquitetura| Geraldo
>>>>>>> 1a57fc0f1e688b507022687ef3a6849d8533c8b0

# Índice
1. [Introdução](#1)
    1. [Finalidade](#1.1)
    2. [Escopo](#1.2)
    3. [Definições, acrônimos, abreviações](#1.3)
2. [Representação da arquitetura](#2)
    1.  [Back-end](#2.1)
        1. [MVC](#2.1.1)
        2. [MTV](#2.1.1)
    2.  [Front-end](#2.2)   
3. [Metas e Restrições de Arquitetura](#3)
4. [Visão de casos de uso](#4)
5. [Visão lógica](#5)
    1. [Diagramas significativos](#5.1)
        1. [Diagrama de classes](#5.1.1)
        2. [Diagrama de colaboração](#5.1.2)
        3. [Diagrama de pacotes](#5.1.3)
6. [Visão de implantação](#6)
    1. [Diagrama de implantação](#6.1)
7. [Diagrama de sequência](#7)
    1. [Diagrama de sequência doador](#7.1)    
    2. [Diagrama de sequência de usuário](#7.2)
8. [Diagrama de usuário](#8)
    1. [Diagrama de atividades (atividade)](#8.1)
    2. [Diagrama de atividades (artigo)](#8.2)
9. [Visão de implementação](#9)
    1. [Finalidade](#9.1)
    2. [Diagramas significativos](#9.2)
        1. [Diagrama de componentes](#9.2.1)
10. [Visão de dados](#10)
    1. [Diagrama entidade-relacionamento](#10.1)
    2. [Diagrama lógico](#10.2)
        1. [Diagrama lógico modelado](#10.2.1)
        2. [Diagrama Lógico Gerado pelo Django](#10.2.2)
11. [Qualidade](#11)
    1. [Requisitos funcionais](#11.1)
    2. [Requisitos não funcionais](#11.2)
    3. [Requisitos para plataformas específicas](#11.3)
    4. [Usabilidade](#11.4)
    5. [Confiabilidade](#11.5)
    6. [Desempenho](#11.6)
    7. [Suportabilidade](#11.7)
    8. [Restrições de design](#11.8)
    9. [Requisitos de Sistema de Ajuda e de Documentação de Usuário On-line](#11.9)
    10. [Interfaces de Hardware](#11.10)
12. [Requisitos Mínimos dos Sistemas](#12)
    1. [Sistema executar o projeto](#12.1)
    2. [Servidor de Banco de Dados e Servidor Web](#12.2)
        1. [Servidor de Banco de Dados](#12.2.1)
            1. [SQLite](#12.2.1.1)
        2. [Servidor Web](#12.2.2)
13. [Referências](#13)


# Introdução <a name="1"></a>

## Finalidade <a name="1.1"></a>
Este documento tem como finalidade apresentar a arquitetura do projeto **FoodCare**, para registrar decisões relacionadas ao projeto através de diversas visões. O documento é dividido da seguinte forma: primeiramente a representação da arquitetura da solução é apresentada, em seguida metas e restrições desta arquitetura e por fim as visões sobre elementos da arquitetura.
## Escopo <a name="1.2"></a>
Este documento apresenta as características arquiteturais do projeto **FoodCare**, descrevendo em detalhes a soluções arquiteturais determinadas para o projeto, de forma a servir como base para o desenvolvimento do projeto pelos desenvolvedores de software alocados para o projeto.
## Definições, acrônimos, abreviações <a name="1.3"></a>
**MVC** - Model View Controller

**MTV** - Model Template View

**Django** - Framework da linguagem python para a construção rápida de aplicativos web, fornecendo componentes prontos e com fácil uso.

**HTTP** - Prototocolo de comunicação utilizado para sistemas de informação.

**REST** - Ferramenta que auxilia a utilização do protocolo http.

**Angular** - Framework de front-end que visa aumentar a produtividade no que diz respeito ao ao front-end do projeto.

**Docker** - Ferramenta utilizada para modularizar os processos do desenvolvimento do software para eliminiar as inconsistências do ambiente de desenvolvimento.

**PWA** - Progressive Web App (PWA) é um termo usado para denotar aplicativos da web que usam as últimas tecnologias da web. Os aplicativos da web progressivos são páginas web (ou sites) tecnicamente regulares, mas podem aparecer ao usuário como aplicativos tradicionais ou aplicativos móveis (nativos).

**FoodCare** - Aplicação web, desenvolvida em Django REST e Angular, que tem como objetivo aproximar pessoas que querem doar com pessoas que desejam receber, estimulando doações, tendo em vista a quantidade de comida que é desperdiçada todos os dias.

# Representação da arquitetura <a name="2"></a>

## Back-end <a name="2.1"></a>

O sistema faz uso do Framework Django (versão 2.2.2), que faz uso do padrão MVC. No entanto, tal plataforma possui uma interpretação singular em relação à organização de camadas. O indicado é considerar que a própria plataforma faz o papel da camada de controle, enquanto a camada de Modelo e de Visão devem ser adaptadas e reinterpretadas conforme o necessário. Por este motivo, ainda que o Django implemente o MVC, considera-se que o padrão de camadas externalizado pela plataforma é o MTV (Model-Template-View). Para auxiliar no protocolo http utilizamos a ferramenta REST.
A utilização de uma arquitetura em camadas é interessante por proporcionar uma clara separação de responsabilidades no código, proporcionando reusabilidade, e reduzindo o esforço de manutenção. Os conceitos de MVC e MTV serão apresentados nas seções seguintes.

### MVC <a name="2.1.1"></a>
Figura 1. Padrão arquitetural MVC.

* **Model:** camada de acesso a base de dados, é responsável pela leitura, manipulação e validação dados;

* **Controller:** é responsável por manipular e validar as requisições do usuário, traduzindo em comandos enviados para enviados para a Model e/ou View .

* **View:** camada de interface com o usuário, responsável pela representação dos dados;
### MTV <a name="2.1.1"></a>
Figura 2. Padrão arquitetural MTV.

* **Model:** segue a mesma definição da model no MVC;

* **Template:** segue a mesma definição da view no MVC;

* **View:** segue a mesma definição da controller no MVC.

## Back-end <a name="2.2"></a>
O sistema faz uso do angular 8, que traz vantagens como: componetização, módulos específicos para configurar PWA, sistema de rotas de páginas, framework material para parte de design do site.
# Metas e Restrições de Arquitetura <a name="3"></a>

# Visão de casos de uso <a name="4"></a>

# Visão lógica  <a name="5"></a>

## Diagramas significativos <a name="5.1"></a>

### Diagrama de classes <a name="5.1.1"></a>

### Diagrama de colaboração <a name="5.1.2"></a>

### Diagrama de pacotes <a name="5.1.3"></a>

# Visão de implantação  <a name="6"></a>
## Diagrama de implantação <a name="6.1"></a>


# diagrama de sequência <a name="7"></a>
## diagrama de sequência doador <a name="7.1"></a>
![Diagrama de Sequência doador](seq_diag_doador.png)

## diagrama de sequência (usuário) <a name="7.2"></a>

# diagrama de usuário <a name="8"></a>
## diagrama de atividades (geral) <a name="8.1"></a>
## diagrama de atividades (usuário) <a name="8.2"></a>

# visão de implementação <a name="9"></a>
## finalidade <a name="9.1"></a>
## diagramas significativos <a name="9.1"></a>
### diagrama de componentes <a name="9.1.1"></a>

# visão de dados <a name="10"></a>
## diagrama entidade-relacionamento <a name="10.1"></a>
![diagrama entidade-relacionamento](https://github.com/fga-eps-mds/2019.2-FoodCare/blob/docs/docs/images/DER.png?raw=true)
## diagrama lógico <a name="10.2"></a>
### diagrama lógico modelado <a name="10.1.1"></a>
![diagrama lógico modelado](https://github.com/fga-eps-mds/2019.2-FoodCare/blob/docs/docs/images/MER.png?raw=true)

# Qualidade  <a name="11"></a>
## requisitos funcionais <a name="11.1"></a>
## requisitos não funcionais <a name="11.2"></a>
## requisitos para plataformas específicas <a name="11.3"></a>
## usabilidade <a name="11.4"></a>
## confiabilidade <a name="11.5"></a>
## desempenho <a name="11.6"></a>
## suportabilidade <a name="11.7"></a>
## restrições de design <a name="11.8"></a>
## Requisitos de Sistema de Ajuda e de Documentação de Usuário On-line <a name="11.9"></a>
## Interfaces de Hardware <a name="11.10"></a>

# Requisitos Mínimos dos Sistemas <a name="12"></a>
## Sistema executar o projeto <a name="12.1"></a>

* Processadores: processador Intel Atom® ou processador Intel® Core ™ i3
* Espaço em disco: 1 GB
* Sistemas operacionais: Windows * 7 ou posterior, macOS e Linux
* Versões Python *: 2.7.X, 3.6.X

## Servidor de Banco de Dados e Servidor Web <a name="12.2"></a>

Com os requisitos a seguir o esse servidor deve suportar cerca de 10 000 usuários, caso tenha necessidade de atuar com mais usuários o estudo deve ser feito novamente.

### Servidor de Banco de Dados <a name="12.2.1"></a>
* Requirido
    * Processador = Xeon E5 server family
    * CPU = 2 x 4 cores
    * Memoria RAM = 16 GB
    * Backup = External Hard Disk, HDD
* Futura expansabilidade
    * CPU = 1 x 4 sockets
    * Espaço de Disco = 16GB à 1.5TB

#### SQLite <a name="12.2.1.1"></a>

Windows | Linux/ Mac
------- | -----
XP Service Pack 3/2003 Service Pack 2 ou maior. |  Java Runtime Environment (JRE) 1.5 ou maior.  
.NET Framework 2.0 ou maior. | 500 MB RAM  
500 MB RAM |
### Servidor Web <a name="12.2.1"></a>

A escolha do servidor web é de grande importancia pois afeta diretamente a experiencia do usuário. Deve ser um equilíbrio de CPU e de RAM.

* Processador: Intel I7-3770
* Memoria Ram: 16GB
* HDD: 146 GB 15K 12GBPS 128MB Cache

# Referências <a name="13"></a>

* Requisitos de hardware. Disponível em <http://www.stansoftware.com/hardware-requirements/>. Acesso em 20 de setembro de 2019.
* Requisitos de sistema. Disponível em: <https://software.intel.com/en-us/distribution-for-python/system-requirements>. Acesso em 20 de setembro de 2019.
* Requisitos de sistema. Disponível em: <http://cdn.cdata.com/help/DEA/rsb/pg_startrequirementsrsb.htm>. Acesso em 20 de setembro de 2019.
* Get Started with Docker. Disponível em <https://www.docker.com/get-started>
* Software Architecture: MVC Design Pattern, Medium. Disponível em: //medium.com/@dennisvera.z/software-architecture-mvc-design-pattern-ceae5d5083d7)).
* Django's Structure – A Heretic's Eye View, The django book. Disponível em: <https://djangobook.com/mdj2-django-structure/>
* O que é PWA (Progressive Web App). Disponível em <https://vizir.com.br/2017/08/o-que-e-pwa-progressive-web-app-porque-isso-pode-aumentar-seus-resultados-mobile/>