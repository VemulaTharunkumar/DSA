import java.util.*;
public class Kthsmallest {
    public static void main(String args[]){
        Kthsmallest o=new Kthsmallest(); 
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int[] a=new int[n];
        for(int i=0;i<n;i++){
            a[i]=sc.nextInt();
        }
        int k=sc.nextInt();
        int res=o.kthsma(a,n,k);
        System.out.print("Kth min element:"+res);
    }
    public int kthsma(int[] a,int n,int k){
        PriorityQueue<Integer>pq=new PriorityQueue<>(Collections.reverseOrder());
        for(int i=0;i<k;i++){
            pq.offer(a[i]);
        }
        for(int j=k;j<n;j++){
            if(a[j]<pq.peek()){
                pq.poll();
                pq.offer(a[j]);
            }
        }
        return pq.peek();
    }
}
