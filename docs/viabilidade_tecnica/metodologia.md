# Introdução

Este documento tem como objetivo deixar transparente o processo Ágil utilizado pelo Time Scrum do projeto FoodCare, descrevendo informações como papéis existentes e ritos do Scrum adotados.

# Papéis na equipe

Esta sessão lista todos os papéis existentes dentro do Time Scrum do projeto FoodCare, suas atribuições e as pessoas que os estão exercendo.

## Product Owner

##### Atribuições:

- Responsável pelo gerenciamento do Backlog do Produto e por garantir o valor do trabalho realizado pelo Time;
- Manter o Backlog do Produto e garante que ele está visível para todos;
- Informar a todos quais itens têm a maior prioridade, de forma que todos sabem em que se irá trabalhar;
- Definir e priorizar os itens do Backlog do Produto;
- Vender o produto;
- Intermediário(ligação) entre o cliente e a equipe;
- Valor de negócio;
- Visão de negócio;
- Negociar com o time e com o cliente;
- Canvas.
- EAP.

## DevOps

##### Atribuições:

- Garantir a integração continua.
- Garantir o deploy continuo.
- Facilitar o processo de desenvolvimento.
- Organizar os diversos pipeline do produto de software.
- Criar docker.

## Scrum Master

##### Atribuições:

- Ajudar todos do Time Scrum a entenderem a teoria, prática, regras e valores do Scrum.
- Servir ao Product Owner, auxiliando de diversas formas, tais como: gerir de maneira eficiente o Backlog do produto.
- Fazer todos do Time Scrum entenderem ao máximo os ítens do Backlog do Produto.
- Servir a equipe, auxiliando de diversas formas, tais como:
remover impedimentos ao progresso de todos da equipe.
instrui-lo em auto-organização e a serem multifuncionais.
- Documentar cada Sprint.
- Determinar e analisar as métricas e indicadores utilizados para acompanhar o progresso de toda a equipe.

## Desenvolvedores

##### Atribuições:

- Entregar os ítens contidos no Backlog da Sprint ao final de cada Sprint.
- Determinar como farão para entregar os ítens do Backlog da Sprint (auto-organização).

# Ritos do Scrum

Abaixo ritos do Scrum que serão realizados pelo Time Scrum do projeto FoodCare. Para cada rito está descrito seus objetivos, o tempo máximo de realização deles, os dias e horários em que ocorrerão.

## Sprint

#### objetivo:

- atingir o objetivo para a Sprint definido no Planejamento da Sprint, assim como entregar todos os ítens do Backlog da Sprint
- time box: segunda à domingo [1 semana]

## Planejamento de Sprint

- Reunião realizada com o Time Scrum no início de cada Sprint que tem como objetivo:

- Determinar o que poderá ser entregue na Sprint que se inicia (criação do Backlog da Sprint).
- Isso deve ser negociado entre o Product Owner e restante da equipe, respeitando a capacidade projetada e a performance passada deste estimar o esforço necessário para entregar as histórias do backlog, através da pontuação delas usando o planning poker.
- Antes do início da pontuação de cada história, o Product Owner deve explicá-la e tirar as dúvidas da equipe, para que todos possam ter uma melhor base para a pontuação.
- Cada participante vota, dando os pontos que acham que aquela história vale, tendo como base quantas horas eles imaginam que serão necessárias para completá-la. O voto de todas as pessoas só é revelado quando todos tiverem decidido quantos pontos darão para a história.
- A pontuação dada para cada história deve estar dentro da sequência de Fibonacci, sendo a menor pontuação válida 1
este passo é repetido até que haja consenso de todos os presentes sobre quantos pontos a história em questão vale.
- A equipe passa a pontuar a próxima história, até que todas estejam pontuadas.
- Determinar como a equipe irá se organizar para que haja a entrega prevista para a Sprint

- time box: : 23:00 [2h]

## Daily Meeting

- Reunião diária do Time Scrum que tem como objetivo:
- Cada membro responder as 3 perguntas abaixo, sobre sua participação no andamento da Sprint:
- O que foi feito pelo membro no dia anterior para ajudar a desenvolver na Sprint?
- O que será feito pelo membro no dia atual para ajudar no desenvolvimento na Sprint?
- Houve algum empedimento para o membro que impossibilitou ele ajudar o restante da equipe na Sprint? (gerenciamento de riscos)
- time box:
- Dailys presenciais: terça e quinta, 15:50 [15 min].
- Dailys online: segunda, quarta, sexta, sábado, domingo começando às 22:00.

## Review de Sprint

objetivo:
- Revisar como foi a Sprint, com foco no Backlog do Produto e no da Sprint.
- O que foi feito e o que ficou como débito (Product Owner).
- Atualização do Backlog do Produto (Product Owner)
Problemas relacionados ao Backlog da Sprint e se/como foram resolvidos (toda a equipe)
time box: domingo, início da reunião 22h[1h]

IMPORTANTE: um item do Backlog da Sprint só será aceito como feito se:
- Estiver terminado.
- Estiver coberto, no mínimo, por teste unitário e/ou de integração, exceto em caso de documentação ou outros tipos de histórias que não puderem ser testadas.
- Tiver sido feito o pull request para a branch develop ou master e este ser aceito pelos revisores.
- A funcionalidade entregue ser aceita pelo Product Owner, de acordo com os critérios de aceitação especificados na história.

## Retrospectiva da Sprint

objetivo:
- Levantar como foi a Sprint, do ponto de vista das pessoas, relacionamentos, processos e ferramentas (pontos positivos e negativos).
- Identificar potenciais melhorias.
- Identificar melhorias para colocar em prática na próxima Sprint

time box: domingo, 24h [1:30h]
