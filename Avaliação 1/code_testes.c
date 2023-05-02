#include "code_algoritmos.c"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void test_to_csv(int algm);
int *renew_table();
int *gerador();

int main() {
  //___________________TESTES___________________
  int algm = 0; // Encadeamento explícito
  test_to_csv(algm);

  algm = 1; // Linear Probing
  test_to_csv(algm);

  algm = 2; // Double Hashing
  test_to_csv(algm);

  return 0;
}

void test_to_csv(int algm) {
  int contagem[TABLE_SIZE];
  
  switch (algm) {

  case 0: // encadeamento explícito 

    printf("Chamada para encadeamento explícito.\n");
    for (int i = 0; i < TABLE_SIZE; i++) { // fator de carga (alpha) n/m
      
      Node** table = malloc(TABLE_SIZE * sizeof(Node*));
      for (int i = 0; i < TABLE_SIZE; i++) {
        table[i] = NULL;
      }

      int *numeros = gerador();

      for (int k = 0; k <= i; k++) {
        inserir_encad_explicito(numeros[k], table);
      }
      int count = 0;
      for (int k = 0; k <= i; k++) {
        count = count + search_encad_explicito(numeros[k], table);
      }
      contagem[i] = count;

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
    // PRINT: Número de acessos
    for (int i = 0; i < TABLE_SIZE; i++) {
      printf("%d\n", contagem[i]);
    }
    // sleep(8);
    break;

  case 1: // Linear Probing

    printf("Chamada para linear probing.\n");
    for (int i = 0; i < TABLE_SIZE; i++) { // fator de carga (alpha) n/m
      int *tabela = renew_table();
      int *numeros = gerador();
      for (int k = 0; k <= i; k++) {
        inserir_sondagem_linear(numeros[k], tabela);
      }
      int count = 0;
      for (int k = 0; k <= i; k++) {
        count = count + search_sondagem_linear(numeros[k], tabela);
      }
      contagem[i] = count;
      free(tabela);
      free(numeros);
    }
    // PRINT: Número de acessos
    for (int i = 0; i < TABLE_SIZE; i++) {
      printf("%d\n", contagem[i]);
    }
    // sleep(8);
    break;

  case 2: // Double Hashing

    printf("Chamada para  Double Hashing.\n");
    for (int i = 0; i < TABLE_SIZE; i++) { // fator de carga (alpha) n/m
      int *tabela = renew_table();
      int *numeros = gerador();
      for (int k = 0; k <= i; k++) {
        inserir_double_hash(numeros[k], tabela);
      }
      int count = 0;
      for (int k = 0; k <= i; k++) {
        count = count + search_double_hash(numeros[k], tabela);
      }
      contagem[i] = count;
      free(tabela);
      free(numeros);
    }
    // PRINT: Número de acessos
    for (int i = 0; i < TABLE_SIZE; i++) {
      printf("%d\n", contagem[i]);
    }
    // sleep(8);
    break;
  }
}

int *renew_table() {
  int *tabela = malloc(TABLE_SIZE * sizeof(int));
  for (int i = 0; i < TABLE_SIZE; i++) {
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