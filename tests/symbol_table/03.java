class Main {
    public static void main(String[] args) {
        System.out.println(new Calculator().init());
    }
}

class Calculator {
    int result;
    int[] numbers;

    public int init() {
        numbers = new int[4];
        numbers[0] = 4;
        numbers[1] = 6;
        numbers[2] = 10;
        numbers[3] = 12;
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