// ---Final Variable---

public class _02_Final {
    public static void main(String[] args) {

        final int NUMBER = 5;
        System.out.println(NUMBER);
        
        /*
            We use final keyword before declaring a variable to make it unchangeable and read-only.
            If we tried to change the value inside the variable num2, it would throw an error. Example :-
            num2 = 20;  // will generate the error: cannot assign a value to a final variable
            NOTE :-  By convention, final variables in Java are usually written in upper case (e.g. BIRTHYEAR). 
                     It is not required, but useful for code readability and common for many programmers.
         */

    }
}