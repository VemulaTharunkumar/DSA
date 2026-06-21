/*public class TwoSum {
    public static void main(String[] args) {
    int n=6;
    int a[]={10,9,-3,8,1,7};
    int tar=7;
    boolean j=istrue(a,n,tar);
    System.out.print(j);
}
    static boolean istrue(int[] a,int n,int tar){
        int i=0,j=n-1;
        while(i<j){
            if(a[i]+a[j]==tar){
                return true;
            }
            else if(a[i]+a[j]<tar){
                i++;
            }
            else j--;
        }
        return false;
    }
}*/
//check weather pair exists or not that equals to 0 and return as arraylist .
import java.util.*;
class TwoSum{
    public static void main(String args[]){
        int[] a={-4,-4,-2,-2,0,0,2,2,4,4};
        ArrayList<ArrayList<Integer>> jk=Psum(a);
        for(ArrayList<Integer> x:jk){
            System.out.print(x+" ");
        }
    }
    static ArrayList<ArrayList<Integer>> Psum(int[] a){
        ArrayList<ArrayList<Integer>>ml=new ArrayList<>();
        int i=0;
        int j=a.length-1;
        while(i<j){
            if(a[i]+a[j]==0){
                ArrayList<Integer>al=new ArrayList<>();
                al.add(i);
                al.add(j);
                ml.add(al);
                int l=a[i];
                int r=a[j];
                while(i<j&&l==a[i])i++;
                while(i<j&&j==a[j])j--;
            }
            else if(a[i]+a[j]<0)i++;
            else j--;
        }
        return ml;
    }
}
