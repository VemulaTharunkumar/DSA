package Disconnected;

public import java.util.*;
public class GraphHash_With_Start_Vertex{
    HashMap<Integer,List<Integer>> hm;
    int n;
    GraphHash_With_Start_Vertex(int n){
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
    public List<Integer> bfs(int s){
        boolean visited[]=new boolean[n];
        List<Integer> res=new ArrayList<>();
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
        return res;
    }
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        GraphHash_With_Start_Vertex g=new GraphHash_With_Start_Vertex(n);
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
        System.out.print("Enter start vertex:");
        int s=sc.nextInt();
        List<Integer> ans=g.bfs(s);
        for(int x:ans){
            System.out.print(x+" ");
        }
    }
}
