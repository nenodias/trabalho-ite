Just-In-Time Compilation

Na computação o termo just-in-time compilation, também conhecida como tradução dinâmica, é uma forma de melhorar a performance de programas baseados em byte code (código de máquina virtual). Normalmente a execução de códigos interpretados é mais lenta que a de códigos compilados para a linguagem de máquina. Para contornar esse problema, o byte code é carregado em memória, e o programa pode ser executado. Posteriormente a máquina virtual identifica a ocorrência de várias chamadas para algum arquivo, método ou bloco de código (Hotspots). Com esse hotspot identificado, a máquina virtual faz a compilação desse bytecode para linguagem de máquina, que e é salvo em cache para que seja executado mais rápido nas próximas ocorrências.
A compilação JIT representa uma abordagem híbrida, onde parte do código executado é interpretado, em conjunto com código compilado em tempo de execução para reduzir os impactos no desempenho.

(http://www.ebooklibrary.org/articles/Just-in-time_compiler, World Heritage Encyclopedia)

Just-In-Time Compilation - Detalhes Técnicos

Um compilador JIT Tracing passa por várias fases em sua execução. Primeiro os hotspots são identificados (Profiling Phase) e após as informações sobre eles serem recolhidas, um tipo especial de chamada que registra todas as operações para esse hotspot. Essa sequencia de operações é chamada trace. Quando esse hotspot for executado novamente, uma versão compilada do seu trace será chamada.

Just-In-Time Compilation - Profiling Phase/ Fase de Identificação Hotspots
O objetivo dessa etapa é identificar os hotspots. Isso normalmente é feito por uma contagem no número de chamadas e/ou iterações para cada bloco. Após a contagem ultrapassar um determinado limite, o bloco passa a ser considerado um hotspot, então a máquina virtual marca esse bloco como em modo trace, onde ela pode rastrear as chamadas a esse bloco.

Just-In-Time Compilation - Tracing Phase/ Fase de Rastreamento
Nesta fase o bloco é executado normalmente, porém cada operação executada é registrada no trace. As informações são gravadas em uma forma de representação intermediária. Esse registrador segue as chamadas das funções e faz seu registro sequencial no trace. A execução continua até que todas as operações do bloco sejam registradas.
Após o registro das operações do bloco, o fluxo de execução desse bloco percorrido procurando os caminhos onde operações a serem executadas podem divergir. Nesses pontos são inseridos no trace uma instrução especial de guarda, um exemplo de um local é onde existem declarações "if". A guarda é uma verificação rápida para determinar se a condição original ainda é verdadeira. Caso a verificação falhe a execução do trace é abortada.
Enquanto essa fase é executada algumas informações correspondentes a execução desse bloco são armazenadas, como por exemplo o tipo dos dados, pois essas informações podem ser utilizadas nas fases de otimização.

(http://www.ebooklibrary.org/article/WHEBN0035604013/Tracing%20just-in-time%20compilation)

## Pesquisar referências sobre os passos das otimizações possíveis
 
Just-In-Time Compilation - Optimization Phase and Code Generation Phase / Fase de Otimizações e Fase de Geração
A fase de otimização do trace é fácil, já que eles são representações apenas de um caminho de execução.
As otimizações possíveis são:
 - Constant Subexpression Elimination (Eliminação de Subexpressões por Constantes)
 - Dead Code Elimination (Eliminação de Código Morto)
 - Register Allocation (Alocação de Registros)
 - invariant code motion (Movimento de Código Invariável)
 - contant folding (Dobramento de Contantes)
 - escape analysis (Análise de Escape)
 
Depois das otimizações o trace é transformado em código de máquina.


Just-In-Time Compilation - Execution Phase / Fase de Execução

Depois que o trace é compilado ele pode ser executado, ele será executado até que uma instrução de guarda falhar.


Python

-Introdução
Python é uma linguagem fácil e de baixa curva de aprendizado,
"Python é uma linguagem de altíssimo nível (em inglês, Very High Level Language) orientada a objeto, de tipagem dinâmica e forte, interpretada e interativa."
(Eduardo Borges, 2010, p13) "Python para Desenvolvedores"

-Características



documento - https://drive.google.com/file/d/0Bx5VjHTESJ_xZlVxMEVxZHFQMmM/view?usp=sharing

(http://www.ebooklibrary.org/article/WHEBN0000023862/Python%20(programming%20language) )
(http://www.ebooklibrary.org/articles/eng/RPython)

(http://www.aosabook.org/en/pypy.html)