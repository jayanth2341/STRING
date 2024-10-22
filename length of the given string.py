"""
Write a program to print th length of the given string.
Sample Input:
Hello
Sample Output:
Hello: 5
"""
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String inputString = scanner.nextLine();
        int length = inputString.length();
        System.out.println(inputString + ": " + length);
        scanner.close();
    }
}
