#ifndef menus
#define menus

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdbool.h>

#include "suporte.h"
#include "notas.h"

void menuTrabalhos(estrutura * p_dados) {
	cls();

	printf("--- Menu dos Trabalhos ---\n");
	
	if(p_dados->tbl1 < 0) {
		printf("1) Nota TBL 1\n");
	} else{
		printf("1) Nota TBL 1 (%.2lf)\n", p_dados->tbl1);	
	}if(p_dados->tbl2 < 0) {
		printf("2) Nota TBL 2\n");
	} else{
		printf("2) Nota TBL 2 (%.2lf)\n", p_dados->tbl2);	
	}if(p_dados->tbl3 < 0) {
		printf("3) Nota TBL 3\n");
	} else{
		printf("3) Nota TBL 3 (%.2lf)\n", p_dados->tbl3);	
	}if(p_dados->tbl4 < 0) {
		printf("4) Nota TBL 4\n");
	} else{
		printf("4) Nota TBL 4 (%.2lf)\n", p_dados->tbl4);	
	}if(p_dados->pjbl < 0) {
		printf("5) Nota PjBL\n");
	} else{
		printf("5) Nota PjBL (%.2lf)\n", p_dados->pjbl);	
	}
	
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
	

	bool valida_media = verificaMedia(p_dados->tbl1, p_dados->pjbl);
	if(valida_media) {
		printf("Média RA1: %.2lf\n", calculaMedia(p_dados->tbl1, p_dados->pjbl));
	} else {
		printf("Média RA1 indisponível.\n");
	}
	
	valida_media = verificaMedia(p_dados->tbl2, p_dados->pjbl);
	if(valida_media) {
		printf("Média RA2: %.2lf\n", calculaMedia(p_dados->tbl2, p_dados->pjbl));
	} else {
		printf("Média RA2 indisponível.\n");
	}

	valida_media = verificaMedia(p_dados->tbl3, p_dados->pjbl);
	if(valida_media) {
		printf("Média RA3: %.2lf\n", calculaMedia(p_dados->tbl3, p_dados->pjbl));
	} else {
		printf("Média RA3 indisponível.\n");
	}

	valida_media = verificaMedia(p_dados->tbl4, p_dados->pjbl);
	if(valida_media) {
		printf("Média RA4: %.2lf\n", calculaMedia(p_dados->tbl4, p_dados->pjbl));
	} else {
		printf("Média RA4 indisponível.\n");
	}

	double media = mediaFinal(p_dados->tbl1, p_dados->tbl2, p_dados->tbl3, p_dados->tbl4, p_dados->pjbl);
	printf("Média final: %.2lf\n", media);

	if ((media >= 0) &&  (media < 70)) {
		printf("Situação: Reprovado!\n");
	} else if(media >= 70) {
		printf("Situação: Aprovado!\n");
	} else{
		printf("Situação: Indisponível.\n");
	}
	printf("\n\nDigite qualquer número para retornar ao menu principal.\n");

	int j;
	scanf("%i", &j);
	return;
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
