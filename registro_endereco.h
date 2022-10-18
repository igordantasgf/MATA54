#include<stdbool.h>
#define GRAU 3
#define FATOR 2

typedef struct{
    int chave;
    char nome[20];
    int idade;
} Dados;

typedef struct{
    Registro *endereco_dir;
    Registro *endereco_esq;
    Chave *pai;
    Dados dados;
    int indice;
} Registro;

typedef struct{
    int valor;
    Registro *end_esq;
    Registro *end_dir;
} Chave;