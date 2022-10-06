#include<stdbool.h>

typedef struct{
    int chave;
    char nome[20];
    int idade;
} Dados;

typedef struct{
    Registro *endereco_dir = NULL;
    Registro *endereco_esq = NULL;
    Endereco *pai = NULL;
    Dados dados;
} Registro;

typedef struct{
    int valor;
    Endereco *end_esq;
    Endereco *end_ dir;
} Chave;

typedef struct{
    Chave *dir = NULL;
    Chave *esq = NULL;
    Chave *filho = NULL;
    Registro *filho_regs = NULL;

} Endereco; 