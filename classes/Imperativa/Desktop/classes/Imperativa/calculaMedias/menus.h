#ifndef menus
#define menus

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include "suporte.h"
#include "notas.h"

void menuTrabalhos(estrutura * p_dados) {
	cls();
	printf("--- Menu dos Trabalhos ---\n");
	printf("1) Nota TBL 1\n");
	printf("2) Nota TBL 2\n");
	printf("3) Nota TBL 3\n");
	printf("4) Nota TBL 4\n");
	printf("5) Nota PjBL\n");
	printf("6) Voltar ao menu principal\n");
	printf("Digite a opção: \n\n");
	int i;
	scanf("%i", &i);

	switch(i) {
		case(1):
			if(p_dados->tbl1 < 0) {
				addNota(p_dados, 1);
			} else {
				modNota(p_dados, 1);
			}
			break;
		case(2):
			if(p_dados->tbl2 < 0) {
				addNota(p_dados, 2);
			} else {
				modNota(p_dados, 2);
			}
			break;
		case(3):
			if(p_dados->tbl3 < 0) {
				addNota(p_dados, 3);
			} else {
				modNota(p_dados, 3);
			}
			break;
		case(4):
			if(p_dados->tbl4 < 0) {
				addNota(p_dados, 4);
			} else {
				modNota(p_dados, 4);
			}
			break;
		case(5):
			if(p_dados->pjbl < 0) {
				addNota(p_dados, 5);
			} else {
				modNota(p_dados, 5);
			}
			break;
		case(6):
			break;
		default:
			printf("\nOpção inválida!\n");
			printf("Retornando ao menu principal.\n");
			sleep(2);
			break;
	}
}


void menuMedias(estrutura * p_dados){
	cls();
	printf("--- Menu de Médias ---\n");	
	printf("1) Média RA1\n");
	printf("2) Média RA2\n");
	printf("2) Média RA3\n");
	printf("2) Média RA4\n");
	printf("2) Média Total\n");
	printf("2) Situação\n");
	printf("Digite a opção: ");
	int i;
	scanf("%i",&i);
}


void menuPrincipal(estrutura * p_dados) {
	cls();

	printf("--- Menu Principal ---\n");
	printf("1) Trabalhos \n");
	printf("2) Médias \n");
	printf("3) Sair \n");
	printf("Digite a opção: \n\n");
	int i;
	scanf("%i", &i);
	if (i == 1) {
		menuTrabalhos(p_dados);
	} else if (i == 2) {
		menuMedias(p_dados);
	} else if (i == 3) {
		p_dados->escolha = 3;
		return;
	} else {
		printf("\nOpção inválida!!\n------------\n");
		sleep(2);
	}
}

#endif
