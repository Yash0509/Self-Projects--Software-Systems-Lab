package Q1;

import java.util.Map.Entry;
import java.util.*; 
import java.util.regex.*;


class NodeDistance implements Comparator<NodeDistance> {

    public Node node;
    public Integer nodeDistance;

    public NodeDistance(){}
    public NodeDistance(Node node,Integer nodeDistance){
        this.node = node;
        this.nodeDistance = nodeDistance;
    }

    @Override
    public int compare(NodeDistance n1, NodeDistance n2) {
        if (n1.nodeDistance < n2.nodeDistance)
            return -1;
        else if (n1.nodeDistance > n2.nodeDistance)
            return 1;
        else
            return 0;
    }
}

public class Graph {

    // Assume maximum path length to be less than INF
    private static Integer INF = 1000*1000*1000 ;
    private Map<String, Node> nodeMap = new HashMap<>() ;

    List<Node> nodeList = new ArrayList<Node>();
    List<Integer> distanceFromSource = new ArrayList<Integer>();
    PriorityQueue<NodeDistance> priorityQueue = new PriorityQueue<NodeDistance>(1000, new NodeDistance());
    Set<String> visitedNodes = new HashSet<String>();

    public void addNode(String name) {
        /*
         * TODO: Implement this method
         */
        Node node = new Node(name);
        nodeMap.put(name,node);
        nodeList.add(node);
        distanceFromSource.add(INF);

    }

    public void addDirectedEdge(String nameA, String nameB, Integer distance) {
        /*
         * TODO: Implement this method
         * Check if nodes with nameA and nameB exist.
         */
        if(nodeMap.containsKey(nameA) && nodeMap.containsKey(nameB)){
            Node tmpA = nodeMap.get(nameA);
            Node tmpB = nodeMap.get(nameB);
            tmpA.addNeighbour(tmpB,distance);
        }
    }

    public Map<String, Integer> dijkstraAlgorithm(String source) {
        /*
         * TODO: Implement this method
         * Return a map of name of all the nodes
         * with the minimum distance from source node
         */
        distanceFromSource.set(Integer.valueOf(source),0);
        Node sourceNode = nodeMap.get(source);
        Integer noOfNodes = nodeList.size();

        priorityQueue.add(new NodeDistance(sourceNode,0));

        while(visitedNodes.size() != noOfNodes){
//        while(count<1){
            Node u = priorityQueue.remove().node;
            visitedNodes.add(u.getName());
//            calculateNearestAdjacentNode(sourceNode);
            calculateNearestAdjacentNode(u);
//            count++;

//            while(!priorityQueue.isEmpty()){
//                NodeDistance nd = priorityQueue.remove();
//                System.out.println("Node in pq are "+nd.node.getName()+" with distance as "+nd.nodeDistance);
//            }
        }
        Map<String, Integer> distance = new HashMap<>();
        for(int i=0;i<distanceFromSource.size();i++)
            distance.put(String.valueOf(i),distanceFromSource.get(i));

//            System.out.println("min distance for node "+i+" is "+distanceFromSource.get(i));


//        return null;
        return distance;
    }

    private void calculateNearestAdjacentNode(Node u) {
        Map<Node,Integer> nodeMap = u.adjacentNodes;
        int edgeDistance = -1;
        int newDistance = -1;

        for(Node node : nodeMap.keySet()){
            Integer nodeDistance = nodeMap.get(node);
//            System.out.println("For node "+u.getName()+" neighbouring node is "+node.getName()+" at distance of "+nodeDistance);
            if(!visitedNodes.contains(node.getName())){
                edgeDistance = nodeDistance;
                newDistance = distanceFromSource.get(Integer.valueOf(u.getName())) + edgeDistance;

                if(newDistance < distanceFromSource.get(Integer.valueOf(node.getName())))
                    distanceFromSource.set(Integer.valueOf(node.getName()),newDistance);

                priorityQueue.add(new NodeDistance(node,distanceFromSource.get(Integer.valueOf(node.getName()))));
            }
        }

    }
}
