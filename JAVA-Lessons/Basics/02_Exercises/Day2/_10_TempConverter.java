// ---Store a Celsius temperature and convert it to Fahrenheit---

public class _10_TempConverter {
    public static void main(String[] args) {
        
        double c = 37.2;
        double F;

        F = (c * 9/5) + 32;

        System.out.println("The temperature in fahreinheit is: " + (int)F + "° f");

    }
}