import java.util.Scanner;

class TrieNode {
    TrieNode child[];
    int c;
    int endCount;
    boolean isleaf;

    TrieNode() {
        child = new TrieNode[26];
        isleaf = false;
        c = 0;
        endCount = 0;
    }
}

public class Trie_Operations_Menu {
    TrieNode root;

    Trie_Operations_Menu() {
        root = new TrieNode();
    }

    void insert(String key) {
        TrieNode curr = root;
        for (char ch : key.toCharArray()) {
            if (curr.child[ch - 'a'] == null) {
                curr.child[ch - 'a'] = new TrieNode();
            }
            curr.child[ch - 'a'].c++;
            curr = curr.child[ch - 'a'];
        }
        curr.isleaf = true;
        curr.endCount++;
    }

    boolean Search(String key) {
        TrieNode curr = root;
        for (char ch : key.toCharArray()) {
            if (curr.child[ch - 'a'] == null) {
                return false;
            }
            curr = curr.child[ch - 'a'];
        }
        return curr.isleaf;
    }

    boolean PrefixSearch(String key) {
        TrieNode curr = root;
        for (char ch : key.toCharArray()) {
            if (curr.child[ch - 'a'] == null) {
                return false;
            }
            curr = curr.child[ch - 'a'];
        }
        return true;
    }

    int PrefixCount(String key) {
        TrieNode curr = root;
        for (char ch : key.toCharArray()) {
            if (curr.child[ch - 'a'] == null) {
                return 0;
            }
            curr = curr.child[ch - 'a'];
        }
        return curr.c;
    }

    int StringCount(String key) {
        TrieNode curr = root;
        for (char ch : key.toCharArray()) {
            if (curr.child[ch - 'a'] == null) {
                return 0;
            }
            curr = curr.child[ch - 'a'];
        }
        return curr.endCount;
    }

    public static void main(String[] args) {
        Trie_Operations_Menu trie = new Trie_Operations_Menu();
        Scanner scanner = new Scanner(System.in);
        int choice;

        System.out.println("=== Trie Data Structure Operations ===");
        do {
            System.out.println("\n1. Insert Word");
            System.out.println("2. Search Exact Word");
            System.out.println("3. Prefix Search");
            System.out.println("4. Prefix Count");
            System.out.println("5. Exact String Count (Endpoint)");
            System.out.println("6. Exit");
            System.out.print("Enter your choice (1-6): ");

            while (!scanner.hasNextInt()) {
                System.out.print("Invalid input. Enter a number (1-6): ");
                scanner.next();
            }
            choice = scanner.nextInt();
            scanner.nextLine();

            switch (choice) {
                case 1:
                    System.out.print("Enter word to insert: ");
                    String wordToInsert = scanner.nextLine().toLowerCase().trim();
                    if (wordToInsert.matches("[a-z]+")) {
                        trie.insert(wordToInsert);
                        System.out.println("\"" + wordToInsert + "\" inserted successfully.");
                    } else {
                        System.out.println("Error: Only lowercase alphabetic characters allowed.");
                    }
                    break;

                case 2:
                    System.out.print("Enter word to search: ");
                    String wordToSearch = scanner.nextLine().toLowerCase().trim();
                    if (trie.Search(wordToSearch)) {
                        System.out.println("Found: \"" + wordToSearch + "\" exists in the Trie.");
                    } else {
                        System.out.println("Not Found: \"" + wordToSearch + "\" does not exist.");
                    }
                    break;

                case 3:
                    System.out.print("Enter prefix to search: ");
                    String prefixToSearch = scanner.nextLine().toLowerCase().trim();
                    if (trie.PrefixSearch(prefixToSearch)) {
                        System.out.println("Success: Words matching prefix \"" + prefixToSearch + "\" exist.");
                    } else {
                        System.out.println("Failed: No words match the prefix \"" + prefixToSearch + "\".");
                    }
                    break;

                case 4:
                    System.out.print("Enter prefix to count: ");
                    String prefixToCount = scanner.nextLine().toLowerCase().trim();
                    System.out.println("Count of words with prefix \"" + prefixToCount + "\": " + trie.PrefixCount(prefixToCount));
                    break;

                case 5:
                    System.out.print("Enter exact word to count: ");
                    String stringToCount = scanner.nextLine().toLowerCase().trim();
                    System.out.println("Exact occurrences of \"" + stringToCount + "\": " + trie.StringCount(stringToCount));
                    break;

                case 6:
                    System.out.println("Exiting application. Goodbye!");
                    break;

                default:
                    System.out.println("Invalid option! Please select a choice between 1 and 6.");
            }
        } while (choice != 6);

        scanner.close();
    }
}