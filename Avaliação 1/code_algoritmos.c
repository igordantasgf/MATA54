#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Tamanho padrão da tabela de dados (m)
#define TABLE_SIZE 1001

typedef struct Node {
    int key;
    struct Node* next;
} Node;

// Função hashing (pos = x mod m)
int hash1(int key) {
    return key % TABLE_SIZE;
  // fonte: Cormen et al.
}

int find_gcd(int, int);

int hash2(int key) {
    int step = TABLE_SIZE - (key % TABLE_SIZE); // PRIME is a large prime number
    int gcd = 0;
    while (gcd != 1) {
      gcd = find_gcd(TABLE_SIZE, step);
      step++;
    }
    return step - 1;
}

//https://dev.to/vosse/open-addressing-13g9
int find_gcd(int a, int b) {
    if (b == 0) {
      return a;
    }else {
      return find_gcd(b, a % b);
    }
}

Node* inserir_encad_explicito(int key, Node** table) {
    int index = hash1(key);
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

int search_encad_explicito(int key, Node** table) {
    int index = hash1(key);
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

void inserir_sondagem_linear(int key, int *tabela) {
    int index = hash1(key);

    while (tabela[index] != -1) {
      index = (index + 1) % TABLE_SIZE;
    }

    tabela[index] = key;
}

int search_sondagem_linear(int key, int *tabela) {
    int index = hash1(key);
    int count = 1;

    while (tabela[index] != -1) {
      if (tabela[index] == key) {
        return count;
      }
      index = (index + 1) % TABLE_SIZE;
      count++;
    }

    printf("Key not found.\n");
    return -1;
}
void inserir_double_hash(int key, int *tabela) {
    int index = hash1(key);
    int step = hash2(key);

    while (tabela[index] != -1) {
      index = (index + step) % TABLE_SIZE;
    }

    tabela[index] = key;
}

int search_double_hash(int key, int *tabela) {
    int index = hash1(key);
    int step = hash2(key);
    int count = 1;
    while (tabela[index] != -1) {
      if (tabela[index] == key) {
        return count;
      }
      index = (index + step) % TABLE_SIZE;
      count++;
    }

    printf("Key not found.\n");
    return -1;
}

void inserir_sondagem_quad(int key, int* table) {
    int index = hash1(key);
    int step = hash2(key);
    int i = 1;
    
    while (table[index] != -1) {
        index = (index + i*i*step) % TABLE_SIZE;
        i++;
    }
    
    table[index] = key;
}

int search_sondagem_quad(int key, int* table) {
    int index = hash1(key);
    int step = hash2(key);
    int i = 1;
    
    while (table[index] != -1 && table[index] != key) {
        index = (index + i*i*step) % TABLE_SIZE;
        i++;
    }
    
    if (table[index] == key) {
        return index;
    } else {
        return -1;
    }
}