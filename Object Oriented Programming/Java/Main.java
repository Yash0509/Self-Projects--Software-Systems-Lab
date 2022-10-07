package Q1;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.* ;

public class Main {
    public static void main(String[] args) throws FileNotFoundException {
        // Instantiate a Graph object graph
        Graph graph = new Graph();
        Integer numberOfNodes;
        Integer numberOfEdges;

        File file = new File("Q1\\input.txt");
        Scanner sc= new Scanner(file);
        String line = sc.nextLine();
        String [] strList = line.split(" ");

        numberOfNodes = Integer.parseInt(strList[0]);
        numberOfEdges = Integer.parseInt(strList[1]);

        line = sc.nextLine();
        strList = line.split(" ");

        // Create nodes with given name
        for (int i=0;i<numberOfNodes;i++) {
            String name = strList[i];
            graph.addNode(name);
        }

        // Create Edges between given nodes
        for (int i=0;i<numberOfEdges;i++) {
            line = sc.nextLine();
            strList = line.split(" ");
            graph.addDirectedEdge(strList[0], strList[1], Integer.parseInt(strList[2]));
        }

        // Source Vertex
        String source = sc.nextLine();
        Map<String, Integer> distances = graph.dijkstraAlgorithm(source);
        for (Map.Entry<String, Integer> entry : distances.entrySet()) {
            System.out.println(entry.getKey() + " " + Integer.toString(entry.getValue()));
        }
    }
}
