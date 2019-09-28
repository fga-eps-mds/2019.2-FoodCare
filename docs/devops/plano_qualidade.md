# Plano de gerenciamento de qualidade

## Histórico de Versão
|Versão|Data|Descrição|Nome|
|---|---|---|---|
|1.0|27/09/2019|Abertura do documento|William Almeida|

## Introdução

Esse documento tem como finalidade apresentar as ferramentas, métricas e o planejamento de qualidade de produto. De acordo com a ISO 9000, a qualidade está relacionada com o grau no qual um conjunto de características inerentes satisfaz aos requisitos.

## Planejamento

Buscando que o código tenha uma boa qualidade, serão usadas algumas métricas iniciais que estão relacionadas com a qualidade, como conformidade com os guias de estilos das linguagens, cobertura de testes unitários, nível de manutenibilidade, entre outras características.

## Métricas
|Métrica|Bom|Regular|Ruim|
|---|---|---|---|
|Cobertura de testes unitários|Acima de 90%|De 75% a 90%|Abaixo de 75%|
|Manutenibilidade|A e B|C|D ou F|
|Quebras no padrão de código|0 a 5|6 a 10|Acima de 11|
|Duplicação de código|Abaixo de 2%|De 2% a 4%|Acima de 4%|
|Tamanho de métodos|Abaixo de 25 linhas|De 25 a 40 linhas|Acima de 40 linhas|

## Monitoramento

O monitoramento da qualidade do código será feito ao final de cada sprint com auxílio das ferramentas CodeClimate e Coveralls. Após a análise dos resultados, se necessários serão montados planos de melhorias para que as possíveis falhas sejam corrigidas.

## Ferramentas


* [Code Climate](https://codeclimate.com/): O Code Climate permite o monitoramento de algumas métricas importantes do software, como a duplicação, complexidade, quantidade de linhas, e nível de manutenibilidade. Será usado tanto no frontend quanto no backend.


* [Unittest](https://docs.python.org/3/library/unittest.html): O unittest é uma ferramenta padrão de testes unitários do python que foi inspirado no JUnit. Ele será usado no backend e permite a automatização dos testes.

* [Karma](https://karma-runner.github.io/latest/index.html): O Karma(com auxílio do Jasmine) é uma ferramenta que possibilita a execução de testes unitários no Angular. Será a ferramenta padrão de testes do frontend.

* [Coveralls](https://coveralls.io/): O coveralls é uma ferramenta que possibilita o monitoramento dos testes unitários, e permite a visualização dos trechos de códigos que estão cobertos por testes e a porcentagem de código coberto. Será usado tanto no backend quanto no frontend.

* [Travis CI](https://travis-ci.org/): O Travis CI é uma ferramenta que permite a criação de builds dos testes unitários e coleta de resultados dos mesmos. Será usado tanto no frontend quanto no backend.
