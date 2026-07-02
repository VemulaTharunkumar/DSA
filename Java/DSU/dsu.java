import java.util.*;
public class dsu{
    int n;
    int[] parent;
    int k;
    dsu(int n){
        this.n=n;
        parent=new int[n];
        for(int i=0;i<n;i++){
            parent[i]=i;
        }
        this.k=this.n;
    }
    public int find(int r){
        if(parent[r]==r){
            return r;
        }
        return find(parent[r]);
    }
    public void union(int i,int j){
        int i1=find(i);
        int j1=find(j);
        if(i1!=j1){
            parent[i1]=j1;
            k--;
        }
    }
    void comp(){
        HashMap<Integer,ArrayList<Integer>> hm = new HashMap<>();
        for (int i = 0;i<n;i++){
            int par = find(i);
            if(!hm.containsKey(par)){
                ArrayList<Integer> arr = new ArrayList<>();
                arr.add(i);
                hm.put(par,arr);
            }
            else{
                ArrayList<Integer> arr = hm.get(par);
                arr.add(i);
                hm.put(par,arr);
            }
        }
        for (int i : hm.keySet()){
            System.out.println(i+":" + hm.get(i));
        }
    }    
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        dsu d=new dsu(n);
        while(true){
            int x=sc.nextInt();
            switch(x){
                case 1:
                    int i=sc.nextInt();
                    int j=sc.nextInt();
                    d.union(i,j);
                    break;
                case 2:
                    int u=sc.nextInt();
                    int v=sc.nextInt();
                    int r=d.find(u);
                    int s=d.find(v);
                    if(r==v||s==u){
                        System.out.print("They are Friends");
                    }
                    else{
                        System.out.print("They are not friends");
                    }
                    break;
                case 3:
                    System.out.println("Friend Groups :"+d.k);    
                    break;
                case 4:
                    d.comp();
                    break;
                case 5:
                    System.exit(0);        
            }
        }
    }
}
