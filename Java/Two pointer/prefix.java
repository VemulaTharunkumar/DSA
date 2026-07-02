import java.util.*;
public class prefix {
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        String[] s=new String[n];
        for(int i=0;i<n;i++){
            s[i]=sc.next();
        }
        Arrays.sort(s);
        String s1=s[0];
        String s2=s[n-1];
        int j=0;
        StringBuilder sb=new StringBuilder();
        while(j<s1.length()){
            if(s1.charAt(j)==s2.charAt(j)){
                sb.append(s1.charAt(j));
                j++;
            }
            else{
                break;
            }
        }
        System.out.print(sb.toString());
    }
}
