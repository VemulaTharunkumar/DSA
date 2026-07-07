import java.util.*;
public class Pattern{
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        String s=sc.next();
        String p=sc.next();
        int freq[]=new int[26];
        int freq1[]=new int[26];
        int n=p.length();
        for(int i=0;i<n;i++){
            char ch=p.charAt(i);
            freq[ch-'a']++;
        }int y=0;
        for(int i=0;i<n;i++){
            char ch=s.charAt(i);
            freq1[ch-'a']++;

        }
        int u=0;
        for(int j=n;j<s.length();j++){
            if(freq.equals(freq1)){
                System.out.println("Pattern matches");
                break;
            }
            else{
                freq1[s.charAt(u)-'a']--;
                u++;
                freq1[s.charAt(j)-'a']++;
            }
        }
        if(!freq.equals(freq1)){
                System.out.println("Pattern not matches");
            }        

    }
}