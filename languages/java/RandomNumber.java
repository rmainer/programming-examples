class RandomNumbers {
    public static void main(String [] args) {
        // random number between 0 and (almost) 1
        double randomNumber = Math.random();

        // change range to 0 to (almost) 10
        randomNumber = randomNumber * 10;

        // cast to integer, ex. 6.998 becomes 6
        int randomInt = (int) randomNumber;

        // range 1 to 6
        randomNumber = Math.random();
        randomNumber = randomNumber * 6;
        randomNumber = randomNumber + 1;
        randomInt = (int) randomNumber;

        // output
        System.out.println(randomInt);
    }
}