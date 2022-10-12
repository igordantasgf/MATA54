#include<stdbool.h>
#define GRAU 3
#define FCS 2

typedef struct{
    int chave;
    char nome[20];
    int idade;
} Dados;

typedef struct{
    Registro *endereco_dir;
    Registro *endereco_esq;
    Endereco *pai;
    Dados dados;
    int indice;
    SetaNo *seta;
} Registro;

typedef struct{
    int valor;
    Endereco *end_esq;
    Endereco *end_dir;
} Chave;

typedef struct{
    Chave *dir;
    Chave *esq;
    Chave *filho;
    Registro *filho_regs;

} Endereco;

typedef struct{
    Registro r;
} SetaNo;
