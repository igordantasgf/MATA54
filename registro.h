#include<stdbool.h>

typedef struct{
    int chave;
    char nome[20];
    int idade;
} Dados;

typedef struct{
    Dados dados;
    int nivel;
    Dados *pai;
    Dados *irmao_esq;
    Dados *irmao_dir;
    bool raiz;
} Registro;