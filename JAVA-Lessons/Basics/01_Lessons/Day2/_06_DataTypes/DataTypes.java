// ---Data Types in JAVA---

public class DataTypes {
    public static void main(String[] args) {

        /*
        Types of variables (Data types) are:-
        Primitive data types (of fixed length) and Non-primitive / Reference date types (of variable length).
        */
        
        // Primitive data types are simple. They always hold a value.
        char name = 'A'; // Stores a single character such as 'a' or 'B'.
        byte age = 20; // Stores whole numbers from -128 to 127.
        short salary = 30000; // Stores whole numbers from -32,768 to 32,767.
        int phone1 = 555555555; // Stores whole numbers from -2,147,483,648 to 2,147,483,647.
        long phone2 = 555555555555555L; // Stores whole numbers from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807.
        float pi = 3.14F; // Stores fractional numbers. Sufficient for storing 6 to 7 decimal digits.
        double pi2 = 3.14159265358979323846; // Stores fractional numbers accurately till 15-16th digit.
        boolean isAdult = true; // Stores true or false values.

        System.out.println(name + " " + age + " " + salary + " " + phone1 + " " + isAdult + " " + phone2 + " " + pi + " " + pi2);

        // Non-primitive or reference data types are complex. Non-primitive types can be null.
        //1. Class - the most fundamental type. Includes predefined and user-defined classes.
            String greeting = "Hello World!"; // Most commonly used class is the string.
            // Also includes Wrapper classes and Custom classes.
        //2. Interfaces - contains only constants, method signatures, default methods, static methods, and nested types.
        //3. Arrays - Arrays in Java are objects that hold a fixed number of values of a single type.
        //4. Enums - A special kind of class used to define a collection of predefined, named constants.
        //5. Annotations - A form of metadata that provides data about a program that is not part of the program itself.

        System.out.println(greeting);
        // As reference data types are complex. I will study them in full detail later on.

    }
}