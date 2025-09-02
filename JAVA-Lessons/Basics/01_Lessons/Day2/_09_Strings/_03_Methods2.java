// ---More methods---

public class _03_Methods2 {
    public static void main(String[] args) {

        // Common & Useful string methods :-
        String friend = "Friend";

        // isEmpty - Returns true if length of the string is 0.
        System.out.println("".isEmpty());

        // startsWith - Checks if the string starts with the given substring.
        System.out.println(friend.startsWith("Fr"));

        // endsWith - Checks if the string ends with the given substring.
        System.out.println(friend.endsWith("nd"));

        // toUpperCase - changes all of the letters in the string to upper case.
        System.out.println(friend.toUpperCase());

        // toLowerCase - changes all of the letters in the string to lower case.
        System.out.println(friend.toLowerCase());

        // trim - Removes whitespaces from the start and end of a string.
        System.out.println(" trimmed ".trim());

        // split - Splits the string into arrays based on a given substring.
        String myNames = "Akshat,Sahil,Vasudev";
        String[] arr = myNames.split(","); // IDK how to print the elements of an array yet.
        for (int i = 0; i < 3; i++) { // Used AI for now.
            System.out.println(arr[i]);
        }
        
    }
}
