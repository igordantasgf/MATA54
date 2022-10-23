#include <stdio.h>
#include <stdlib.h>
#include "registro_endereco.h"

void inserindo(FILE *f, Registro r, bool nulo, bool raiz_chave, long raiz){ // colocando registro em um nó

    if (!(f = fopen("dados","wb+"))) {
		printf ("Erro na abertura do arquivo \"dados\" - Programa abortado\n");
		exit(-1);
	}

    if(raiz_chave == false && nulo == false){// Se a raíz for um registro
        Registro K;
        int n;
        
        if(n == 2*FATOR-1){
            //criação de uma chave a partir do registro do meio. Após isso, inserir registro a partir dessa chave
        }else{
            r.endereco_esq = ftell(f);
            fseek(f,0,SEEK_END);
            K.endereco_dir = ftell(f);
            r.registro_atual = ftell(f);
            fwrite(&r, sizeof(Registro), 1, f);
            fseek(f,0,K.registro_atual);
            fwrite(&K, sizeof(Registro), 1, f);
            return raiz;
        }
    } 

    if(nulo==true){// Nada armazenado
        fseek(f, 0, SEEK_SET);
        fwrite(&r, sizeof(Registro), 1, f); // o primeiro registro, de início, fica na posição zero
        return;
    }
    
    if(raiz_chave == true){
        Chave c;

        fseek(f,raiz,SEEK_SET);
        fread(&c, sizeof(Chave), 1, f);
        if(c.valor <= r.dados.chave){// se a chave indica valor a esquerda
            if(c.chave_esq == NULL){ // não aponta para chave, aponta para um registro
                //contagem de registros no nó
                // se menor que 2*fator-1, inserir
                // senão, quebra
            }else{// aponta para chave
                //repete o processo com novo fseek
            }
        }else{ // se a chave indica valor a direita
            if(c.chave_dir == NULL){ // 
                //
                // 
                // 
            }else{// 
                //
            }
        }
    }
}   