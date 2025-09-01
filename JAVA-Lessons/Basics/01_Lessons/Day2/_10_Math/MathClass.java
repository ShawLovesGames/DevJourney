// ---Math Class---

public class MathClass {
    public static void main(String[] args) {
        
        // JAVA math class has many methods that perform mathematical tasks.

        // Most important math methods (to remember) :-
        double a = 4.6, b = 6.1;
        int x = -5, y = 4, z = 2, i = 27;

        // Math.max(a, b) - Returns the larger of two numbers.
        System.out.println(Math.max(a, b));

        // Math.min(a, b) -  Returns the smaller of the two numbers.
        System.out.println(Math.min(a, b));

        // Math.abs(x) - Return the absolute value (no negative sign).
        System.out.println(Math.abs(x));

        // Math.sqrt(y) - Returns the square root of the number.
        System.out.println(Math.sqrt(y));

        // Math.cbrt(i) - Returns the cube root of the given number.
        System.out.println(Math.cbrt(i));

        // Math.pow(y, z) -  Returns power.
        System.out.println(Math.pow(y, z));

        // Math.round(a) - Rounds to the nearest integer.
        System.out.println(Math.round(a));

        // Math.floor(a) - Returns the largest integer <= number.
        System.out.println(Math.floor(a));

        // Math.ceil(b) - Returns the smallest integer >= number.
        System.out.println(Math.ceil(b));

        // Math.random() - Returns random double between 0.0 and 1.0
        System.out.println(Math.random());

    }
}
