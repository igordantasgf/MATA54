#include <stdio.h>
#include <stdlib.h>

#include "registro_endereco.h"

void inserir_bloco_r(FILE *f, Registro r_inicio ,int n_registros, int grau, Registro r){ // navega no bloco de registros para inserir

}

void inserir_raiz_r(FILE *f, Chave *raiz_chave, int n_registros, int grau, Registro r){// busca o espaço para inserção partindo da raiz

}

Chave inserir(FILE *f, Chave *raiz_chave, int n_registros, int grau, int chave, char nome[20], int idade){
    
    f = fopen("dados","w+b");
    SetaNo s;
    
    int i_no=0;

    // Criação do registro para inserção
    Registro r, r_dir, r_esq;
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
        if(raiz_chave!=NULL){ // se não houver chave como raíz, insere diretamente na fila de registros
            fseek(f, 0, SEEK_SET);
            while(1){
                fread(&r_dir, sizeof(Registro), 1, f);
                i_no++;
                if(r_dir.dados.chave >= r.dados.chave){//insere a esquerda
                    if(i_no == 2*grau-1){ // quebra do bloco de registros
                        /// quebra_registro();
                    }else{
                        if(r_dir.endereco_esq==NULL){ // se estiver no inicio da fila de registros
                           
                            fread(&r_dir, sizeof(Registro), 1, f);
                        }
                    }
                }else{ // 

                }
            }
            

            /*while(1){
                fread(&r, sizeof(Registro), 1, f);
                i_no++;
                if(r.dados.chave<chave){ // 1.1 : procurando espaço para o registro
                    if(r.endereco_dir!=NULL){
                        fseek(f, r.endereco_dir, SEEK_SET);
                        continue;
                    }
                    if(r.seta!=NULL){
                        fseek(f, r.seta, SEEK_SET);
                        fread(&s, sizeof(s), 1, f);
                        fseek(f, s.r, SEEK_SET);
                        i_no=0;
                        continue;
                    }
                    if(r.seta==NULL && r.endereco_dir==NULL){//fim da linha de registros: insere

                    }
                }else{ // 1.2 : insere à esquerda se um registro maior ou igual a ele

                }
            }*/
        }else{ // inserção a partir das chaves (raiz)

        }
    }
}