import java.util.Scanner;
import java.util.ArrayList;
public class maxinsubarray {
        public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int[] a=new int[n];
        for(int i=0;i<n;i++){
            a[i]=sc.nextInt();
        }
        int k=sc.nextInt();
        int[] o=max(a,n,k);
        for(int l:o){
            System.out.print(l+" ");
        }
    }
    static int[] max(int[] a,int n,int k){
        ArrayList<Integer>al=new ArrayList<>();
        int[] j=new int[n-k+1];
        int max=0;
        for(int i=0;i<k;i++){
            if(a[i]>max){
                max=a[i];
            }
        }
        al.add(max);
        for(int h=k;h<n;h++){
            while(!al.contains())
        }
    }
}
