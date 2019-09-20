# Documento de Arquitetura
## Historico de versão
 Data | Versão | Descrição | Autor
 ---- | ------ | --------- | -----
19/09/19 | 1.0 | Abertura do documento, criação da introdução| Lucas
20/09/19 | 1.1 | Adiciona Requisitos mínimos dos sistemas | Giovanna

# Índice
1. [Introdução](#1)
    1. [Finalidade](#1.1)
    2. [Escopo](#1.2)
    3. [Definições, acrônimos, abreviações](#1.3)
2. [Representação da arquitetura](#2)
    1. [MVC](#2.1)
    2. [MTV](#2.2)
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
    1. [Diagrama de sequência geral](#7.1)    
    2. [Diagrama de sequência de usuário](#7.2)
8. [Diagrama de usuário](#8)
    1. [Diagrama de atividades (atividade)](#8.1)
    2. [Diagrama de atividades (artigo)](#8.2)
9. [Diagrama de estados](#9)
    1. [Diagrama de estados (atividade)](#9.1)
    2. [Diagrama de estados (artigo)](#9.2)
10. [Visão de implementação](#10)
    1. [Finalidade](#10.1)
    2. [Diagramas significativos](#10.2)
        1. [Diagrama de componentes](#10.2.1)
11. [Visão de dados](#11)
    1. [Diagrama entidade-relacionamento](#11.1)
    2. [Diagrama lógico](#11.2)
        1. [Diagrama lógico modelado](#11.2.1)
        2. [Diagrama Lógico Gerado pelo Django](#11.2.2)
12. [Qualidade](#12)
    1. [Requisitos funcionais](#12.1)
    2. [Requisitos não funcionais](#12.2)
    3. [Requisitos para plataformas específicas](#12.3)
    4. [Usabilidade](#12.4)
    5. [Confiabilidade](#12.5)
    6. [Desempenho](#12.6)
    7. [Suportabilidade](#12.7)
    8. [Restrições de design](#12.8)
    9. [Requisitos de Sistema de Ajuda e de Documentação de Usuário On-line](#12.9)
    10. [Interfaces de Hardware](#12.10)
13. [Requisitos Mínimos dos Sistemas](#13)
    1. [Sistema executar o projeto](#13.1)
    2. [Servidor de Banco de Dados e Servidor Web](#13.2)
        1. [Servidor de Banco de Dados](#13.2.1)
            1. [SQLite](#13.2.1.1)
        2. [Servidor Web](#13.2.2)
14. [Referências](#14)


# Introdução <a name="1"></a>

## Finalidade <a name="1.1"></a>

## Escopo <a name="1.2"></a>

## Definições, acrônimos, abreviações <a name="1.3"></a>

# Representação da arquitetura <a name="2"></a>

## MVC <a name="2.1"></a>

## MTV <a name="2.2"></a>

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
## diagrama de sequência (geral) <a name="7.1"></a>
## diagrama de sequência (usuário) <a name="7.2"></a>

# diagrama de usuário <a name="8"></a>
## diagrama de atividades (geral) <a name="8.1"></a>
## diagrama de atividades (usuário) <a name="8.2"></a>

# diagrama de estados <a name="9"></a>
## diagrama de estados (geral) <a name="9.1"></a>
## diagrama de estados (usuário) <a name="9.2"></a>

# visão de implementação <a name="10"></a>
## finalidade <a name="10.1"></a>
## diagramas significativos <a name="10.1"></a>
### diagrama de componentes <a name="10.1.1"></a>

# visão de dados <a name="11"></a>
## diagrama entidade-relacionamento <a name="11.1"></a>
## diagrama lógico <a name="11.2"></a>
### diagrama lógico modelado <a name="11.1.1"></a>
### Diagrama Lógico Gerado pelo Django <a name="11.1.2"></a>

# Qualidade  <a name="12"></a>
## requisitos funcionais <a name="12.1"></a>
## requisitos não funcionais <a name="12.2"></a>
## requisitos para plataformas específicas <a name="12.3"></a>
## usabilidade <a name="12.4"></a>
## confiabilidade <a name="12.5"></a>
## desempenho <a name="12.6"></a>
## suportabilidade <a name="12.7"></a>
## restrições de design <a name="12.8"></a>
## Requisitos de Sistema de Ajuda e de Documentação de Usuário On-line <a name="12.9"></a>
## Interfaces de Hardware <a name="12.10"></a>

# Requisitos Mínimos dos Sistemas <a name="13"></a>
## Sistema executar o projeto <a name="13.1"></a>

* Processadores: processador Intel Atom® ou processador Intel® Core ™ i3
* Espaço em disco: 1 GB
* Sistemas operacionais: Windows * 7 ou posterior, macOS e Linux
* Versões Python *: 2.7.X, 3.6.X

## Servidor de Banco de Dados e Servidor Web <a name="13.2"></a>

Com os requisitos a seguir o esse servidor deve suportar cerca de 10 000 usuários, caso tenha necessidade de atuar com mais usuários o estudo deve ser feito novamente.

### Servidor de Banco de Dados <a name="13.2.1"></a>
* Requirido
    * Processador = Xeon E5 server family
    * CPU = 2 x 4 cores
    * Memoria RAM = 16 GB
    * Backup = External Hard Disk, HDD
* Futura expansabilidade
    * CPU = 1 x 4 sockets
    * Espaço de Disco = 16GB à 1.5TB

#### SQLite <a name="13.2.1.1"></a>

Windows | Linux/ Mac
------- | -----
* XP Service Pack 3/2003 Service Pack 2 ou maior. | * Java Runtime Environment (JRE) 1.5 ou maior.  
* .NET Framework 2.0 ou maior. | * 500 MB RAM  
* 500 MB RAM |
### Servidor Web <a name="13.2.1"></a>

A escolha do servidor web é de grande importancia pois afeta diretamente a experiencia do usuário. Deve ser um equilíbrio de CPU e de RAM.

* Processador: Intel I7-3770
* Memoria Ram: 16GB
* HDD: 146 GB 15K 12GBPS 128MB Cache

# Referências <a name="14"></a>

* Requisitos de hardware. Disponível em <http://www.stansoftware.com/hardware-requirements/>. Acesso em 20 de setembro de 2019.
* Requisitos de sistema. Disponível em: <https://software.intel.com/en-us/distribution-for-python/system-requirements>. Acesso em 20 de setembro de 2019.
* Requisitos de sistema. Disponível em: <http://cdn.cdata.com/help/DEA/rsb/pg_startrequirementsrsb.htm>. Acesso em 20 de setembro de 2019.
