--Resumo:
Esta pesquisa visa mostrar as vantagens performáticas da Tradução Dinâmica (just-in-time) em contraste com a versão compilada estática. Foi utilizado  como linguagem base para a realização dos testes o Python por possuir duas implementações que abrangem os tópicos anteriormente citados. Compreender as possíveis melhorias executadas no ambiente just-in-time (pypy), analisando por meio de dados, gráficos, e a execução de testes. As estratégias de otimizações utilizam heurísticas, que são identificadas em tempo de execução. Há também a possibilidade de executar configurações atribuídas à máquina virtual, possibilitando a utilização de implementações diversificadas para algumas estruturas, resultando em melhorias para casos mais específicos, como redução de memória, performance, etc. As modificações acontecem internamente, sem alteração nas definições das chamadas dos métodos. Ou seja, para os desenvolvedores as mudanças são irrelevantes. Os desenvolvedores obtém um ganho considerável de flexibilidade para optar por estratégias mais específicas, ou utilizar configurações genéricas que são habilitadas por padrão.

--Introdução

    -Objetivo

    -Estrutura do Trabalho

--Contextualização
    
    -Python

    -Implementações

    -Pypy

    -JIT

--Configurações
    
    -Configurações e Otimizações do Pypy

    -Estratégias de Otimização

--Implementação de Testes
    
    -Dados amostrais sobre performance

    -Dados amostrais sobre teste de carga

    -Dados amostrais sobre tempo de resposta

--Conclusão

    -Gráficos

--Apêndices