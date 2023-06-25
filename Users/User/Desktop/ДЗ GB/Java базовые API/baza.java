// Реализовать простой калькулятор

import java.util.Scanner;

public class baza {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.print("Введите 1е и 2е число -");
            int a = sc.nextInt();
            int b = sc.nextInt();
            System.out.print("Выберите и введите тип операции которую необходимо выполнить (+, -, *, /, %)- ");
            char op = sc.next().charAt(0);
            solve(a, b, op);
        }
    }

    public static int solve(int a, int b, char op) {
        int ans = 0;
        if (op == '+') {
            ans = a + b;
        } else if (op == '-') {
            ans = a - b;
        } else if (op == '*') {
            ans = a * b;
        } else if (op == '%') {
            ans = a % b;
        } else if (op == '/') {
            ans = a / b;
        }
        System.out.println("Получается: - " + ans);
        return ans;
    }
}
