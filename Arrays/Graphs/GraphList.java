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
    public void dfs(int s,boolean visited[]){
        System.out.print(s+" ");
        visited[s]=true;
        for(int i:l.get(s)){
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
            for(int i:l.get(h)){
                if(!visited[i]){
                    visited[i]=true;
                    st.push(i);
                }
            }
        }
        return l1;
    }

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
        g.print1();
        /*int s=sc.nextInt();
        boolean visited[]=new boolean[n];
        List<Integer>a=g.dfs_itr(s, visited);
        System.out.println("Using Adjacency list(DFS)");
        for(int t:a){
                System.out.print(t+" ");
            }
        /*System.out.println("Using Adjacency list(DFS)");
        g.dfs(s,visited);   
        }*/
        }
    }