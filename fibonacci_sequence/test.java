class Main {
    public static long fibonacci_sequence(int n) {
        if (n <= 2)
            return n;
            
        return fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2);
    }

    public static void test() {
        fibonacci_sequence(30);
    }

    public static void main(String[] args) {
        long startTime = System.currentTimeMillis();

        test();

        System.out.println(System.currentTimeMillis() - startTime);
    }
}