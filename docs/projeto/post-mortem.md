# Post Mortem

## Historico de versão

 Data | Versão | Descrição | Autor
 ---- | ------ | --------- | -----
20/10/19 | 1.0 | Abertura do documento | Hugo
27/10/19 | 2.0 | Atualiza para Release 2, Introdução, Definição de escopo e Metodologia | Hugo
28/10/19 | 2.1 | Correções e complementação de metodologia | Lucas
28/10/19 | 2.2 | Adiciona Tecnologia | Giovanna
28/10/19 | 2.3 | Capacitação da equipe | Lucas
28/10/19 | 2.4 | Adiciona Arquitetura | Bruna

## Introdução

O documento visa expor a experiência do grupo com o projeto
e os pontos de maior relevância em seu desenvolvimento.

## Definição de Escopo

O escopo foi inicialmente definido a partir do problema que decidimos abordar, no caso 'Acabar com a fome'.
A partir desse processo o grupo realizou um exercício de brainstorming para encontar os pontos principais de 
abordagem para solucionar o problema. O escopo partiu então de criação de uma solução em tecnologia que 
conectasse um doador de alimentos com uma pessoa que tivesse interesse de receber a doação.

Com a decisão de criar uma Webapp para a facilidade de acesso de pessoas com com recurso financeiro limitado, sendo exportado também na forma de PWA, onde pode ser acessado via smartphones de diversos modelos. Após a definição do modelo, reunimos as ideias e reduzimos o escopo até onde parecia ser aceitável e possível de entregar dentro das requisições da disciplina.

## Metodologia

A metodologia adotada seguiu o modelo Scrum e foi sendo incrementada ao longo do decorrer da disciplina, como a adoção e aplicação de prática abordadas de Clean Code do livro de Robert Cencil Martin,"Uncle Bob", e  de processos da metodologia de desenvolvimento unificado R.U.P.,Rational Unified Process.

Mais informações em: [Metodologia](https://github.com/fga-eps-mds/2019.2-FoodCare/blob/docs/docs/projeto/metodologia.md)

## Capacitação 

Foram realizados treinamentos de teste usando a ferramenta de test runner Karma e Jasmine para teste unitários para o Front-end e  capacitação e treino em um dojo para utilização do Django em conjunto com Django-RestFramework, DRF, para extensão de suas classes e execução dos teste usando o Client da ferramenta para simulação do ambiente em produção para o Back-end da aplicação.

## Tecnologia

A defeninição das tecnologias foi feita através de discussões entre os membros do grupo. Para o gerenciamento e configuração usamos [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/). Para a criação da interface do webapp optamos pelo [Angular](https://angular.io/), pela curva de aprendizado. Já na escolha da tecnologia para o desenvolvimento de nossa API escolhemos [Django](https://www.djangoproject.com/) também pelo facilidade de aprendizado e conhecimento do grupo. Usamos o [Travis](https://travis-ci.org/) para a integração continua. Para a comunicação e gerenciamento foi usado o [ZenHub](https://www.zenhub.com/) e o [Telegram](https://web.telegram.org/#/im). E por fim para versonamento de codigo foi usado o [Git](https://git-scm.com/) e o [GitHub](https://github.com/).

Mais informações em: [Ferramentas](https://github.com/fga-eps-mds/2019.2-FoodCare/blob/docs/docs/projeto/ferramentas.md)

## Arquitetura

Como sugerido durante a release 1, diminuímos o escopo do projeto para termos a certeza de que todas as funcionalidades seriam entregues corretamente.
Com a diminuição do escopo, conseguimos trabalhar melhor em cada funcionalidade, pois o trabalho foi melhor distribuído entre as sprints.

Mais informações em: [Arquitetura](https://github.com/fga-eps-mds/2019.2-FoodCare/blob/master/docs/produto/doc-arquitetura.md)

## Conclusão

No início do projeto foram divididos os papéis e as responsabilidades entre a equipe de EPS, já a equipe de MDS ficou responsável por desenvolver o código. A experiência vivida na matéria de MDS trouxe para todos os membros do grupo um grande amadurecimento em relação a tecnologias e metodologias de desenvolvimento de software. Terminamos a matéria com um sentimento de cansaço e satisfação. Apesar dos erros aprendemos muito. 


## Citações
```
Hoje eles riem do seu esforço amanhã do seu fracasso. Victor Geraldo.
```
 
```
Se não tem código ele não precisa ser testado. Aragão Hugo.
```

```
Uma boa ação nunca fica sem punição. Aragão Hugo.
```

```
Desistir é para os fracos, faça que nem eu, nem tente. Almeida Bruna.
```

```
Desisto. Bottino Giovanna. 
```

```
Na hora certa vai dar tudo errado. Bottino Giovanna. 
```

```
Não estamos mais atrasados, obrigado. Aragão Hugo.
```
