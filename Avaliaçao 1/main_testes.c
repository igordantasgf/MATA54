#include "algoritmos.c"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void test_to_csv(int algm, FILE *f, FILE *g, FILE *h);
int *renew_table();
int *gerador();

int main() {

  int i;
  printf("0 - Gerar testes a partir de arquivos importados\n1 - Gerar testes para o relatório geral\nEntrada: ");
  fflush(stdout);
  scanf("%d", &i);
  int x;

  if(i==0){ // Testes manuais
    // Padrão: m - n
    printf("\nRodando Testes...\nDefina o tamanho m:\n");
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

    for(int p=0; p<4; p++){
      int k=0;
      Node** table = malloc(tamanho * sizeof(Node*));
      int *tabela = renew_table(tamanho);
      for(int i=0; i<count; i++){
        switch(p){
          case 0:
            inserir_encad_explicito(lista[i], table, tamanho);
            break;
          case 1:
            inserir_sondagem_linear(lista[i], tabela, tamanho);
            break;
          case 2:
            inserir_double_hash(lista[i], tabela, tamanho);
            break;
          case 3:
            inserir_sondagem_quad(lista[i], tabela, tamanho);
            break;
        }
      }
      for(int i=0; i<count; i++){
        switch (p){
          case 0:
            k = k + search_encad_explicito(lista[i], table, tamanho);
            break;
          case 1:
            k = k + search_sondagem_linear(lista[i], tabela, tamanho);
            break;
          case 2:
            k = k + search_double_hash(lista[i], tabela, tamanho);
            break;
          case 3:
            k = k + search_sondagem_quad(lista[i], tabela, tamanho);
            break;
        }
      }
      switch(p){
        case 0:
          printf("\nMedia de acessos para Encadeamento Explicito: %.2f", (float)k/count);
          break;
        case 1:
          printf("\nMedia de acessos para Sondagem Linear: %.2f", (float)k/count);
          break;
        case 2:
          printf("\nMedia de acessos para Double Hashing: %.2f", (float)k/count);
          break;
        case 3:
          printf("\nMedia de acessos para Sondagem Quadratica: %.2f", (float)k/count);
          break;
      }
      free(tabela);
      /*for(int i = 0; i < tamanho; i++){
        Node* current_node = table[i];
        while (current_node != NULL) {
          Node* temp = current_node;
          current_node = current_node->next;
          free(temp);
        }
      }*/
    }
  }
  
  if(i==1){
    //___________________TESTES - Relatório ___________________
    FILE *f;
    FILE *g;
    FILE *h;
    f = fopen("dados.txt", "w");
    fprintf(f, "%d\n", TABLE_SIZE-36);
    fclose(f);
    g = fopen("numeros_inseridos.txt","w");
    fclose(g);
    h = fopen("encad_size_4129_m.txt","w");
    fclose(h);

     // Encadeamento explícito
    int algm = 0;
    test_to_csv(algm, f, g, h);

    algm = 1; // Linear Probing
    test_to_csv(algm, f, g, h);

    algm = 2; // Double Hashing
    test_to_csv(algm, f, g, h);

    algm = 3; // Quadratic Hashing
    test_to_csv(algm, f, g, h);

    //__________________________________________________________
  }

  return 0;
}

void test_to_csv(int algm, FILE *f, FILE *g, FILE *h) {
  f = fopen("dados.txt", "a");
  g = fopen("numeros_inseridos.txt","a");
  h = fopen("encad_size_2027_m.txt","a");
  fseek(f, 0, SEEK_END);
  fseek(g, 0, SEEK_END);
  fseek(h, 0, SEEK_END);
  int contagem[TABLE_SIZE-36];

  for (int i = 0; i < TABLE_SIZE-36; i++){

    Node** table = malloc(TABLE_SIZE * sizeof(Node*));
    for (int i = 0; i < TABLE_SIZE; i++) {
      table[i] = NULL;
    }
    int *tabela = renew_table(TABLE_SIZE);
    int *numeros = gerador();

    for(int p=0; p<TABLE_SIZE; p++){
      fprintf(g, "%d\n", numeros[p]);
    }

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

  
  for (int i = 0; i < TABLE_SIZE-36; i++) {
    printf("%d\n", contagem[i]);
    fprintf(f, "%d\n", contagem[i]);
    if(algm==0){
      fprintf(h, "%d\n", contagem[i]);
    }
  }
  fclose(f);
  fclose(g);
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