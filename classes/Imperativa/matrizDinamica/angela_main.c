#include <stdio.h>
#include <stdlib.h>

struct Matriz{
   int *m, *n, **matriz;
};

struct Matriz *criarMatriz(int m, int n){
   int matriz[m][n];
   int linha, coluna;
   for (linha = 0; linha < m; linha++) {
       for (coluna = 0; coluna < n; coluna++) {
           printf("Entre com o valor da posição %d da coluna e da linha: ", linha+1, coluna+1);
           scanf("%d", &matriz[linha][coluna]);
       }
   }
}

void imprimirMatriz(struct Matriz *m){
   int linha, coluna;

   for (linha = 0; linha < m; linha++) {
       for (coluna = 0; coluna < m; coluna++){
           printf("%3d", m[linha]);
       }
   }
}



int main() {
   int linhas;
   int colunas;
   int *m, *n, **matriz;

   printf("Digite o numero de linhas: ");
   scanf("%d", &linhas);
   m = (int *)malloc(sizeof(int)*linhas);
   if(m == NULL){
       printf("\nErro de alocação de memoria m");
   }

   printf("Digite o numero de colunas: ");
   scanf("%d", &colunas);
   n = (int *)malloc(sizeof(int)*colunas);
   if(m == NULL){
       printf("\nErro de alocação de memoria n");
   }

   criarMatriz(linhas, colunas);
   imprimirMatriz(**matriz);

   return 0;
}

