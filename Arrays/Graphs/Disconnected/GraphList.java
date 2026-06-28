import java.util.*;
public class GraphList{
    List<List<Integer>>l;
    int n;
    GraphList(int n){
        this.n=n;
        l=new ArrayList<>();
        for(int i=0;i<n;i++){
        l.add(new ArrayList<>());
        }        
    }
    public void addEdge(int u,int v){
        l.get(u).add(v);
    }
    public void print1(){
        for(int i=0;i<l.size();i++){
            System.out.print(i + " -> ");
        for(int x : l.get(i)){
            System.out.print(x + " ");
        }
        System.out.println();
    }
}
    public List<Integer> dfs(int s){
        List<Integer> la=new ArrayList<>();
        boolean visited[]=new boolean[n];
        dfs1(s,visited,la);
        for(int i=0;i<n;i++){
            if(!visited[i]){
                dfs1(i,visited,la);
            }
        }
        return la;
    }
    public void dfs1(int s,boolean visited[],List<Integer> li){
        li.add(s);
        visited[s]=true;
        for(int i:l.get(s)){
            if(!visited[i]){
                dfs1(i,visited,li);
            }
        }
    }
    /*public void dfs_itr(int s,boolean visited[],List<Integer> k){
        Stack<Integer>st=new Stack<>();
        visited[s]=true;
        st.push(s);
        while(!st.isEmpty()){
            int h=st.pop();
            k.add(h);
            for(int i:l.get(h)){
                if(!visited[i]){
                    visited[i]=true;
                    st.push(i);
                }
            }
        }
    }*/
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter n");
        int n=sc.nextInt();
        GraphList g=new GraphList(n);
        while(true){
        System.out.println("Enter u,v :");
        int u=sc.nextInt();
        int v=sc.nextInt();
        g.addEdge(u, v);
        System.out.print("Enter -1 to exit:");
        int x=sc.nextInt();
        if (x==-1){
            break;
        }
        }
        
        //int s=sc.nextInt();
        boolean visited[]=new boolean[n];
        int s=sc.nextInt();
        List<Integer>a=g.dfs(s);
        System.out.println("Using Adjacency list(DFS) with start vertex");
        for(int t:a){
                System.out.print(t+" ");
            }
        /*System.out.println("Using Adjacency list(DFS)");
        g.dfs(s,visited);   
        }*/
        }
    }