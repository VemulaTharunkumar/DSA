//Find all components and its vertices 
import java.util.*;
public class Components {
    int m[][],n;
    Components(int n){
        this.n=n;
        m=new int[n][n];
    }
    public void addEdge(int u,int v){
        m[u][v]=1;
    }
    public void display(){
        for(int[] x:m){
            for(int g:x){
                System.out.print(g+" ");
            }
            System.out.println();
        }
    }
    public void dfs(int s,boolean[] visited){
        Stack<Integer>st=new Stack<>();
        visited[s]=true;
        st.push(s);
        while(!st.isEmpty()){
            int p=st.pop();
            System.out.print(p+" ");            
            for(int i=0;i<n;i++){
            if(m[p][i]==1&&!visited[i]){
                visited[i]=true;
                st.push(i);
            }
        }
    }
    }
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        Components c=new Components(n);
        while(true){
            int u=sc.nextInt();
            int v=sc.nextInt();
            c.addEdge(u,v);
            System.out.print("Enter -1 to quit :");
            int x=sc.nextInt();
            if(x==-1){
                break;
            }
        }
        c.display();
        int s=sc.nextInt();
        boolean[] visited=new boolean[n];
        c.dfs(s,visited);
    }

}
