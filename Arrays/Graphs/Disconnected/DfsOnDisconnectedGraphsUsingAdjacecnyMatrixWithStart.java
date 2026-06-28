import java.util.*;
public class DfsOnDisconnectedGraphsUsingAdjacecnyMatrixWithStart{
    int m[][];
    int n;
    DfsOnDisconnectedGraphsUsingAdjacecnyMatrixWithStart(int n){
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
    public void dfs(int s)
    {
        boolean visited[]=new boolean[n];
        dfs1(s,visited);
        for (int i=0;i<n;i++)
        {
            if(!visited[i])
            {
                dfs1(i,visited);
            }
        }
    }
    public List<Integer> dfs_itr(int s,boolean visited[]){
        List<Integer>l=new ArrayList<>();
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
        DfsOnDisconnectedGraphsUsingAdjacecnyMatrixWithStart g=new DfsOnDisconnectedGraphsUsingAdjacecnyMatrixWithStart(n);
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
        /*int s=sc.nextInt();
        List<Integer> q=g.dfs_itr(s, visited);
        for(int x:q){
            System.out.print(x+" ");
        }*/
       System.out.println("Enter start vertex");
       int s=sc.nextInt();
       
        System.out.println("Using recursive dfs (Adjacency Matrix)");
        g.dfs(s);

    }
}
