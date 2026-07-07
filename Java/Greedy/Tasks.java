import java.util.*;

public class Tasks {
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int[] a=new int[n];
        for(int i=0;i<n;i++){
            a[i]=sc.nextInt();
        }
        int left=sc.nextInt();
        int u=tasks(a,n,left);
        System.out.println("Min :"+u);
    }
    public static int tasks(int[] a,int n,int left){
        Arrays.sort(a);
        int c=0;
        for(int i=0;i<n;i++){
            if(left!=0&&a[i]<=left){
            left-=a[i];
            c++;
            }
            else{
                break;
            }
        }
        return c;
    }    
}
