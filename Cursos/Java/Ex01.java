public class Ex01 {
// Faça um programa que leia dois valores numéricos inteiros e apresente
// o resultado da diferença do maior valor pelo menor valor. Se os valores
// forem iguais, o programa deve mostrar zero.
public static void main(String[] args) {
    int n1, n2, maior,menor, res;
    System.out.print("Digite dois números inteiros:\n");
    n1 = Integer.parseInt(System.console().readLine());
    n2 = Integer.parseInt(System.console().readLine());
    maior = Math.max(n1, n2);
    menor = Math.min(n1, n2);
    res = maior - menor;
    if (n1 != n2)
         System.out.printf("Resultado: %d", res);
    if (n1 == n2)
         System.out.print("0");
} 

}
