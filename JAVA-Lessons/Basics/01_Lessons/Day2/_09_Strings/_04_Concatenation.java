// ---Concatenation of Strings---

public class _04_Concatenation {
    public static void main(String[] args) {
        
        // We can use the '+' operator for combine strings.
        String first_name = "Akshat";
        String last_name = "Shaw";
        System.out.println(first_name + " " + last_name);

        // concat() method can also be used to concatenate two strings.
        first_name = "Akshat ";
        last_name = "Shaw";
        System.out.println(first_name.concat(last_name));

    }
}
