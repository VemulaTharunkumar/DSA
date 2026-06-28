import java.util.*;
class Practice{
    List<List<Integer>>l;
    int n;
    Practice(int n){
        this.n=n;
        l=new ArrayList<>();
        for(int i=0;i<n;i++){
            l.add(new ArrayList<>());
        }
    }
    public void addEdge(int u,int v){
        l.get(u).add(v);
        l.get(v).add(u);
    }
    public void display(){
        for(int i=0;i<l.size();i++){
            System.out.print(i+"->");
                System.out.print(l.get(i));
            System.out.println();
        }
    }
    public List<Integer> dfs1(int s){
        boolean visited[]=new boolean[n];
        List<Integer>ls=new ArrayList<>();
        dfs(s,ls,visited);
        for(int i=0;i<n;i++){
            if(!visited[i]){
                dfs(i,ls,visited);
            }
        }
        return ls;
    }
    public void dfs_itr(int s,boolean[] visited){
        Stack<Integer>s1=new Stack<>();
        s1.push(s);
        visited[s]=true;
        while(!s1.isEmpty()){
            int r=s1.pop();
            System.out.print(r+" ");
            for(int u:l.get(r)){
                if(!visited[u]){
                    s1.push(u);
                    visited[u]=true;
                }
            }
        }
    }
    public void dfs(int s,List<Integer> k,boolean[] visited){
        k.add(s);
        visited[s]=true;
        for(int i:l.get(s)){
            if(!visited[i]){
                dfs(i,k,visited);
            }
        }
    }
    public void bfs(int x,boolean[] visited){
        Queue<Integer>q=new LinkedList<>();
        q.add(x);
        visited[x]=true;
        while(!q.isEmpty()){
            int k=q.poll();
            System.out.print(k+" ");
            for(int r:l.get(k)){
            if(!visited[r]){
                q.add(r);
                visited[r]=true;
            }
        }
        }
    }

    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        Practice p=new Practice(n);
        while(true){
        int u=sc.nextInt();
        int v=sc.nextInt();
        p.addEdge(u, v);
        System.out.print("enter -1 to exit");
        int x=sc.nextInt();
        if(x==-1)break;
        }
        int s=sc.nextInt();
        boolean visited[]=new boolean[n];
        /*p.bfs(s,visited);
        System.out.println();
        List<Integer>k=p.dfs1(s);
        for(int x:k){
            System.out.print(x+" ");
        }*/
       p.dfs_itr(s,visited);
    }
}