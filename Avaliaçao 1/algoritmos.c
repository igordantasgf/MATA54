#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Tamanho padrão da tabela de dados (m)
#define TABLE_SIZE 997

typedef struct Node {
    int key;
    struct Node* next;
} Node;

// Função hashing (pos = x mod m)
int hash1(int key, int c) {
  if(c==-1){
    return key % TABLE_SIZE;
  }else{
    return key % c;
  }
    
  // fonte: Cormen et al.
}

int find_gcd(int, int);

int hash2(int key, int c) {
    if(c==-1){
      c = TABLE_SIZE;
    }else{
      c = c;
    }
    return 1+(key % (c-1));
}

//https://dev.to/vosse/open-addressing-13g9
int find_gcd(int a, int b) {
    if (b == 0) {
      return a;
    }else {
      return find_gcd(b, a % b);
    }
}

Node* inserir_encad_explicito(int key, Node** table, int c) {
    int index = hash1(key, c);
    
    Node* new_node = malloc(sizeof(Node));
    new_node->key = key;
    new_node->next = NULL;
    
    if (table[index] == NULL) {
      table[index] = new_node;
    }else {
      Node* current_node = table[index];
      while (current_node->next != NULL) {
        current_node = current_node->next;
      }
      current_node->next = new_node;
    }
}

int search_encad_explicito(int key, Node** table, int c) {
    int index = hash1(key, c);
    Node* current_node = table[index];
    int count = 1;

    while (current_node != NULL) {
      if (current_node->key == key) {
        return count;
      }
      current_node = current_node->next;
      count++;
    }
    return -1;
}

void inserir_sondagem_linear(int key, int *tabela, int c) {
    int index = hash1(key, c);
    if(c==-1){
      c = TABLE_SIZE;
    }else{
      c=c;
    }

    while (tabela[index] != -1) {
      index = (index + 1) % c;
    }

    tabela[index] = key;
}

int search_sondagem_linear(int key, int *tabela, int c) {
    int index = hash1(key, c);
    int count = 1;
    if(c==-1){
      c = TABLE_SIZE;
    }else{
      c=c;
    }

    while (tabela[index] != -1) {
      if (tabela[index] == key) {
        return count;
      }
      index = (index + 1) % c;
      count++;
    }

    printf("Key not found.\n");
    return -1;
}
void inserir_double_hash(int key, int *tabela, int c) {
    int index = hash1(key, c);
    int step = hash2(key, c);
    if(c==-1){
      c = TABLE_SIZE;
    }else{
      c=c;
    }

    while (tabela[index] != -1) {
      index = (index + step) % c;
    }

    tabela[index] = key;
}

int search_double_hash(int key, int *tabela, int c) {
    int index = hash1(key, c);
    int step = hash2(key, c);
    int count = 1;
    if(c==-1){
      c = TABLE_SIZE;
    }else{
      c=c;
    }

    while (tabela[index] != -1) {
      if (tabela[index] == key) {
        return count;
      }
      index = (index + step) % c;
      count++;
    }

    printf("Key not found.\n");
    return -1;
}

void inserir_sondagem_quad(int key, int* tabela, int c) {
    int index = hash1(key, c);
    int i = 1;
    if(c==-1){
      c = TABLE_SIZE;
    }else{
      c=c;
    }
    
    while (tabela[index] != -1) {
      index = (index + i*i) % c;
      i++;
    }
    
    tabela[index] = key;
}

int search_sondagem_quad(int key, int* tabela, int c) {
    int index = hash1(key, c);
    int i = 1;
    int count = 1;
    if(c==-1){
      c = TABLE_SIZE;
    }else{
      c=c;
    }
    
    while (tabela[index] != -1) {
      if (tabela[index] == key) {
        return count;
      }
      index = (index + i*i) % c;
      i++;
      count++;
    }
}