//1) Вычислить n-ое треугольного число (сумма чисел от 1 до n), n! (произведение чисел от 1 до n)
import java.util.Scanner;
public class baza {
    public static void main(String[] args) {
        try (Scanner console = new Scanner(System.in)) {
            System.out.print("Введите число: ");
            int f = console.nextInt();
            int factorial = f;
            for (int i = (f - 1); i > 1; i--) {
                factorial *= i;
            }
            System.out.printf("Факториал введенного числа = " + factorial);
        }
    }
}
    