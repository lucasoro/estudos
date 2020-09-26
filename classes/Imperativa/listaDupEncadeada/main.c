#include <stdio.h>
#include <stdlib.h>

// Definição da estrutura de nó
struct objeto {
	struct objeto* prev;
	struct objeto* next;
	int val;
};

// Definições utilizadas para simplicidade no código
typedef struct objeto node;

// Método para inserção do primeiro nó na lista
void insere_head(node **lista) {
	node *local = malloc(sizeof(node));
	int valor;
	printf("Digite o valor a ser inserido: \n");
	scanf("%d", &valor);
	local->val = valor;
	local->next = NULL;
	local->prev = NULL;
	*lista = local;
}

// Método para inserção de nós na lista
void insere_node(node **lista, node *aloc) {
	node *local = *lista;
	// Verifica se o head da lista já é maior que o valor do input, e substitui o head caso seja
	if(aloc->val <= local->val) {
		(*lista)->prev = aloc;
		aloc->next = *lista;
		*lista = aloc;
	} else {
		// Percorre a lista até chegar em um valor maior que o valor fornecido
		while((aloc->val >= local->val) && (local->next != NULL)) {
			local = local->next;
		}
		// Caso especial - final da lista, último termo
		if((aloc->val >= local->val) && (local->next == NULL)) {
			local->next = aloc;
			aloc->prev = local;
			return;
		}
		// Reorganiza os ponteiros
		node* anterior = local->prev;
		anterior->next = aloc;
		aloc->prev = anterior;
		aloc->next = local;
		local->prev = aloc;
	}
}

// Método para a impressão da lista
void imprime_lista(node *head) {
	node *tmp = head;
	// Percorre toda a lista, imprimindo os valores
	while(tmp->next != NULL){
		printf(" %d -", tmp->val);
		tmp = tmp->next;
	};
	// Imprime o último valor, que não é impresso por causa do tmp->next == NULL
	printf(" %d\n", tmp->val);
}

// Método main - Principal
int main() {
	
	// Ponteiro principal e ponteiro que aponta para este ponteiro
	node *head = malloc(sizeof(node));
	node **lista = &head;
	insere_head(lista);

	while(1) {
		// Método de impressão de lista
		imprime_lista(head);
		int value;
		printf("Digite o valor a ser inserido: \n");
		scanf("%d", &value);
		// Node a ser inserido
		node *aloc = malloc(sizeof(node));
		aloc->val = value;
		// Método de inserção de node
		insere_node(lista, aloc);
	}

	return 0;
}
