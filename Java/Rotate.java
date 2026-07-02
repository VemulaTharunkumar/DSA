public class Rotate {
    public static void main(String args[]){
        int[] a={400,500,600,700};
        int[] k=r(a);
        for(int o:k){
            System.out.print(o+" ");
        }
    }
    static int[] r(int[] a){
        int n=a.length-1;
        int i=0;
        int j=n;
        while(i<j){
            int y=a[i];
            a[i]=a[j];
            a[j]=y;
            i++;
            j--;
        }
        return a;
    }
}
