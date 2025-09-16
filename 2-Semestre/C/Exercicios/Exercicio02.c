#include <stdio.h>
int main(){
int i;
int numeros[3];
for(i = 0; i < 3; i++){
printf("Digite o %d numero:\n", i+1);
scanf("%d", &numeros[i]);
}
if (numeros[0] > numeros[1] && numeros[0] > numeros[2])
printf("O Primeiro numero eh o maior - > %d",numeros[0]);
else if (numeros[1] > numeros[0] && numeros[1] > numeros[2] )
printf("O Segundo numero eh o maior - > %d",numeros[1]);
else if (numeros[2] > numeros[0] && numeros[2] > numeros[1] )
printf("O Terceiro numero eh o maior - > %d",numeros[2]);
else
printf("Ha um empate entre os maiores numeros!!");

}
