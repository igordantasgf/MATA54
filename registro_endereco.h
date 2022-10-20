#include<stdbool.h>
#define GRAU 3
#define FATOR 2

typedef struct{
    int chave;
    char nome[20];
    int idade;
} Dados;

typedef struct{
    Registro endereco_dir;
    Registro endereco_esq;
    Registro endereco_atual;
    Chave pai;
    Dados dados;
} Registro;

typedef struct{
    int valor;
    Chave pai;
    Chave atual;
    Registro end_esq;
    Registro end_dir;
} Chave;

typedef struct{
    Chave dir;
    Chave esq;
    Chave filho_chave;
    Registro filho_registro;
} Endereco;