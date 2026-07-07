import java.util.*;
public class LongestSubstring {
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        String s=sc.next();
        int freq[]=new int[27];
        int n=s.length();
        for(int i=0;i<n;i++){
            char ch=s.charAt(i);
            freq[(ch-'a')+1]++;
        }
        int l=0;
        for(int i=0;i<n;i++){
            char ch=s.charAt(i);
            if(freq[(ch-'a')+1]<=(ch-'a')+1){
                l+=freq[(ch-'a')+1];
            }
            else{
                freq[(ch-'a')+1]--;
            }
        }
        System.out.println("Length :"+l);
    }
}
