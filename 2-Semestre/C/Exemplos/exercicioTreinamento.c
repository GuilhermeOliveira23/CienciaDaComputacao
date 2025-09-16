#include <stdio.h>
int main(){
    
int qntRotulos;
float valorUnitario;
float valorTotal;
char rep;
int cont = 0;
while(cont==0){
printf("Qual eh o preco do rotulo?\n");
scanf("%f",&valorUnitario);
printf("Quantos rotulos voce quer comprar?\n");
scanf("%d",&qntRotulos);

valorTotal = valorUnitario * qntRotulos;
if(qntRotulos >= 100)
valorTotal *= 0.75;

printf("Olha o valor total: %.2f\n",valorTotal);
printf("Deseja continuar?(s/n)\n");
scanf(" %c",&rep);
if(rep == 'n')
cont++;
}
return 0;
}