import java.util.Scanner;

public class Ex02 {
    public static void main(String[] args){
        int nro_estudantes, soma, nota, notasLidas;
        double media;
        Scanner scanner = new Scanner(System.in);
        System.out.print("Numero de estudantes da turma: ");
        nro_estudantes = scanner.nextInt();
        soma = 0;

        notasLidas = 0;

        while(notasLidas < nro_estudantes){
            System.out.printf("Nota %d: ", notasLidas+1);
            nota = scanner.nextInt();
            soma = nota + soma;
            notasLidas = notasLidas + 1;

        }
        scanner.close();
        media = (double) soma/ nro_estudantes;
        System.out.printf("Media das notas = %.1f\n", media);
        
    }
}
