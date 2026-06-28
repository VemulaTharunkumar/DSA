import java.util.*;
public class GraphHash {
    HashMap<Integer,List<Integer>>hm;
    List<Integer>l;
    int n;
    GraphHash(int n){
        this.n=n;
        hm=new HashMap<>();
        for(int i=0;i<n;i++){
        hm.put(i,new ArrayList<>());
        }
    }
    public void addEdge(int u,int v){
        hm.get(u).add(v);
    }
    public void display(){
        for(int i:hm.keySet()){
            System.out.print(i+"-"+hm.get(i));
            System.out.println();
        }
    }
    public void dfs(int s,boolean visited[]){
        System.out.print(s+" ");
        visited[s]=true;
        for(int i:hm.get(s)){
            if(!visited[i]){
                dfs(i,visited);
            }
        }
    }
    public List<Integer> dfs_itr(int s,boolean visited[]){
        List<Integer>l1=new ArrayList<>();
        Stack<Integer>st=new Stack<>();
        visited[s]=true;
        st.push(s);
        while(!st.isEmpty()){
            int h=st.pop();
            l1.add(h);
            for(int i:hm.get(h)){
                if(!visited[i]){
                    visited[i]=true;
                    st.push(i);
                }
            }
        }
        return l1;
    }    
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        GraphHash g=new GraphHash(n);
        while(true){
            int u=sc.nextInt();
            int v=sc.nextInt();
            g.addEdge(u, v);
            System.out.print("Enter -1 to exit:");
            int x=sc.nextInt();
            if(x==-1){
                break;
            }
        }
        System.out.println("Using Adjacency list with Hashmap");
        boolean visited[]=new boolean[n];
        int s=sc.nextInt();
        List<Integer>o=g.dfs_itr(s, visited);
        for(int i:o){
            System.out.print(i+" ");
        }
    }
}
