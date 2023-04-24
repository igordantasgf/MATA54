#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Tamanho padrão da tabela de dados (m)
#define TABLE_SIZE 1000

// Função hashing (pos = x mod m)
int hash1(int key){
    return key % TABLE_SIZE;
    // fonte: Cormen et al.
}

int hash2(int key){
    return (key % (TABLE_SIZE - 1)) + 1;
    // fonte: Cormen et al.
}

void inserir_sondagem_linear(int key, int* tabela){
    int index = hash1(key);
    
    while (tabela[index] != -1) {
        index = (index + 1) % TABLE_SIZE;
    }
    
    tabela[index] = key;
}

void inserir_double_hash(int key, int* tabela){
    int index = hash1(key);
    int step = hash2(key);
    
    while (tabela[index] != -1) {
        index = (index + step) % TABLE_SIZE;
    }
    
    tabela[index] = key;
}

int search_sondagem_linear(int key, int* tabela){
    int index = hash1(key);
    int count = 1;
    
    while (tabela[index] != -1) {
        if (tabela[index] == key) {
            //printf("Access count for key %d: %d\n", key, count);
            return count;
        }
        index = (index + 1) % TABLE_SIZE;
        count++;
    }
    
    printf("Key not found.\n");
    return -1;
}

int search_double_hash(int key, int* tabela){
    int index = hash1(key);
    int step = hash2(key);
    int count = 1;
    
    while (tabela[index] != -1) {
        if (tabela[index] == key) {
            //printf("Access count for key %d: %d\n", key, count);
            return count;
        }
        index = (index + step) % TABLE_SIZE;
        count++;
    }
    
    printf("Key not found.\n");
    return -1;
}

