# Termo de Abertura do Projeto

## Histórico de Versão

|Versão|Data|Descrição|Nome|
|---|---|---|---|
|1.0|10/09/2019|Abertura do documento|Igor Aragão|

## Introdução

Este documento visa apresentar uma visão inicial do projeto FoodCare. Também tem como objetivo informar os propósitos, objetivos e requisitos de alto nível do projeto.

## Descrição

FoodCare é um sistema desenvolvido para buscar, através da doação de sobra de alimentos, uma solução que ajude no cumprimento da meta 2.1 dos Objetivos de Desenvolvimento Sustentável, que busca "até 2030, acabar com a fome e garantir o acesso de todas as pessoas, em particular os pobres e pessoas em situações vulneráveis, incluindo crianças, a alimentos seguros, nutritivos e suficientes durante todo o ano".  

## Propósito

Os dados do último levantamento da Organização das Nações Unidas para Alimentação e Agricultura (FAO), em 2018, permitem estimar que mais de 5 milhões de brasileiros ainda sofrem com a escassez de alimentos.  

Esse mesmo levantamento, nos diz que dos 268,1 milhões de toneladas de alimentos disponíveis no País em 2013, 26,3 milhões, ou quase 10%, foram perdidos.  

Diante desse quadro, nosso propósito, é evitar que as pessoas, ou empresas, joguem fora alimentos que ainda são próprios para consumo, conectando-as com quem precisa desses alimentos, ajudando a combater a fome no Brasil.  

## Objetivo

O objetivo do FoodCare é facilitar a doação de alimentos, conectando quem não precisa mais deles, com quem realmente precisa.  

## Requisitos de Alto Nível

O sistema tem como foco, as seguintes funcionalidades:

- Cadastro de doador
- Cadastro de receptor
- Criação de um novo evento (doação de alimento), por parte do doador
- Edição de um evento criado pelo próprio doador
- Finalização de um evento criado pelo próprio doador
- Visualização de eventos criados pelo próprio doador
- Visualização dos eventos na proximidade, por parte do receptor

## Restrições

Para utilizar o sistema, os usuários vão precisar de:

- Conexão com a internet
- Possuir um dispositivo com navegador web

## Riscos Iniciais

Os principais riscos do desenvolvimento do FoodCare são:

|Risco|Ação Preventiva|Ação Reativa|
|---|---|---|
|Dificuldade da equipe em se adaptar com as tecnologias inseridas|Utilização de tecnologias onde a equipe de gerência já tenha tido experiências posteriores|Realização de treinamento e resolução de dúvidas sobre tecnologias|
|Desistência de membros da equipe|Mostrar aos membros a real experiência da matéria, e motivá-los a participar|Separar tarefas de forma que não sobrecarregue os demais membros do grupo|
|Divergência de horários entre membros da equipe|Criar planilha com horários de cada membro|Planejar pareamento dos que têm horários disponíveis mais parecidos|
Alteração do escopo|Elicitar corretamente os requisitos, manter documentos atualizados|Atualizar documentos, e melhorar planejamento|
Falta de comunicação|Equipe de gerência buscar envolver todos do projeto|Reunir membros

## Cronograma

O projeto tem como base dois marcos principais, Release 1 e Release 2, que representam entregas do produto.  

Baseado nesses marcos, definimos as datas mais importantes do projeto:

|Marco|Data|Atividade|
|---|---|---|
|Início do Projeto|12/08/2019|Montar equipe, buscar tema do projeto|
|Release 01|30/09/2019 a 04/10/2019|Apresentação dos documentos elaborados, comunicação da equipe e software desenvolvido|
|Release 02|02/12/2019 a 06/12/2019|Apresentação do software desenvolvido e evidências da execução da metodologia|

## Custo Estimado

Por meio deste, disponibilizamos os cálculos referentes ao custo dos insumos necessários para o desenvolvimento do projeto.

### Custo de Aquisição

|Item|Finalidade|Valor (R$)|Quantidade|Total (R$)|Fornecedor|
|---|---|---|---|---|---|
|Notebook|Desenvolvimento e planejamento|Média: R$ 2.199,00|9|R$ 19.791,00|Variados|
|Energia|Desenvolvimento e planejamento|0,557 R$/KWh*|814,32 kw/h*|R$ 453,57|CEB|
|Internet|Desenvolvimento e planejamento|R$ 99,99*|9 pessoas durante 4 meses*|R$ 3.599,64*|Variados|

O Custo de Aquisição totaliza: R$ 23.844,21.

#### Observações

- De acordo com a Agência Nacional de Energia Elétrica (ANEEL), na data de 10/09/2019, o custo do KW/h, no DF, é de R$ 0,557.
- **Energia:** Adotamos que: Um computador opera a 130 watts e o computador permanece ligado 6 horas por dia ao longo de 116 dias (12/09/2019 à 06/12/2019). Sendo assim, calculamos:  
```CONSUMO = (130 watts x 6 horas x 116 dias)/1.000 * 9 PCs = 814,32 kw/h```
- **Internet:** Adotamos que o valor médio, por mês, de um plano de internet no DF é de R$ 99,99 e que serão 4 meses de desenvolvimento. Sendo assim, calculamos:  
```CONSUMO = (99,99 reais x 4 meses x 9 pessoas) = R$ 3599,64```

### Custo de Pessoal

|Cargo|Quantidade|Salário/mês* (R$)|Salário/hora (R$)|Total (R$)*|
|---|---|---|---|---|
|Desenvolvedor Python Jr|6|R$ 3.250,00|R$ 20,32|R$ 20.726,40|
|DevOps, Scrum Master e PO|3|R$ 6.000,00|R$ 37,50|R$ 19.125,00|

O Custo de Pessoal totaliza: R$ 39851,40.

#### Observações

- Foi considerado que o mês tem 160 horas.
- Adotamos também que o projeto terá a duração de 17 semanas, e que em cada semana, cada membro trabalhara por 10 horas/semana.
- O salário total por pessoa é conseguido através do cálculo:  
```SALARIO TOTAL (INDIVIDUAL) = SalarioHora x 10 horas x 17 semanas```

### Custo de Ferramentas

|Ferramenta|Finalidade|Preço total|
|---|---|---|
|Telegram|Comunicação entre os membros|R$ 0|
|Editor de Texto|Elaboração de documentos e código|R$ 0|
|Git e GitHub|Versionamento de arquivos|R$ 0|
|Google Drive|Compartilhamento de arquivos|R$ 0|
|ZenHub|Gestão de tarefas|R$ 0|
|Linux|Ambiente de desenvolvimento|R$ 0|
|Python, Rasa, Flask, MongoDB|Tecnologias utilizadas para desenvolvimento|R$ 0|

### Custo Total

|Tipo de Recurso|Custo|
|---|---|
|Custo de Aquisição|R$ 23.844,21|
|Custo de Pessoal|R$ 39.851,40|
|Custo de Ferramentas|R$ 0,00|
|**Custo Total**|**R$ 63.695,61**|

## Partes Interessadas

### Usuários

Os usuários se dividem em duas categorias: Doadores e Receptores.

#### Doadores

Qualquer restaurante, hortifruti, sacolão, supermercado, panificadora, ou qualquer empresa que tem alimentos que já perderam valor comercial, mas ainda estão próprios para consumo.

#### Receptores

Qualquer ONG que distribua alimentos, ou qualquer pessoa física que possa buscar o alimento.

### Equipe

|Nome|Papel|Email|
|---|---|---|
|Bruna Almeida     |Desenvolvedor|brunaalmeida48@gmail.com    |
|Geraldo Victor    |Desenvolvedor|geraldovictor@outlook.com   |
|Giovanna Bottino  |Desenvolvedor|gibottino@gmail.com         |
|Hugo Aragão       |Desenvolvedor|hugoaraliveira@gmail.com    |
|Lucas Lopes       |Desenvolvedor|l.lopes.fga@gmail.com       |
|Rafaella Junqueira|Desenvolvedor|rafaellafjunqueira@gmail.com|
|Geovanne Saraiva  |Gerência|geovannessaraiva97@gmail.com|
|Igor Aragão       |Gerência|roginaldosemog@gmail.com|
|William Almeida   |Gerência|will.allmeida@gmail.com|

## Referências

Ranking das Tarifas. ANEEL. Disponível em: <http://www.aneel.gov.br/ranking-das-tarifas>. Acesso em 10/09/2019.

The State of Food Security and Nutrition in the World 2018. FAO. Disponível em: <http://www.fao.org/3/i9553en/i9553en.pdf>. Acesso em 10/09/2019.

Objetivo de Desenvolvimento Sustentável. ONU. Disponível em: <https://nacoesunidas.org/pos2015/ods2/>. Acesso em 10/09/2019.

Estes dados mostram que a fome ainda é um problema no Brasil. Super Interessante. Disponível em: <https://super.abril.com.br/sociedade/por-que-ainda-nao-da-para-afirmar-que-nao-existe-fome-no-brasil/>. Acesso em 10/09/2019.

Termo de Abertura de Projeto. Dr. Down. Disponível em: <https://fga-eps-mds.github.io/2018.1-Dr-Down/eps/TAP/>. Acesso em 10/09/2019.
