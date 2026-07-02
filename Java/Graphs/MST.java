import java.util.*;
public class MST {
    static int parent[];
    public static int find(int x) {
        if (parent[x] == x) {
            return x;
        }
        return parent[x] = find(parent[x]);
    }
    public static void union(int x, int y) {
        int p1 = find(x);
        int p2 = find(y);
        if (p1 != p2) {
            parent[p2] = p1;
        }
    }
    public static class Edge {
        int u, v, w;
        Edge(int u, int v, int w) {
            this.u = u;
            this.v = v;
            this.w = w;
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of nodes: ");
        int n = sc.nextInt();
        parent = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
        List<Edge> edges = new ArrayList<>();
        while (true) {
            System.out.println("Enter u v w (-1 -1 -1 to stop):");
            int u = sc.nextInt();
            int v = sc.nextInt();
            int w = sc.nextInt();

            if (u == -1 && v == -1 && w == -1) {
                break;
            }

            edges.add(new Edge(u, v, w));
        }
        Collections.sort(edges, (a, b) -> a.w - b.w);
        int mstWeight = 0;
        for (Edge e : edges) {
            if (find(e.u) != find(e.v)) {
                union(e.u, e.v);
                mstWeight += e.w;
                System.out.println("Edge added to MST: " + e.u + " - " + e.v + " with weight " + e.w);
            }
        }
        System.out.println("Total weight of MST: " + mstWeight);
    }
}
