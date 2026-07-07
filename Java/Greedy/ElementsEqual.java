import java.util.Arrays;
import java.util.Scanner;
public class ElementsEqual {
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int[] a=new int[n];
        for(int i=0;i<n;i++){
            a[i]=sc.nextInt();
        }
        int u=Equal(a,n);
        System.out.println("Min :"+u);
    }
    public static int Equal(int[] a,int n){
        Arrays.sort(a);
        int[] b=new int[n];
        for(int i=0;i<n;i++){
            b[i]=a[n/2];
        }
        int res=0;
        for(int j=0;j<n;j++){
            res+=Math.abs(b[j]-a[j]);
        }
        return res;
    }
}
