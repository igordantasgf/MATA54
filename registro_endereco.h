#include<stdbool.h>

typedef struct{
    int chave;
    char nome[20];
    int idade;
} Dados;

typedef struct{
    int *endereco_dir;
    int *endereco_esq;
    int *pai;
    int nivel;
    Dados dados;
} Registro;

typedef struct{
    int *pai;
    Registro dir;
    Registro esq;
} endereco;