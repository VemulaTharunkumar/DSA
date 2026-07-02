import java.util.Scanner;

public class Flood_Fill {
    public static int [][] floodFill(int img[][],int sr,int sc,int newcol){
        if (img[sr][sc]==newcol){
            return img;
        }
        int m = img.length;
        int n = img[0].length;
        int oldcol=img[sr][sc];
        dfs(img,sr,sc,m,n,oldcol,newcol);
        return img;
    }
    public static void dfs(int [][]img,int sr,int sc,int m,int n,int oldcol,int newcol){
        if(sr<0 || sc<0 || sr>=n||sc>=m||img[sr][sc]!=oldcol){
            return;
        }
        img[sr][sc]=newcol;
        dfs(img,sr+1,sc,m,n,oldcol,newcol);
        dfs(img,sr-1,sc,m,n,oldcol,newcol);
        dfs(img,sr,sc+1,m,n,oldcol,newcol);
        dfs(img,sr,sc-1,m,n,oldcol,newcol);
    }
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter no.of rows");
        int n=sc.nextInt();
        System.out.println("Enter no.of Columns : ");
        int m=sc.nextInt();
        int img[][]=new int[n][m];
        for (int i = 0 ; i < n ; i ++){
            for (int j = 0 ; j < m ; j ++){
                img[i][j]=sc.nextInt();
            }
        }
        System.out.println("Enter Source Row : ");
        int srow=sc.nextInt();
        System.out.println("Enter Source Column : ");
        int scol = sc.nextInt();
        System.out.println("Enter New Color : ");
        int newcol = sc.nextInt();
        int res[][]= floodFill(img , srow,scol,newcol);
        for (int i = 0 ; i < n ; i++){
            for (int j = 0 ; j < m ; j++){
                System.out.print(res[i][j]);
            }
            System.out.println(" ");
        }
    }
}