import java.util.*;
public class ksum{
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int[] a=new int[n];
        for(int i=0;i<n;i++){
            a[i]=sc.nextInt();
        }
        int k=sc.nextInt();
        int[] o=sum(a,n,k);
        for(int l:o){
            System.out.print(l+" ");
        }
    }
    static int[] sum(int[] a,int n,int k){
        int i=0;
        int[] b=new int[n-k+1];
        int sum=0;
        for(int j=0;j<k;j++){
            sum+=a[j];
        }
        b[i]=sum;
        i++;
        for(int h=k;h<n;h++){
            sum-=a[h-k];
            sum+=a[h];
            b[i]=sum;
            i++;
        }
        return b;
    }
}