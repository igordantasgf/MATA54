#include <stdio.h>
#include <stdlib.h>
#include "registro_endereco.h"

int contagem_no_regs(FILE *f, long endereco_registro){ // conta quantidade de registros em um nó e retorna um inteiro
    int n = 0;
    while(1){
        fseek(f, endereco_registro, SEEK_SET);
        Registro r;
        fread(&r, sizeof(Chave), 1, f);
        n++;
        if(r.registro_dir==NULL){
            return n;
        }else{
            endereco_registro = r.registro_dir;
        }
    }
}

int contagem_no_chaves(FILE *f, long endereco_chave){
    int n = 0;
    while(1){
        fseek(f, endereco_chave, SEEK_SET);
        Chave c;
        fread(&c, sizeof(Chave), 1, f);
        n++;
        if(c.chave_dir==NULL){
            return n;
        }else{
            endereco_chave = c.chave_dir;
        }
    }
}

void quebra_no_registro(long registro_um){
    
}

void quebra_no_chave(){

}