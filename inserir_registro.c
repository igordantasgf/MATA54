#include <stdio.h>
#include <stdlib.h>

#include "registro_endereco.h"

int inserir(FILE *f, bool vazio, int grau, Registro *raiz, int chave, char nome[20], int idade){
    f = fopen("dados","w+");
    Registro r;

    // Operação padrão para qualquer chave: armazenamento de dados
    r.dados.chave = chave;
    r.dados.idade = idade;
    for(int i=0; i<20; i++){
        r.dados.nome[i] = nome[i];
    }

    if(vazio==true){
        r.nivel=0;
        r.endereco_dir=NULL;
        r.endereco_esq=NULL;
        r.pai=NULL;
        
    }else{
        
    }

}