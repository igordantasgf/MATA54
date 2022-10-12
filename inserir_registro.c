#include <stdio.h>
#include <stdlib.h>

#include "registro_endereco.h"

int inserir(FILE *f, Chave *raiz_chave, int nivel, int n_registros ,int grau, int chave, char nome[20], int idade){
    
    f = fopen("dados","w+b");

    // Criação do registro para inserção
    Registro r;
    r.dados.chave = chave;
    r.dados.idade= idade;
    for(int i=0;i<20;i++){
        r.dados.nome[i] = nome[i];
    }

    // Algumas instruções prévias:
    //      1. Ter uma variável que indica se já existem chaves;
    //      2. Caso tenha, começar a busca fseek através dessa raiz;
    //      3. Senão, começar fseek por 0, ou seja, o primeiro registro;

    // Caso 1: Arquivo vazio

    if(n_registros==0){
        r.indice=1;
        fseek(f, 0, SEEK_SET);
        fwrite(&r,sizeof(Registro), 1, f);

    // Caso 2: Arquivo não vazio

    }else{ 
        if(raiz_chave!=NULL){ // inserção na sequencia de registros
            fseek(f, 0, SEEK_SET);

            // procurando onde colocar o registro e verificando
            // se o nó está cheio

            while(1){
                fread(&r, sizeof(Registro), 1, f);
                if(r.dados.chave<=chave){ 
                    if(r.endereco_dir!=NULL){
                        fseek(f, r.endereco_dir, SEEK_SET);
                        continue;
                    }
                    if(r.endereco_dir==NULL){
                        fseek(f, r.endereco_dir, SEEK_SET);
                        
                    }
                }
            }
        }else{ // inserção a partir das chaves (raiz)

        }
    }
}