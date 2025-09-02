// ---Print a random integer between 1 and 10---

public class _09_RandomNumber {
    public static void main(String[] args) {
        
        int randomNum = (int)(Math.random() * 10) + 1;

        System.out.println(randomNum);
    }
}