import java.util.*;
public class Transform{
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int[] a=new int[n];
        int[] b=new int[n];
        for(int i=0;i<n;i++){
            a[i]=sc.nextInt();
        }
        for(int j=0;j<n;j++){
            b[j]=sc.nextInt();
        }
        int y=transform(a,b,n);
        System.out.print("Min Operations:"+y);
    }
    public static int transform(int[] a,int[] b,int n){
        Arrays.sort(a);
        Arrays.sort(b);
        int res=0;
        for(int i=0;i<n;i++){
            res+=Math.abs(a[i]-b[i]);
        }
        return res;
    }
}