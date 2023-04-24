#include <stdio.h>
#include <stdlib.h>
#include "code_algoritmos.c"

int main() {
    int* tabela = malloc(TABLE_SIZE * sizeof(int));
    for (int i = 0; i < TABLE_SIZE; i++) {
        tabela[i] = -1;
    }

    //___________________TESTES___________________

    inserir_double_hash(123, tabela);
    inserir_double_hash(456, tabela);
    inserir_double_hash(789, tabela);
    
    // Print the table
    for (int i = 0; i < TABLE_SIZE; i++) {
        printf("%d ", tabela[i]);
    }
    printf("\n");

    // ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    
    free(tabela);
    return 0;
}
