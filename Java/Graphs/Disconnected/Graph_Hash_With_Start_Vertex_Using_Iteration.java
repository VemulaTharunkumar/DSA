import java.util.*;
public class Graph_Hash_With_Start_Vertex_Using_Iteration {
    HashMap<Integer,List<Integer>>hm;
    List<Integer>l;
    int n;
    Graph_Hash_With_Start_Vertex_Using_Iteration(int n){
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
    public List<Integer> dfs(int s){
        boolean visited[] = new boolean[n];
        List<Integer>res=new ArrayList<>();
        dfs_itr(s, visited, res);
        for (int i = 0; i<n;i++){
            if(!visited[i]){
                dfs_itr(i,visited,res);
            }
        }
        return res;
    }
    public void dfs_itr(int s,boolean visited[],List<Integer>res){
        Stack<Integer>st=new Stack<>();
        st.push(s);
        while(!st.isEmpty()){
            int h=st.pop();
            if(!visited[h]){
                visited[h]=true;
                res.add(h);
            }
            for(int i:hm.get(h)){
                if(!visited[i]){
                    st.push(i);
                }
            }
        }
    }    
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        Graph_Hash_With_Start_Vertex_Using_Iteration g=new Graph_Hash_With_Start_Vertex_Using_Iteration(n);
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
        System.out.println("Enter Start : ");
        int start = sc.nextInt();
        List<Integer>o=g.dfs(start);
        for(int i:o){
            System.out.print(i+" ");
        }
    }
}