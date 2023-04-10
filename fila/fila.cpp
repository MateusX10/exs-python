// Autor: Mateus Henrique de Souza Medeiros

#include <stdio.h>
#include <stdlib.h>
#define MAX 5



// Struct de dados da fila
typedef struct{
	int elementos[MAX];
	int inicio=0;
	int fim=0;
}lista;


// Menu de op��es
void menu(){
	printf("\n\n>>> Menu:\n\n1 - Inserir valor na fila\n2 - Retirar valor da fila \n3 - Listar fila \n4 - Sair do Programa");
	
}


// Verifica se a fila est� vazia
bool FilaEstaVazia(lista &f){
	if (f.fim == 0){
		return true;	
	}
	else {
		return false;
	}
		
}


// Verifica se a fila est� cheia
bool FilaEstaCheia(lista &f){
	if (f.fim - f.inicio == 5){
		return true;
	}
	
	else {
		return false;
	}
}



// Insere valor na fila
int InserirValorNaFila(lista &f){
	if (FilaEstaCheia(f)){
		printf("\nOps, fila cheia!");
		
	}
	
	else {
		int valor = 0;
		printf("\n\nInforme um valor para adicionar a fila: ");
		scanf("%d", &valor);
		f.elementos[f.fim++] = valor;
		printf("\nValor %d adicionado a fila com sucesso!\n\n", valor);
		system("pause");
}
}



//Lista valores da fila
int ListarValoresDaFila(lista &f){
	int cont=0;
	
	if (FilaEstaVazia(f)){
		printf("\n\nOps, fila vazia!\n");
	}
	
	else{
		// Caracteres com o intuito de melhorar a est�tica do programa
		printf("\n\n\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=");
		printf("\nValores da fila --> ");
		printf("[");

		for (cont; cont < f.fim; cont++){
			if (cont == (f.fim - 1)){
				printf("%d", f.elementos[cont]);
			
			}
		
			
			else {
				printf("%d    ", f.elementos[cont]);
			}
			
	}
	// Caracteres com o intuito de melhorar a est�tica do programa
	printf("]");
	printf("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=");
		
	}
	
	
}





// Retira valor da fila
int RetirarValorDaFila(lista &f){
	if (FilaEstaVazia(f)){
		printf("\n\nOps, fila vazia!\n");
	}
	
	else{
		printf("...");
		printf("\n\nItem %d removido da fila com sucesso! ", f.elementos[f.inicio]);
		for (int i=f.inicio; i < f.fim; i++){
			if (i < (f.fim - 1)){
			
			// Supondo que a fila esteja cheia (com 5 elementos), a l�gica da remo��o do elemento funciona da seguinte forma:
			
			// O primeiro elemento da fila passa a ser o segundo,  o segundo passa a ser o terceiro, o quarto passa a ser o quinto e o quinto elemento 
			// passa a n�o existir mais.Como n�o h� nenhum elemento antes do primeiro elemento que possa "receber" o seu valor, ent�o o primeiro elemento
			// simplesmente deixa de existir
			f.elementos[i] = f.elementos[i+1];
		}
			
		}
		// O quinto elemento j� n
		f.fim--;
		
	}
}




// Fun��o principal
int main(){
	lista fila;
	int EscolhaUsuario=0;
	
	
	
	
	// Loop infinito e menu de escolhas do usu�rio
	while (1){
		
		
		// Menu e input de dados do usu�rio
		menu();
		printf("\n\nFaca sua escolha: ");
		scanf("%d", &EscolhaUsuario);
		
		// Usu�rio optou por inserir valores na fila
		if (EscolhaUsuario == 1){
			printf("\n<<< INSERIR VALOR NA FILA >>>");
			InserirValorNaFila(fila);
		}
		
		// Usu�rio optou por retirar valores da fila
		else if (EscolhaUsuario == 2){
			printf("\n<<< RETIRAR VALOR DA FILA >>>");
			RetirarValorDaFila(fila);
		}
		
		// Usu�rio optou por listar valores da fila
		else if (EscolhaUsuario == 3){
			printf("\n<<< LISTAR VALORES DA FILA >>>");
			ListarValoresDaFila(fila);
		}
		
		// Usu�rio optou por sair do programa
		else if (EscolhaUsuario == 4){
			printf("\n<<< Sair do Programa >>>");
			break;
		}
		
		
		// Usu�rio selecionou uma op��o inv�lida
		else {
			printf("\nOps, op��o inv�lida!");
			printf("\nPor favor, tente novamente :)");
			
		}
		
	}
	
	
	return 0;
}




