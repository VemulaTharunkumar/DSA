import java.util.*;
public class TopoList {
    List<List<Integer>> l;
    int n;

    TopoList(int n) {
        this.n = n;
        l = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            l.add(new ArrayList<>());
        }
    }
    public void addEdge(int u, int v) {
        l.get(u).add(v);
    }
    public List<Integer> topoSort() {
        int indegree[] = new int[n];
        for (int i = 0; i < n; i++) {
            for (int x : l.get(i)) {
                indegree[x]++;
            }
        }
        Queue<Integer> q = new LinkedList<>();

        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                q.add(i);
            }
        }
        List<Integer> result = new ArrayList<>();
        while (!q.isEmpty()) {
            int node = q.poll();
            result.add(node);

            for (int x : l.get(node)) {
                indegree[x]--;
                if (indegree[x] == 0) {
                    q.add(x);
                }
            }
        }
        return result;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of nodes: ");
        int n = sc.nextInt();

        TopoList g = new TopoList(n);

        while (true) {
            System.out.println("Enter u v (-1 -1 to stop):");
            int u = sc.nextInt();
            int v = sc.nextInt();

            if (u == -1 && v == -1) {
                break;
            }

            g.addEdge(u, v);
        }

        List<Integer> topo = g.topoSort();

        System.out.println("Topological Order:");
        for (int x : topo) {
            System.out.print(x + " ");
        }
    }
}