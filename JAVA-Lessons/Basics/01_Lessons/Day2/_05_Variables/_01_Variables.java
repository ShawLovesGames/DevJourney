// ---Variables in JAVA---

public class _01_Variables {
    public static void main(String[] args) {
        
        // To initialize a variable.
        char letter = 'A'; // Char stores a single character.
        int num = 20; // int stores integers.

        // To print the values of variables.
        System.out.println(letter);
        System.out.println(num);

        // To store some text.
        String name = "Akshat Shaw"; // String is a complex data type, I will study strings in more detail in coming lessons.
        System.out.println(name);

        // We can declare variables without assigning the value, then we can assign the value later.
        int age;
        age = 20;
        System.out.println(age);

        // We can overwrite the value of any existing variable.
        num = 15;
        System.out.println(num);

        // We can declare multiple variables of the same type in one line.
        int x = 5, y = 10, z = 15;
        System.out.println(x);
        System.out.println(y);
        System.out.println(z);

        // We can assign same value to multiple variables in one line.
        x = y = z = 20;
        System.out.println(x);
        System.out.println(y);
        System.out.println(z);

        /* 
            Every variable must have a unique name. This unique name is called an identifier.
            Rules for naming variables :-
            1.  Names can contain letters, digits, underscores, and dollar signs.
            2.  Names must begin with a letter.
            3.  Names should start with a lowercase letter, and cannot contain whitespace.
            4.  Names can also begin with $ and _.
            5.  Names are case-sensitive ("myVar" and "myvar" are different variables).
            6.  Reserved words (like Java keywords, such as int or boolean) cannot be used as names.
        */

    }
}