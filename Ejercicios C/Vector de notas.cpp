#include <stdio.h>

int main()
{
	int sum_notas, i, notas[10];
	int nota_max = 0 ;
	float promedio;
	
	for(i = 0; i < 10; i++)
	{
		printf("Ingrese numero : ");
		scanf("%i", &notas[i]);
		sum_notas += notas[i];
		if (nota_max < notas[i])
		{
			nota_max = notas[i];
		}
	}
	
	promedio = float(sum_notas / 10);
	printf("La nota mas alta es %i \n", nota_max);
	printf("El promedio es %f", promedio);

}
