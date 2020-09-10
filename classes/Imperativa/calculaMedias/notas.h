#ifndef notas
#define notas

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdbool.h>

#include "suporte.h"

void addNota(estrutura * p_dados, int i) {
	double d;
	switch(i) {
		case(1):
			printf("Digite o valor desejado: ");
			scanf("%lf", &d);
			if (d > 0 && d < 100) {
				p_dados->tbl1 = d;
				printf("\nFeito!\n");
				printf("Novo valor: %.2lf.\n", p_dados->tbl1);
				sleep(1);
				cls();
			} else {
				printf("Valor inválido!\n");
				printf("Retornando ao menu principal.\n");
				sleep(1);
				break;
			}
			break;
		case(2):
			printf("Digite o valor desejado: ");
			scanf("%lf", &d);
			if (d > 0 && d < 100) {
				p_dados->tbl2 = d;
				printf("\nFeito!\n");
				printf("Novo valor: %.2lf.\n", p_dados->tbl2);
				sleep(1);
				cls();
			} else {
				printf("Valor inválido!\n");
				printf("Retornando ao menu principal.\n");
				sleep(1);
				break;
			}
			break;
		case(3):
			printf("Digite o valor desejado: ");
			scanf("%lf", &d);
			if (d > 0 && d < 100) {
				p_dados->tbl3 = d;
				printf("\nFeito!\n");
				printf("Novo valor: %.2lf.\n", p_dados->tbl3);
				sleep(1);
				cls();
			} else {
				printf("Valor inválido!\n");
				printf("Retornando ao menu principal.\n");
				sleep(1);
				break;
			}
			break;
		case(4):
			printf("Digite o valor desejado: ");
			scanf("%lf", &d);
			if (d > 0 && d < 100) {
				p_dados->tbl4 = d;
				printf("\nFeito!\n");
				printf("Novo valor: %.2lf.\n", p_dados->tbl4);
				sleep(1);
				cls();
			} else {
				printf("Valor inválido!\n");
				printf("Retornando ao menu principal.\n");
				sleep(1);
				break;
			}
			break;
		case(5):
			printf("Digite o valor desejado: ");
			scanf("%lf", &d);
			if (d > 0 && d < 100) {
				p_dados->pjbl = d;
				printf("\nFeito!\n");
				printf("Novo valor: %.2lf.\n", p_dados->pjbl);
				sleep(1);
				cls();
			} else {
				printf("Valor inválido!\n");
				printf("Retornando ao menu principal.\n");
				sleep(1);
				break;
			}
			break;
		case(6):
			printf("Retornando ao menu principal.\n");
			sleep(1);
			break;
		default:
			printf("Valor inválido!\n");
			printf("Retornando ao menu Principal.\n");
			sleep(1);
	}
}

void modNota(estrutura * p_dados, int i) {
	double d;
	switch(i){
		case(1):
			printf("Valor antigo: %.2lf.\n", p_dados->tbl1);
			printf("Digite o valor desejado: ");
			scanf("%lf", &d);
			if (d > 0 && d < 100) {
				p_dados->tbl1 = d;
				printf("\nFeito!\n");
				printf("Novo valor: %.2lf.\n", p_dados->tbl1);
				sleep(3);
				cls();
			} else {
				printf("Valor inválido!\n");
				printf("Retornando ao menu principal.\n");
				sleep(2);
				break;
			}
			break;
		case(2):
			printf("Valor antigo: %.2lf.\n", p_dados->tbl2);
			printf("Digite o valor desejado: ");
			scanf("%lf", &d);
			if (d > 0 && d < 100) {
				p_dados->tbl2 = d;
				printf("\nFeito!\n");
				printf("Novo valor: %.2lf.\n", p_dados->tbl2);
				sleep(3);
				cls();
			} else {
				printf("Valor inválido!\n");
				printf("Retornando ao menu principal.\n");
				sleep(2);
				break;
			}
			break;
		case(3):
			printf("Valor antigo: %.2lf.\n", p_dados->tbl3);
			printf("Digite o valor desejado: ");
			scanf("%lf", &d);
			if (d > 0 && d < 100) {
				p_dados->tbl3 = d;
				printf("\nFeito!\n");
				printf("Novo valor: %.2lf.\n", p_dados->tbl3);
				sleep(3);
				cls();
			} else {
				printf("Valor inválido!\n");
				printf("Retornando ao menu principal.\n");
				sleep(2);
				break;
			}
			break;
		case(4):
			printf("Valor antigo: %.2lf.\n", p_dados->tbl4);
			printf("Digite o valor desejado: ");
			scanf("%lf", &d);
			if (d > 0 && d < 100) {
				p_dados->tbl4 = d;
				printf("\nFeito!\n");
				printf("Novo valor: %.2lf.\n", p_dados->tbl4);
				sleep(3);
				cls();
			} else {
				printf("Valor inválido!\n");
				printf("Retornando ao menu principal.\n");
				sleep(2);
				break;
			}
			break;
		case(5):
			printf("Valor antigo: %.2lf.\n", p_dados->pjbl);
			printf("Digite o valor desejado: ");
			scanf("%lf", &d);
			if (d > 0 && d < 100) {
				p_dados->pjbl = d;
				printf("\nFeito!\n");
				printf("Novo valor: %.2lf.\n", p_dados->pjbl);
				sleep(3);
				cls();
			} else {
				printf("Valor inválido!\n");
				printf("Retornando ao menu principal.\n");
				sleep(2);
				break;
			}
			break;
		default:
			printf("Valor inválido!.\n");
			printf("Retornando ao menu Principal.\n");
			sleep(2);
	}
}

bool verificaMedia(double tbl, double pjbl) {
	if((tbl >= 0) && (pjbl >= 0)) {
	return true;
	} 
	return false;
} 

double calculaMedia(double tbl, double pjbl) {
	return tbl * 0.6 + pjbl * 0.4;
}

double mediaFinal(double tbl1, double tbl2, double tbl3, double tbl4, double pjbl) {
	
	double ra1 = tbl1 * 0.6 + pjbl * 0.4;
	double ra2 = tbl2 * 0.6 + pjbl * 0.4;
	double ra3 = tbl3 * 0.6 + pjbl * 0.4;
	double ra4 = tbl4 * 0.6 + pjbl * 0.4;
	
	double media_final = ra1 * 0.2 + ra2 * 0.3 + ra3 * 0.3 + ra4 * 0.2;

	return media_final;
}
#endif
