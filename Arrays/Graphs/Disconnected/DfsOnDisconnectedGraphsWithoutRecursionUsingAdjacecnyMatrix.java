import java.util.*;
public class DfsOnDisconnectedGraphsWithoutRecursionUsingAdjacecnyMatrix{
    int m[][];
    int n;
    DfsOnDisconnectedGraphsWithoutRecursionUsingAdjacecnyMatrix(int n){
        this.n=n;
        m=new int [n][n];
    }
    public void addEdge(int u,int v){
        m[u][v]=1;
        m[v][u]=1;
    }
    public void print1(){
        System.out.println("Using adjacency matrix(Undirected)");
        for(int[] r:m){
            for(int x:r){
                System.out.print(x+" ");
            }
            System.out.println();
        }
    }
    public void dfs1(int s,boolean visited[]){
        System.out.print(s+" ");
        visited[s]=true;
        for(int i=0;i<n;i++){
            if(m[s][i]==1&&!visited[i]){
                visited[i]=true;
                dfs1(i,visited);
            }
        }
    }
    public ArrayList<Integer> dfs()
    {
        ArrayList<Integer> l=new ArrayList<>();
        boolean visited[]=new boolean[n];
        for (int i=0;i<n;i++)
        {
            if(!visited[i])
            {
                dfs_itr(i,visited,l);
            }
        }
        return l;
    }
    public List<Integer> dfs_itr(int s,boolean visited[],ArrayList<Integer> l){
        Stack<Integer>st=new Stack<>();
        visited[s]=true;
        st.push(s);
        while(!st.isEmpty()){
            int h=st.pop();
            l.add(h);
            for(int i=0;i<n;i++){
                if(m[h][i]==1&&!visited[i]){
                    visited[i]=true;
                    st.push(i);
                }
            }
        }
        return l;
    }

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter n");
        int n=sc.nextInt();
        DfsOnDisconnectedGraphsWithoutRecursionUsingAdjacecnyMatrix g=new DfsOnDisconnectedGraphsWithoutRecursionUsingAdjacecnyMatrix(n);
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
        
        List<Integer> q=g.dfs();
        for(int x:q){
            System.out.print(x+" ");
        }
       
        System.out.println("Using iteartive dfs (Adjacency Matrix)");
        g.dfs();

    }
}