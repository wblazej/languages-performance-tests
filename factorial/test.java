class Main {
    public static long factorial(int n) {
        if (n <= 2)
            return n;
            
        return n * factorial(n - 1);
    }

    public static void test() {
        for (int j = 0; j < 10000; j++)
            for (int i = 1; i <= 20; i++)
                factorial(i);
    }

    public static void main(String[] args) {
        long startTime = System.currentTimeMillis();

        test();

        System.out.println(System.currentTimeMillis() - startTime);
    }
}