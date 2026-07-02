public class GraphColoring{
    public boolean dfs(List<List<Integer>>g,int s,int col,int[] color){
        color[s]=col;
        for(int x:g.get(s)){
            if(color[x]==1){
                if(dfs(g,x,1-col,color)==false){
                return false;
                }    
            }
        }
        return g;
    }
}