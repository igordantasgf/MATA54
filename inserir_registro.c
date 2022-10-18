#include <stdio.h>
#include <stdlib.h>

#include "registro_endereco.h"

void inserindo(Registro r_pai, Registro *pont_pai, Registro r_filho, bool direita, FILE *f){ // colocando registro em um nó
    if(direita==true){
        fseek(f, 0, SEEK_END); // armazena registro como filho esquerdo 
        unsigned long position = ftell(f);
        r_filho.pai = pont_pai;
        fwrite(&r_filho, sizeof(Registro), 1, f);

        r_pai.endereco_dir = position; // salva o endereço do filho esquerdo 
        fseek(f, pont_pai, SEEK_SET);
        fwrite(&r_pai, sizeof(Registro), 1, f);
        return;

    }else{
        fseek(f, 0, SEEK_END); // armazena registro como filho esquerdo 
        unsigned long position = ftell(f);
        r_filho.pai = pont_pai;
        fwrite(&r, sizeof(Registro), 1, f);

        r_pai.endereco_esq = position; // salva o endereço do filho esquerdo 
        fseek(f, pont_pai, SEEK_SET);
        fwrite(&r_pai, sizeof(Registro), 1, f);
        return;

    }

}

void inserir_no_r(FILE *f, Registro *pont_pai, bool direita, int n_registros, int fator, Registro r){ // navega no bloco de registros para inserir   
    // Sentido: 0=esq, 1=dir
    f = fopen("dados","rb+");
    int i = 0;
    int contador = 0;
    Registro r_contador, r_escrito, r_pai;
    Registro *r_apontador;
    unsigned long position;

    if (!(f = fopen("dados","r+"))) {
		printf ("Erro na abertura do arquivo \"dados\" - Programa abortado\n");
		exit(-1);       
	}   

    fseek(f, pont_pai, SEEK_SET);
    fread(&r_pai, sizeof(Registro), 1, f);
    
    // Inserção de um registro no nó final de registros

    if(direita==true){//esq
        
        if(r_pai.endereco_esq==NULL){ // se nó a esquerda está vazio         
            inserindo(r_pai, pont_pai, r, direita, f);
        }else{  
            contador=0;
            fseek(f, r_pai.endereco_esq, SEEK_SET);

            while(1){// checagem de registros no nó   
                contador++;
                fread(&r_contador, sizeof(Registro), 1, f);
                if(r_contador.endereco_dir==NULL || contador==2*FATOR-1){
                    break;
                }else{
                    r_apontador = r_contador.endereco_dir;
                    fseek(f, r_apontador, SEEK_SET);
                }
            }

            if(contador==2*FATOR-1){
                quebra_no_registros(); 
            }else{ // inserção no espaço vazio do nó
                fseek(f, 0, SEEK_END);
                r.indice = contador;
                r.endereco_esq = r_apontador;
                position = ftell(f);
                fwrite(&r, sizeof(Registro), 1, f);

                fseek(f, r_apontador, SEEK_SET);
                fread(&r_contador, sizeof(Registro), 1, f);
                r_contador.endereco_dir = position;
                fseek(f, r_apontador, SEEK_SET);
                fwrite(&r_contador, sizeof(Registro), 1, f);
            }
        }
    }else{//dir
        if(r_pai.endereco_dir==NULL){ // se nó a direita está vazio
            inserindo(r_pai, pont_pai, r, direita, f);

        }
    }
}