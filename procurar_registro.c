#include <stdio.h>
#include <stdlib.h>

#include <registro_endereco.h>


int procurar_registro(int chave){
    FILE *f;

    if (!(f = fopen("dados","rb+"))) {
		printf ("Erro na abertura do arquivo");
		exit(-1);
	}

    Registro r; // nivel mais baixo da arvore, armazenando registros
    Endereco e; // armazena apontador para filho, chave esq e dir
    Chave c; // armazena chave, e enderecos esq e dir

    /* Por definição a ser feita no código "inserindo_registro",
        a raíz do arquivo sempre será nos (2*GRAU_MINIMO-1) endereços
        iniciais.
    */

    fseek(f,0, SEEK_SET);
    fread(&e, sizeof(Endereco), 1, f);
        
    if(e.dir == -1){ // Caso de lista vazia: primeiro apontador não aponta para ninguém

        print("chave nao encontrada: %d",chave);

    }else{

        int *p;
        int *fila=NULL;
        int ultima_chave;
        p = e.dir;
        

        while(true){
            
            if(fila!=NULL){                 // 0 - Quando encontra-se já na sequência de registros

                fseek(f, fila, SEEK_SET);
                fread(&r, sizeof(Registro), 1, f);

                if(r.dados.chave == chave){     // 0.1 - chave encontrada 

                    print("chave: %d\nnome: %s\nidade: %d");
                    return(1);

                }else{                          // 0.2 - Ainda não é a chave atual
                    if(r.endereco_dir == NULL){     //  0.2.1 - Fim da partição de registros (chegou em um endereco) = nao encontrou
                        print('chave nao encontrada: %d',chave);
                    }else{
                        fila = r.endereco_dir;      //  0.2.2 - Passa para o próximo registro a direita
                    }
                }
            }
            
            fseek(f, p, SEEK_SET); // lendo chave no endereço p
            fread(&c, sizeof(Chave), 1, f);

            if(c.valor <= chave){ // 1 -> chave > valor na Chave
                fseek(f, c.end_dir, SEEK_SET);
                fread(&e, sizeof(Endereco), 1, f);
                
                if(e.dir==NULL){        // 1.1 - sem chaves a direita
                    if(e.filho!=NULL){     // 1.1.1 - tem chave como filho
                        p = e.filho;
                    }else{                 // 1.1.2 - tem registro como filho 
                        fila = e.filho_regs;
                         
                    }
                }
            }

            

    }

}

