// Вывести все простые числа от 1 до 1000
public class baza {
    public static void main(String[] args) {
        for (int i = 2; i <= 1000; i++) { // Простым числом называют такое натуральное число,
            if (i % 1 == 0 || i % i == 0) { // которое > 1 и делится только на 1 и само на себя
                System.out.print(i + ", ");
            }
        }
    }
}
