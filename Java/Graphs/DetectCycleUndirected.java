import java.util.*;

public class DetectCycleUndirected {

    static boolean isCycle(List<List<Integer>> graph, int n) {
        boolean[] visited = new boolean[n];

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                if (dfs(graph, i, -1, visited)) {
                    return true;
                }
            }
        }

        return false;
    }

    static boolean dfs(List<List<Integer>> graph, int node, int parent, boolean[] visited) {

        visited[node] = true;

        for (int neighbor : graph.get(node)) {

            if (!visited[neighbor]) {

                if (dfs(graph, neighbor, node, visited))
                    return true;

            } else if (neighbor != parent) {
                // Visited neighbor that isn't the parent -> cycle
                return true;
            }
        }

        return false;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of vertices: ");
        int n = sc.nextInt();

        System.out.print("Enter number of edges: ");
        int e = sc.nextInt();

        List<List<Integer>> graph = new ArrayList<>();

        for (int i = 0; i < n; i++)
            graph.add(new ArrayList<>());

        System.out.println("Enter edges:");

        for (int i = 0; i < e; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();

            graph.get(u).add(v);
            graph.get(v).add(u);
        }

        if (isCycle(graph, n))
            System.out.println("Cycle Detected");
        else
            System.out.println("No Cycle");

        sc.close();
    }
}