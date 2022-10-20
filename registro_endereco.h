#include <stdbool.h>
#define GRAU 3
#define FATOR 2

typedef struct{
    int chave;
    char nome[20];
    int idade;
} Dados;

typedef struct{
    long endereco_dir;
    long endereco_esq;
    long registro_atual;
    long pai;
    Dados dados;
} Registro;

typedef struct{
    int valor;
    long chave_pai;
    long chave_atual;
    long chave_esq;
    long chave_dir;
    long registro_esq;
    long registro_dir;
} Chave;

typedef struct{
    long registro_dir;
    long registro_esq;
} Endereco;