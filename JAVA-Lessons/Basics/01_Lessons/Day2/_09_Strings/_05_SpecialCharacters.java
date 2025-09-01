// ---Special Characters---

public class _05_SpecialCharacters {
    public static void main(String[] args) {
        /*
            JAVA can sometimes misunderstand a string and throw an error.

            String name = "Akshat "The Dev" Shaw"; This will throw an error.

            We use backslash escape character for avoiding this problem :-
                \'	    '	    Single quote
                \"	    "	    Double quote
                \\	    \	    Backslash
        */

        String name = "Akshat \"The Dev\" Shaw";
        System.out.println(name);

        /*
            Other common escape characters :-
                \n	    New Line	
                \r	    Carriage Return	
                \t	    Tab	
                \b	    Backspace	
                \f	    Form Feed
         */
    }
}
