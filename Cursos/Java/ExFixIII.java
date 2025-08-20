
import java.util.Scanner;

// Faça um programa que receba cinco números e mostre a saída a seguir:
// Digite o 1º número: 5
// Digite o 2º número: 3
// Digite o 3º número: 2
// Digite o 4º número: 0
// Digite o 5º número: 2
// Os números digitados foram:
// 5 + 3 + 2 + 0 + 2 = 12



public class ExFixIII {
    public static void main (String args[]){
    Scanner scanner = new Scanner (System.in);
    int[] vetor = new int[5];
    int soma = 0;
    for (int i = 0; i < 5; i++) {
        System.out.printf("\nDigite o %dº número: ",i + 1);
        vetor[i] = scanner.nextInt();
        soma += vetor[i];

    }
    System.out.printf("A soma dos números é: %d",soma);



    }
}
