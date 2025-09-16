#include <stdio.h>
int fatorial(int num){
if (num == 1 || num == 0)
return 1;
int resultado = num;
for (int i = 2; i < num; i++)
{
   resultado *= i;
}
return resultado;
}

int main()
{
int num;
printf("Digite um numero:\n");
scanf("%d",&num);
printf("Fatorial: %d", fatorial(num));

}



