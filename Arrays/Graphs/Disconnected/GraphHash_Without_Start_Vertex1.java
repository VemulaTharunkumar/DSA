import java.util.*;
public class GraphHash_Without_Start_Vertex1{
    HashMap<Integer,List<Integer>> hm;
    int n;
    GraphHash_Without_Start_Vertex1(int n){
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
            System.out.println(i+"-"+hm.get(i));
        }
    }
    public void bfs1(int s,boolean visited[],List<Integer> res){
        Queue<Integer> q=new LinkedList<>();
        visited[s]=true;
        q.offer(s);
        while(!q.isEmpty()){
            int u=q.poll();
            res.add(u);
            for(int v:hm.get(u)){
                if(!visited[v]){
                    visited[v]=true;
                    q.offer(v);
                }
            }
        }
    }
    public List<Integer> bfs(){
        boolean visited[]=new boolean[n];
        List<Integer> res=new ArrayList<>();
        for(int i=0;i<n;i++){
            if(!visited[i]){
                bfs1(i,visited,res);
            }
        }
        return res;
    }
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        GraphHash_Without_Start_Vertex1 g=new GraphHash_Without_Start_Vertex1(n);
        while(true){
            int u=sc.nextInt();
            int v=sc.nextInt();
            g.addEdge(u,v);
            System.out.print("Enter -1 to exit:");
            int x=sc.nextInt();
            if(x==-1){
                break;
            }
        }
        g.display();
        List<Integer> ans=g.bfs();
        for(int x:ans){
            System.out.print(x+" ");
        }
    }
}