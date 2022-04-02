class Main {
    public static void test() {
        int n = 1000000;
        int[] randomNumbers = new int[n];
        
        for (int i = 0; i < randomNumbers.length; i++)
            randomNumbers[i] = (int) (Math.random() * n) + 1;
    }

    public static void main(String[] args) {
        long startTime = System.currentTimeMillis();

        test();

        System.out.println(System.currentTimeMillis() - startTime);
    }
}