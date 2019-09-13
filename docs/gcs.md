# Plano de Gerenciamento de Configuração de Software

## Histórico de Versão

|Versão|Data|Descrição|Nome|
|---|---|---|---|
|1.0|01/09/2019|Abertura do documento|Igor Aragão|
|1.1|12/09/2019|Refatora o documento|Igor Aragão|

## Introdução

Esse documento tem como finalidade definir a política de utilização de branches no repositório.

## Políticas

### Política de Commits

Cada commit deve ser criado após a finalização de um bloco conexo de alterações, seja em código, e/ou em documentação.  
O título do commit, deve ser coerente às alterações feitas de forma resumida e em português, com o tempo verbal no particípio, e ser iniciado com a letra maiúscula. Por exemplo:

   ```Adiciona API Google Maps```

Caso haja mais de uma alteração (pertinente ao *commit*) ela deve ser adicionada na descrição do *commit*.

### Política de Branches

O fluxo das *branches* utilizadas deverá seguir o fluxo ***git flow***

* A **master** será a *branch* de produção, sendo ela a *branch* estável.
* A **develop** é a *branch* de homologação, onde todo fluxo de trabalho irá ocorrer antes de fazer o *release* versionado que será feito *merge* na ***master***, ela deve sempre conter o código mais atual, onde as *branchs* de *features* serão ramificadas tendo ela como base.
* Para novas funcionalidades, deve-se seguir o exemplo: ```git checkout -b feature/US05-nome_funcionalidade```. Sendo **feature** a *branch* específica para cada nova funcionalidade ou componente desenvolvido.
* É importante também, fazer a *tag* da versão da *release* da *master* com o seguinte comando: ```git tag -a v1.0.1 -m “Release do novo componente”```
* A branch ***hotfix*** é utilizada para resolver problema crítico em produção que não pode esperar novo release, ou seja, ao identificar qualquer *bug* na ***master***, deve-se criar um ***hotfix***, retornando a solução diretamente para a ***master***, e fazendo o *merge* para a **develop** também.

Veja mais detalhes sobre o fluxo *git flow* [aqui](https://medium.com/trainingcenter/utilizando-o-fluxo-git-flow-e63d5e0d5e04).

#### Conflitos

Se um pull request causar algum tipo de conflito, deve ser resolvido primeiro pela equipe que desenvolveu o que está causando conflito, prezando pela integridade e organização do histórico de commits, e então deve ser refeito o pedido para avaliação do merge.

### Uso de Issues

As issues serão criadas com o objetivo de mapear as histórias de usuário, histórias técnicas e bugs, tendo assim um maior controle sobre eles. Com isso, conseguiremos manter o rastro dos commits com suas respectivas issues.

* As issues serão divididas em labels, para que se possa indicar sua natureza.
* O padrão do nome das issues referentes às funcionalidades terá o seguinte formato:
  * ```US<Número referente à funcionalidade> - <Nome da funcionalidade>```
  * Exemplo: ```US01 - Cadastro e login de usuário```.
* Uma descrição, contendo explicações e passos a serem tomados, deverá ser elaborada.

## Referências

* Utilizando o fluxo Git Flow. Medium. <https://medium.com/trainingcenter/utilizando-o-fluxo-git-flow-e63d5e0d5e04>
* Plano de Gestão e Configuração de Software. Unigrade. <https://ads-unigrade-2019-1.github.io/Wiki/dinamica02/GCS/>
