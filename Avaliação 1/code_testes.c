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

  algm = 3; // Double Hashing
  test_to_csv(algm);

  return 0;
}

void test_to_csv(int algm) {
    int contagem[TABLE_SIZE];

  for (int i = 0; i < TABLE_SIZE; i++){

    Node** table = malloc(TABLE_SIZE * sizeof(Node*));
    for (int i = 0; i < TABLE_SIZE; i++) {
      table[i] = NULL;
    }
    int *tabela = renew_table();
    int *numeros = gerador();

  // -------- // -------- Inserção -------- // --------  
    switch(algm){
      case 0:
        for (int k = 0; k <= i; k++) {
          inserir_encad_explicito(numeros[k], table);
        }
        break;

      case 1: // sondagem linear
        for (int k = 0; k <= i; k++) {
          inserir_sondagem_linear(numeros[k], tabela);
        }
        break;

      case 2: // Double hashing
        for (int k = 0; k <= i; k++) {
          inserir_double_hash(numeros[k], tabela);
        }
        break;

      case 3: // sondagem quadratica
        for (int k = 0; k <= i; k++) {
          inserir_sondagem_quad(numeros[k], tabela);
        }
        break;
    }
    // -------- // -------- // -------- // --------  

      int count = 0;

    // -------- // -------- Busca -------- // --------  
    switch(algm){
      case 0:
        for (int k = 0; k <= i; k++) {
          count = count + search_encad_explicito(numeros[k], table);
        }
        break;  
      case 1:
        for (int k = 0; k <= i; k++) {
          count = count + search_sondagem_linear(numeros[k], tabela);
        }
        break;
      case 2:
        for (int k = 0; k <= i; k++) {
          count = count + search_double_hash(numeros[k], tabela);
        }
        break;   
      case 3:
        for (int k = 0; k <= i; k++) {
          count = count + search_sondagem_quad(numeros[k], tabela);
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

int *renew_table(){
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
