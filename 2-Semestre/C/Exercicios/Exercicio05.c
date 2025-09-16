#include <stdio.h>
int main()
{
int numeros[3];
int tamanho = sizeof(numeros)/ sizeof(numeros[0]);

for(int i = 0; i < tamanho; i++){
printf("Digite o %d numero:\n", i+1);
scanf("%d", &numeros[i]);
}
int maior = numeros[0];

for(int i = 1; i < tamanho; i++){
    if(numeros[i] > maior)
     maior = numeros[i];
}

int soma = 0;
for (int i = 0; i < tamanho; i++)
{
   soma += numeros[i];
}

float media = (float)soma/ tamanho;

printf("O maior numero eh: %d\n",maior);
printf("A soma total eh: %d\n", soma);
printf("A media eh: %.2f\n", media);
}
