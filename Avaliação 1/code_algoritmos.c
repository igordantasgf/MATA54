#include <stdio.h>
#include <stdlib.h>

// Tamanho padrão da tabela de dados (m)
#define TABLE_SIZE 1000

// Função hashing (pos = x mod m)
int hash1(int key) {
    return key % TABLE_SIZE;
}

int hash2(int key) {
    return (key % (TABLE_SIZE - 1)) + 1;
}

void inserir_sondagem_linear(int key, int* tabela) {
    int index = hash1(key);
    
    while (tabela[index] != -1) {
        index = (index + 1) % TABLE_SIZE;
    }
    
    tabela[index] = key;
}

void inserir_double_hash(int key, int* tabela) {
    int index = hash1(key);
    int step = hash2(key);
    
    while (tabela[index] != -1) {
        index = (index + step) % TABLE_SIZE;
    }
    
    tabela[index] = key;
}