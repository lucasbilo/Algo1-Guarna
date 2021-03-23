#include <stdio.h>

int main(){
	
	int cantidad, desc = 0, asc = 0;
	printf("Cantidad de numeros que va a ingresar: ");
	scanf("%i", &cantidad);
	int numero, numeros[cantidad], num_anterior = 0, i;
	for (i = 0; i <= cantidad; i++){
		printf("Ingrese un numero: ");
		scanf("%i", &numero);
		numeros[i] = numero;
		if (num_anterior < numeros[i])
			asc ++;
		else
			desc ++;
		num_anterior = numeros[i];
	}
	switch(cantidad){
		case 1:
			if (cantidad == asc)
				printf("asc");
				break;
		case 2:
			if (cantidad == desc)
				printf("desc");
				break;
		case 3:
			printf("desor");
			break;
	}
}
