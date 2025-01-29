class Main {
    public static void main(String[] args) {
        System.out.println(10 + 2 * 3 - 2);
    }
}

class Calculator {
    int result;
    int[] numbers;

    public int init(int size) {
        numbers = new int[size];
        result = 0;
        return 0;
    }

    public int add(int a, int b) {
        int temp;
        temp = a + b;
        return temp;
    }

    public int power(int base, int exp) {
        return base ** exp;
    }

    public boolean isPositive(int num) {
        return !(num < 0);
    }
}

class MathUtil extends Calculator {
    public int multiply(int x, int y) {
        int result;
        if (x < y) {
            result = x * y;
        } else {
            result = y * x;
        }
        return result;
    }

    public int sumArray() {
        int i;
        int sum;
        i = 0;
        sum = 0;
        while (i < numbers.length) {
            sum = sum + numbers[i];
            i = i + 1;
        }
        return sum;
    }
}