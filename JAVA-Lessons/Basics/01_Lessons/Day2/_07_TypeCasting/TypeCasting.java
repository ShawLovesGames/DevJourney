public class TypeCasting {
    public static void main(String[] args) {

        // Type Casting is used to assign a value of one primitive data type to another type. 
        // There are two types :-

        // Widening casting (implicit) - converting a smaller type to a larger size type.
        int intValue = 100;
        long longValue = intValue; // int to long conversion.
        float floatValue = longValue; // long to float conversion.
        double doubleValue = floatValue; // float to double conversion.
        System.out.println("Widening Casting:");
        System.out.println("int to long: " + longValue);
        System.out.println("long to float: " + floatValue);
        System.out.println("float to double: " + doubleValue);

        // Narrowing casting (explicit) - converting a larger type to a smaller size type.
        double anotherDouble = 123.45;
        float anotherFloat = (float) anotherDouble; // double to float conversion using (float).
        long anotherLong = (long) anotherFloat; // float to long conversion using (long).
        int anotherInt = (int) anotherLong; // long to int conversion using (int).

        System.out.println("\nNarrowing Casting:");
        System.out.println("double to float: " + anotherFloat);
        System.out.println("float to long: " + anotherLong);
        System.out.println("long to int: " + anotherInt);

    }
}
