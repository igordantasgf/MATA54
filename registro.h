#include<stdbool.h>

typedef struct{
    int chave;
    char nome[20];
    int idade;
} Registro;

typedef struct{
    Registro atual;
    int nivel;
    Registro *pai;
    Registro *irmao_esq;
    Registro *irmao_dir;
} Estrutura;