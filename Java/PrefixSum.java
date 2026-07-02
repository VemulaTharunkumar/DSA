import java.util.*;
class Main{
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        List<Integer>al=new ArrayList<>();
        int[] a=new int[5];
        for(int i=0;i<5;i++){
            a[i]=sc.nextInt();
        }
        int k[]=Psum(a);
        for(int l:k){
            System.out.print(l+" ");
        }
        int r=RangeSum(k);
         System.out.print(r);
    }
    static int[] Psum(int[] a){
        int[] psum=new int[5];
        psum[0]=a[0];
        for(int i=1;i<5;i++){
            psum[i]=psum[i-1]+a[i];
        }
        return psum;
    }
    static int RangeSum(int[] a){
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter start index");
        int s=sc.nextInt();
        System.out.print("Enter end index");
        int e=sc.nextInt();
        if(s==0)return a[e];
        else
        return a[e]-a[s-1];
    }
}