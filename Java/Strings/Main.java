import java.util.Scanner;

public class Main {

    static final int NO_OF_CHARS = 256;

    static void badCharHeuristic(String pattern, int m, int[] badChar) {
        for (int i = 0; i < NO_OF_CHARS; i++)
            badChar[i] = -1;
        for (int i = 0; i < m; i++)
            badChar[pattern.charAt(i)] = i;
    }
    static void search(String text, String pattern) {
        int m = pattern.length();
        int n = text.length();
        int[] badChar = new int[NO_OF_CHARS];
        badCharHeuristic(pattern, m, badChar);
        int shift = 0;
        while (shift <= (n - m)) {
            int j = m - 1;
            while (j >= 0 && pattern.charAt(j) == text.charAt(shift + j))
                j--;
            if (j < 0) {
                System.out.println("Pattern found at index " + shift);

                if (shift + m < n)
                    shift += m - badChar[text.charAt(shift + m)];
                else
                    shift += 1;
            }
            else {
                shift += Math.max(1,
                        j - badChar[text.charAt(shift + j)]);
            }
        }
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter Text: ");
        String text = sc.nextLine();

        System.out.print("Enter Pattern: ");
        String pattern = sc.nextLine();

        search(text, pattern);

        sc.close();
    }
}