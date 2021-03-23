#include <stdio.h>

int calcular_factorial(int numero){
	if (numero > 0)
		return numero * calcular_factorial(numero-1);
	else
		return 1;
}

int main(){
	
	int numero, factorial;
	printf("Ingrese numero para calcular su factorial: ");
	scanf("%i", &numero);
	factorial = calcular_factorial(numero);
	printf("El factorial del numero %i es %i", numero, factorial);
}
