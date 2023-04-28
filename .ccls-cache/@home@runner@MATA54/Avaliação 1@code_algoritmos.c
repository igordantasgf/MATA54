#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

// Tamanho padrão da tabela de dados (m)
#define TABLE_SIZE 1001

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

int find_gcd(int a, int b) {
  if (b == 0) {
    return a;
  } else {
    return find_gcd(b, a % b);
  }
}

void inserir_sondagem_linear(int key, int *tabela) {
  int index = hash1(key);

  while (tabela[index] != -1) {
    index = (index + 1) % TABLE_SIZE;
  }

  tabela[index] = key;
}

void inserir_double_hash(int key, int *tabela) {
  int index = hash1(key);
  int step = hash2(key);

  //for (int i = 0; i < TABLE_SIZE; i++) {
  //  printf("%d", tabela[i]);
  //}

  while (tabela[index] != -1) {
    index = (index + step) % TABLE_SIZE;
  }

  //printf("\nInserindo %d na posição %d", key,index);
  tabela[index] = key;
  //printf("\nInseriu\n ");
}

int search_sondagem_linear(int key, int *tabela) {
  int index = hash1(key);
  int count = 1;

  while (tabela[index] != -1) {
    if (tabela[index] == key) {
      // printf("Access count for key %d: %d\n", key, count);
      return count;
    }
    index = (index + 1) % TABLE_SIZE;
    count++;
  }

  printf("Key not found.\n");
  return -1;
}

int search_double_hash(int key, int *tabela) {
  int index = hash1(key);
  int step = hash2(key);
  int count = 1;
  //printf("\nProcurando %d", key);
  while (tabela[index] != -1) {
    if (tabela[index] == key) {
      //printf("\nAchou! Posição %d\n", index);
      // printf("Access count for key %d: %d\n", key, count);
      return count;
    }
    index = (index + step) % TABLE_SIZE;
    count++;
  }

  printf("Key not found.\n");
  return -1;
}
