#include <stdio.h>
#include <stdlib.h>

// Definição da estrutura principal
struct obj {
	int linhas;
	int colunas;
	double* matriz;
};

// Definição de um alias -> matrix para struct obj
typedef struct obj matrix;

// Função que retorna ponteiro para nova struct alocada
matrix* createMatrix(int m, int n) {

	matrix* local = (struct obj *)(malloc(sizeof(matrix)));
	
	local->linhas = m;
	local->colunas = n;
	local->matriz = (double *)(malloc(sizeof(double) * m * n));
	
	int i, j;
	for(i = 0; i < local->linhas; i++) {
		for(j = 0; j < local->colunas; j++) {
			int valor;
			printf("digite o valor na posição %i, %i: ", i, j);
			scanf("%i", &valor);
			local->matriz[i * local->colunas + j] = valor;
		}
	}
	return local;
}

//Função que imprime matriz
void printMatrix(matrix* mat) {
	int lin = mat->linhas;
	int col = mat->colunas;
	int i, j;
	for(i = 0; i < lin; i++) {
		printf("\n");
		for(j = 0; j < col; j++) {
			printf("%f ", mat->matriz[i*col + j]);
		}
	}
	printf("\n");
}

// Função que cria uma cópia de uma matriz, multiplicando seus valores pelo escalar n
matrix* multMatrix(matrix* mat, int n) {
	
	matrix* mat_final = (struct obj *)(malloc(sizeof(matrix)));
	
	mat_final->linhas = mat->linhas;
	mat_final->colunas = mat->colunas;
	mat_final->matriz = (double *)(malloc(sizeof(double) * mat_final->linhas * mat_final->colunas));
	
	int i, j, lin = mat_final->linhas, col = mat_final->colunas;
	for(i = 0; i < lin; i++) {
		for(j = 0; j < col; j++) {
			int valor;
			valor = n * mat->matriz[i * col + j];
			mat_final->matriz[i * col + j] = valor;
		}
	}
	return mat_final;
}

// Função que copia uma matriz
matrix* copyMatrix(matrix *mat) {
	
	matrix* mat_final = (struct obj *)(malloc(sizeof(matrix)));
	
	mat_final->linhas = mat->linhas;
	mat_final->colunas = mat->colunas;
	mat_final->matriz = (double *)(malloc(sizeof(double) * mat_final->linhas * mat_final->colunas));
	
	int i, j, lin = mat_final->linhas, col = mat_final->colunas;
	for(i = 0; i < lin; i++) {
		for(j = 0; j < col; j++) {
			mat_final->matriz[i * col + j] = mat->matriz[i * col + j];
		}
	}
	return mat_final;

}

// Função que libera memória das structs alocadas
void freeMatrix(matrix* mat) {
	free(mat->matriz);
	free(mat);
}

// Função principal - Método main
int main() {
	matrix* inicial;
	inicial = createMatrix(2, 2);
	printMatrix(inicial);

	matrix* inicial_multiplicada;
	inicial_multiplicada = multMatrix(inicial, 4);
	printMatrix(inicial_multiplicada);

	matrix* inicial_copia;
	inicial_copia = copyMatrix(inicial);
	printMatrix(inicial_copia);
	
	freeMatrix(inicial);
	freeMatrix(inicial_multiplicada);
	freeMatrix(inicial_copia);
	
	return 0;
}
