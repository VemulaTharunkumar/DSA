import java.util.*;
public class maxProduct{
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int[] a=new int[n];
        for(int i=0;i<n;i++){
            a[i]=sc.nextInt();
        }
        Arrays.sort(a);
        int max=1,max1=1;
        max=a[n-1]*a[n-2]*a[n-3];
        max1=a[0]*a[1]*a[n-1];
        System.out.print("Max Product :"+Math.max(max,max1));
    }    
}