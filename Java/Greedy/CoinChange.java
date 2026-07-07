import java.util.*;
public class CoinChange {
    public static void main(String args[]){
    Scanner sc=new Scanner(System.in);    
    int[] d={2000,500,200,100,50,20,10,5,2,1};
    int V=sc.nextInt();
    int c=0;
    for(int i=0;i<d.length;i++){
        c+=V/d[i];
        V=V%d[i];
    }
    System.out.print("Change in min :"+c);
    }
}
