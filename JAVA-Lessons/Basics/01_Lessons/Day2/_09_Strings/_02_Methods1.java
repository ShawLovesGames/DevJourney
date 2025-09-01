// ---Important Methods---

public class _02_Methods1 {
    public static void main(String[] args) {

        // ---String Methods---
        // Note :- As strings are immutaable, these methods do not change the existing string but they return a brand new String object.
        
        // Most important string methods (to remember) :-
        String friend = "Friend";

        // length - Shows the length of the String.
        System.out.println(friend.length());

        // Concatenate - "Joins" two or more strings.
        System.out.println("--" + friend + "--");

        // charAt - Returns the character at given index.
        System.out.println(friend.charAt(0));

        // substring - Returns a substring from a string from and to desired indexes.
        System.out.println(friend.substring(0, 3));

        // replace - Replaces all occurrences of the given character with desired character.
        System.out.println(friend.replace('F', 'T'));

        // equals - Compares two strings and returns true if they are equal.
        System.out.println(friend.equals("Friend"));

        // equalsIgnoreCase - Compares two strings for equality, ignoring case.
        System.out.println(friend.equalsIgnoreCase("fRIEND"));

        // indexOf - Returns the index of the first occurrence of a character in the string.
        System.out.println(friend.indexOf('r'));

        // lastIndexOf - Returns the index of the last occurence of a character in the string.
        System.out.println("Friendr".lastIndexOf('r'));
        
        // contains - Checks if the string contains a given substring or sequence of characters.
        System.out.println(friend.contains("end"));

    }
}
