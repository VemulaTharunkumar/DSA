import java.util.*;
public class Alphanumeric{
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        String s=sc.next();
        String y=longest(s,s.length());
        System.out.print("Max:"+y);
    }
    /*public static int Asum(String s,int n){
        int sum=0;
        int num=0;
        for(int i=0;i<n;i++){
            char ch=s.charAt(i);
            if(Character.isDigit(ch)){
                num=num*10+(ch-'0');
            }
            else{
                sum+=num;
                num=0;
            }
        }
        return sum+num;
    }*/
   public static String longest(String s,int n){
        int num=0;
        int len=0;
        StringBuilder p=new StringBuilder();
        for(int i=0;i<n;i++){
            char ch=s.charAt(i);
            if(Character.isDigit(ch)){
                num=num*10+(ch-'0');
                p.append(String.valueOf(num));
            }
            else{
                num=0;
            }
        }
        String r="";
        for(int i=0;i<p.length();i++){
            if(p.i.length()>r.length()){

            }
        }
   }
}