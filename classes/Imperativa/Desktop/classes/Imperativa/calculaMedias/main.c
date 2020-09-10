#include <stdio.h>
#include <stdlib.h>

#include "suporte.h"
#include "menus.h"

int main() {
	estrutura dados;
	estrutura * p_dados = (estrutura *)malloc(sizeof(estrutura));

	p_dados->escolha = 1;
	p_dados->tbl1 = -1;
	p_dados->tbl2 = -1;
	p_dados->tbl3 = -1;
	p_dados->tbl4 = -1;
	p_dados->pjbl = -1;

	do {
		menuPrincipal(p_dados);
	} while ((p_dados->escolha) != 3); 

	if(p_dados->escolha == 3) {
		printf("\nEncerrando execução.\n");
	}

	free(p_dados);
}
