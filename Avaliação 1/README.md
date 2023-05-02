# Avaliação de Desempenho de Algoritmos Hashing
##### Igor Dantas Gomes Franca
###### Prof.º George Marconi
###### Estruturas de Dados e Algoritmos 2
###### Universidade Federal da Bahia
---

### Objetivo:
Avaliar o desempenho de algoritmos de hashing apresentados em sala de aula, na matéria Estrutura de Dados e Algoritmos 2, ministrada pelo Prof.º George Marconi, com o intuito de avaliar a complexidade e desempenho dos algoritmos a serem apresentados, através da computação de medidas estatísticas e visualização de gráficos.

---

### Objetos de Estudo:
Seguem abaixo os algoritmos definidos pelo professor (1-3) e uma abordagem de hashing de livre escolha (4):
1. Encadeamento explcito com o uso de ponteiros usando alocação estática de memória
2. Endereçamento aberto com sondagem linear
3. Endereçamento aberto com duplo hashing
4. Hashing Perfeito em dois níveis **(temporário)**

---

### Método:
A priori, serão implementados na linguagem C (MinGW GCC-6.3.0-1) os algoritmos citados. Para possibilitar a análise de desempenho, serão implementados funções de inserção (certas quantidades de números gerados aleatoriamente) em uma tabela estática, e funções de busca de um número aleatório inserido. Com isso, pode-se armazenar variáveis contendo o número de acessos em cada busca, para diferentes coeficientes de fator de carga $(\alpha = \frac{m}{n})$.

Esses números serão armazenados em um arquivo .csv para serem importados através da linguagem Python (3.8.5), em que a geração de gráficos e análise dos dados será mais eficiente e sucinta. Serão obtidos séries de médias e desvios padrão para cada algoritmo, histogramas e gráficos de dispersão.

---
