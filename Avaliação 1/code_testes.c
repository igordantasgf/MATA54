#include "code_algoritmos.c"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void test_to_csv(int algm);
int *renew_table();
int *gerador();

int main() {

  int i;
  int algm = 0;
  printf("0 - Gerar testes a partir de arquivos importados\n1 - Gerar testes para o relatório geral\nEntrada: ");
  fflush(stdout);
  scanf("%d", &i);
  int x;

  if(i==0){
    // Padrão: m - n - alpha
    printf("\nRodando Testes pré-definidos...\nDefina o tamanho m:\n");
    
    scanf("%d", &x);
    const int tamanho = x;
    printf("\nDefiniu o tamanho: %d\n", tamanho);

    int lista[tamanho];
    int count = 0;
    int num;
    
    printf("\nEscaneando numeros a serem inseridos:\n(Insira uma letra quando finalizar!)\n");
    while(scanf("%d", &num) == 1){
      lista[count] = num;
      count++;
    }

    //encadeamento explícito
    Node** table = malloc(tamanho * sizeof(Node*));
    for (int i = 0; i < tamanho; i++) {
      table[i] = NULL;
    }

    for(int i=0; i<count; i++){
      inserir_encad_explicito(lista[i], table, tamanho);
    }
    int k=0;
    for(int i=0; i<count; i++){
      k = k + search_encad_explicito(lista[i], table, tamanho);
    }
    for (int i = 0; i < tamanho; i++) {
        Node* current_node = table[i];
        while (current_node != NULL) {
          Node* temp = current_node;
          current_node = current_node->next;
          free(temp);
        }
      }
    printf("\nMédia de acessos para Encadeamento Explícito: %.2f", (float)k/count);

    //Linear Probing
    int *tabela = renew_table(tamanho);
    printf("\n\nLendo números para colocar na lista");
    for(int i=0; i<count; i++){
      inserir_sondagem_linear(lista[i], tabela, tamanho);
    }
    k=0;
    for(int i=0; i<count; i++){
      k = k + search_sondagem_linear(lista[i], tabela, tamanho);
    }
    free(tabela);
    printf("\nMédia de acessos para Sondagem Linear: %.2f", (float)k/count);

    //Double Hashing
    tabela = renew_table(tamanho);
    printf("\n\nLendo números para colocar na lista");
    for(int i=0; i<count; i++){
      inserir_double_hash(lista[i], tabela, tamanho);
    }
    k=0;
    for(int i=0; i<count; i++){
      k = k + search_double_hash(lista[i], tabela, tamanho);
    }
    free(tabela);
    printf("\nMédia de acessos para Double Hashing: %.2f", (float)k/count);

    //Quadratic Probing
    tabela = renew_table(tamanho);
    printf("\n\nLendo números para colocar na lista");
    for(int i=0; i<count; i++){
      inserir_sondagem_quad(lista[i], tabela, tamanho);
    }
    k=0;
    for(int i=0; i<count; i++){
      k = k + search_sondagem_quad(lista[i], tabela, tamanho);
    }
    free(tabela);
    printf("\nMédia de acessos para Quadratic Hashing: %.2f", (float)k/count);

  }
  
  if(i==1){
    //___________________TESTES - Relatório ___________________
     // Encadeamento explícito
    test_to_csv(algm);

    algm = 1; // Linear Probing
    test_to_csv(algm);

    algm = 2; // Double Hashing
    test_to_csv(algm);

    algm = 3; // Quadratic Hashing
    test_to_csv(algm);
    //__________________________________________________________
  }

  return 0;
}

void test_to_csv(int algm) {
    int contagem[TABLE_SIZE];

  for (int i = 0; i < TABLE_SIZE; i++){

    Node** table = malloc(TABLE_SIZE * sizeof(Node*));
    for (int i = 0; i < TABLE_SIZE; i++) {
      table[i] = NULL;
    }
    int *tabela = renew_table(TABLE_SIZE);
    int *numeros = gerador();

  // -------- // -------- Inserção -------- // --------  
    switch(algm){
      case 0:
        for (int k = 0; k <= i; k++) {
          inserir_encad_explicito(numeros[k], table, -1);
        }
        break;

      case 1: // sondagem linear
        for (int k = 0; k <= i; k++) {
          inserir_sondagem_linear(numeros[k], tabela, -1);
        }
        break;

      case 2: // Double hashing
        for (int k = 0; k <= i; k++) {
          inserir_double_hash(numeros[k], tabela, -1);
        }
        break;

      case 3: // sondagem quadratica
        for (int k = 0; k <= i; k++) {
          inserir_sondagem_quad(numeros[k], tabela, -1);
        }
        break;
    }
    // -------- // -------- // -------- // --------  

      int count = 0;

    // -------- // -------- Busca -------- // --------  
    switch(algm){
      case 0:
        for (int k = 0; k <= i; k++) {
          count = count + search_encad_explicito(numeros[k], table, -1);
        }
        break;  
      case 1:
        for (int k = 0; k <= i; k++) {
          count = count + search_sondagem_linear(numeros[k], tabela, -1);
        }
        break;
      case 2:
        for (int k = 0; k <= i; k++) {
          count = count + search_double_hash(numeros[k], tabela, -1);
        }
        break;   
      case 3:
        for (int k = 0; k <= i; k++) {
          count = count + search_sondagem_quad(numeros[k], tabela, -1);
        }
        break;
      }
    // -------- // -------- // -------- // --------  

      contagem[i] = count;
      free(tabela);
      free(numeros);

    if(algm==0){
      // Free memory
      for (int i = 0; i < TABLE_SIZE; i++) {
        Node* current_node = table[i];
        while (current_node != NULL) {
          Node* temp = current_node;
          current_node = current_node->next;
          free(temp);
        }
      }
    }
  }

  for (int i = 0; i < TABLE_SIZE; i++) {
    printf("%d\n", contagem[i]);
  }
}

int *renew_table(int size){
  int *tabela = malloc(size * sizeof(int));
  for (int i = 0; i < size; i++) {
    tabela[i] = -1;
  }
  return tabela;
}

int *gerador() {
  int *lista = malloc(TABLE_SIZE * sizeof(int));
  srand(time(NULL));
  for (int i = 0; i < TABLE_SIZE; i++) {
    int random_num = rand() % 999999999;
    lista[i] = random_num;
  }
  return lista;
}
