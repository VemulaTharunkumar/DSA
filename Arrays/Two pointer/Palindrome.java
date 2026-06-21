/*import java.util.*;
public class Palindrome {
    public static void main(String args[]){
    Scanner sc=new Scanner(System.in);
    String s=sc.next();
    int i=0;
    int j=s.length()-1;
    while(i<j){
        if(s.charAt(i)!=s.charAt(j)){
            System.out.print("Not a palindrome");
            System.exit(0);
        };
        i++;
        j--;
    }
    System.out.print("Palindrome");
}
}*/
//Reverse the given string using 2 pointers
import java.util.*;
public class Palindrome {
    public static void main(String args[]){
    Scanner sc=new Scanner(System.in);
    String s=sc.next();
    char[] r=s.toCharArray();
    int i=0;
    int j=r.length-1;
    while(i<j){
        char t=r[i];
        r[i]=r[j];
        r[j]=t;
        i++;
        j--;
    }
    System.out.print(r);
    }
}