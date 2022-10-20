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

        fseek(f, 0, SEEK_SET);
        while(1){
            fread(&K, sizeof(Registro), 1, f);
            n++;
            if(K.endereco_dir==NULL || n == 2*FATOR-1){
                break;
            }else{
                fseek(f, K.endereco_dir, SEEK_SET);
            }
        }
        if(n == 2*FATOR-1){
            //criação de uma chave a partir do registro do meio. Após isso, inserir registro a partir dessa chave
        }else{
            r.endereco_esq = ftell(f);
            fseek(f,0,SEEK_END);
            K.endereco_dir = ftell(f);
            r.endereco_atual = ftell(f);
            fwrite(&r, sizeof(Registro), 1, f);
            fseek(f,0,K.endereco_atual);
            fwrite(&K, sizeof(Registro), 1, f);
            return;
        }


    } 
}