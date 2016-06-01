--Resumo
Esta pesquisa visa mostrar as vantagens performáticas da Tradução Dinâmica (just-in-time) em contraste com a versão compilada estática. Foi utilizado  como linguagem base para a realização dos testes o Python por possuir duas implementações que abrangem os tópicos anteriormente citados. Compreender as possíveis melhorias executadas no ambiente just-in-time (pypy), analisando por meio de dados, gráficos, e a execução de testes. As estratégias de otimizações utilizam heurísticas, que são identificadas em tempo de execução. Há também a possibilidade de executar configurações atribuídas à máquina virtual, possibilitando a utilização de implementações diversificadas para algumas estruturas, resultando em melhorias para casos mais específicos, como redução de memória, performance, etc. As modificações acontecem internamente, sem alteração nas definições das chamadas dos métodos. Ou seja, para os desenvolvedores as mudanças são irrelevantes. Os desenvolvedores obtém um ganho considerável de flexibilidade para optar por estratégias mais específicas, ou utilizar configurações genéricas que são habilitadas por padrão.

--Introdução

    -Objetivo

    -Estrutura do Trabalho

--Materiais e métodos - Contextualização
    
        -Python

            Foi criada em dezembro de 1989, criado por Guido van Rossum um programador dos Países Baixos, que desenvolveu a linguagem em algumas semanas que se aproximam do natal. Ganhou esse nome não por referência a serperte, mas pelo grupo inglês de comédia chamado Monty Python. Foi desenvolvida a partir da linguagem ABC.
            Python é uma linguagem de programação com ampla utilização no mercado, empregada em diversas áreas como educacionais, comerciais, científicos, plataformas web, desktop e móvel. Possui uma baixa curva de aprendizado, é concisa e muito produtiva, sua adoção tem crescido bastante. É uma linguagem gratuita e de código-fonte aberto, com versões para os mais variados sistemas. Possui uma grande biblioteca padrão e uma documentação muito intuitiva, o que possibilita sua utilização para vários fins sem a necessidade de bibliotecas externas. Python é uma linguagem de alto nível interpretada, comporta vários paradigmas sendo os mais utilizados o estruturado, orientado à objetos e funcional. É uma linguagem com tipagem forte e dinâmica, também conhecido como Duck Typing, onde os objetos que se comportam de maneira similar são tratados iguais. A linguagem possui um gerenciamento automático de memória, algumas estruturas de dados embutidas na sintaxe da linguagem reduzindo a verbosidade, e é muito conhecida por possuir baterias inclusas, fazendo referência a grande biblioteca padrão que possui vários utilitários.Possui uma comunidade forte e ativa, que é um de seus grandes pontos fortes. Ela se diversifica da maioria das linguagens por utilizar a indentação para definir os blocos de código.

        -Implementações
            Python é uma linguagem interpretada e seu funcionamento é semelhante aos de outras linguagens, como o Java onde o código-fonte é compilado para um bytecode, que é posteriormente interpretado por sua máquina virtual (Python Virtual Machine). Dessa forma podemos ter várias implementações do Python, que por sua vez utilizam mecanismos diferentes para a compilação do código-fonte e interpretação dos bytecodes. Existem várias implementações do Python, como Jython (em java), IronPython(.NET), Stackeless Python, Pypy e a mais famosa é o CPython. Por ser uma linguagem dinamicamente tipada a performance de seu interpretador pode não ser tão eficiente, e é justamente com o foco em eficiência que surgiu o Pypy.

        -Pypy
            O Pypy é um projeto que resultou em um novo interpretador python mais flexível e rápido que o convencional(CPython). Ele possui esse nome pois o sua implementação utiliza o RPython, que é um dialeto da linguagem Python com algumas restrições.
        -JIT

        -Apache JMeter
            O Apache JMeter é uma ferramenta de código aberto que é executado na plataforma do Java, é utilizada para realizar testes de carga em sistemas web. O mesmo possui uma gama gigantesca de plugins e possibilidades de configurações possíbilitando simular uma carga grando de requisições. O funcionamento dele segue a ideia de simular várias requisições simultâneas, que são disparadas para o servidor com os cabeçalhos e dados configurados pelo usuário, conforme as requisições são atendidas os dados colhidos são salvos. O JMeter conta com vários gráficos de saída, métodos de asserção, métodos de confirmação de erro ou determinado status de resposta. Nos exemplos utilizamos o Gráfico Agregado e o Gráfico de Resultados. Os gráficos escolhidos provém os mesmos dados, porém de maneira diferente. O gráfico agregado simplemente exibe o tempo médio, a mediana, o minimo e o tempo máximo decorrido em um gráfico de barras. O gráfico de resultados exibe os mesmos dados em um gráfico de linhas, mostrando esses dados e o desvio conforme os testes são realizados.

        -Matplotlib e Numpy
            O Mathplotlib é uma biblioteca do python utilizada para gerar gŕaficos em geral, normalmente utilizada em conjunto com o Numpy, que uma biblioteca famosa do python na área acadêmica e científica, onde várias operações matemáticas complexas foram implementadas de uma maneira rápida e eficiênciente

    --Configurações
        
        -Configurações e Otimizações do Pypy

        -Estratégias de Otimização

--Resultados - Implementação de Testes
    
    -Dados amostrais sobre performance

    -Dados amostrais sobre teste de carga

    -Dados amostrais sobre tempo de resposta

--Discussão

--Conclusões

    -Gráficos

--Apêndices

--Agradecimentos

--Referências

    -https://www.packtpub.com/books/content/brief-history-python
    -Python Escreva seus primeiros programas, Casa do Código, Felipe Cruz
    -http://www.rudamoura.com/python-bytecode.html
    -https://www.toptal.com/python/por-que-h-tantos-pythons/pt
    -https://www.infoq.com/br/news/2011/11/py-py17
    -http://jmeter.apache.org/
    -https://www.udacity.com/wiki/plotting-graphs-with-python
    -http://wiki.python.org.br/PyPy