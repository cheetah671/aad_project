import collections

def _count_reachable_nodes(adj_list, num_nodes, start_node, removed_vertex=None, removed_edge=None):
    """
    Helper function to count reachable nodes using BFS,
    ignoring a specified vertex or edge.
    """
    visited = set()
    queue = collections.deque()

    # Handle case where the start_node is the one being removed
    if start_node == removed_vertex:
        # If the start_node is removed, we can't start a traversal from it.
        # This function is designed to check connectivity of the *remaining* graph,
        # so the caller must provide a valid start_node from the remaining nodes.
        return 0  
        
    queue.append(start_node)
    visited.add(start_node)
    count = 0

    while queue:
        u = queue.popleft()
        count += 1

        # Use .get() for safety, in case a node has no neighbors
        for v in adj_list.get(u, []):
            if v == removed_vertex or v in visited:
                continue
            
            # Check if the edge (u, v) is the one to be removed
            if removed_edge:
                if (u == removed_edge[0] and v == removed_edge[1]) or \
                   (u == removed_edge[1] and v == removed_edge[0]):
                    continue
            
            visited.add(v)
            queue.append(v)
            
    return count

def find_articulation_points_naive(adj_list, num_nodes):
    """
    Finds all articulation points using the naive O(V * (V+E)) method.
    """
    if num_nodes <= 2:
        return set() # A graph with 0, 1, or 2 nodes has no articulation points

    articulation_points = set()
    
    for v_to_remove in range(num_nodes):
        # Pick a valid start node from the remaining graph
        start_node = -1
        for i in range(num_nodes):
            if i != v_to_remove:
                start_node = i
                break
        
        if start_node == -1: # Should only happen if num_nodes is 1, handled above
            continue

        # Count how many nodes are reachable in the graph *without* v_to_remove
        reachable_count = _count_reachable_nodes(adj_list, 
                                                 num_nodes, 
                                                 start_node, 
                                                 removed_vertex=v_to_remove)
        
        # If the number of reachable nodes is less than the total remaining nodes,
        # the graph was disconnected by removing v_to_remove.
        if reachable_count < num_nodes - 1:
            articulation_points.add(v_to_remove)
            
    return articulation_points

def find_bridges_naive(adj_list, num_nodes):
    """
    Finds all bridges using the naive O(E * (V+E)) method.
    """
    if num_nodes <= 1:
        return set()

    bridges = set()
    all_edges = set()

    # 1. Get a unique list of all edges
    for u in adj_list:
        for v in adj_list[u]:
            # Add as a sorted tuple to avoid duplicates like (0, 1) and (1, 0)
            if u < v:
                all_edges.add((u, v))
    
    # 2. Iterate through each edge and test removal
    for u, v in all_edges:
        edge_to_remove = (u, v)
        
        # Count nodes reachable from any valid start node (e.g., node 0)
        reachable_count = _count_reachable_nodes(adj_list, 
                                                 num_nodes, 
                                                 0, 
                                                 removed_edge=edge_to_remove)
        
        # If not all nodes are reachable, the graph is disconnected
        if reachable_count < num_nodes:
            bridges.add(edge_to_remove)
            
    return bridges

# --- User Input Section ---

# Use defaultdict to easily build the adjacency list
adj_list = collections.defaultdict(list)

try:
    num_nodes = int(input("Enter the number of nodes (e.g., 5): "))
    num_edges = int(input("Enter the number of edges (e.g., 6): "))

    print(f"\nEnter {num_edges} edges, one per line (e.g., '0 1'):")
    
    for _ in range(num_edges):
        line = input().split()
        if len(line) < 2:
            print("Invalid input. Please enter two space-separated node IDs.")
            continue
            
        u, v = int(line[0]), int(line[1])
        
        if u >= num_nodes or v >= num_nodes or u < 0 or v < 0:
            print(f"Invalid edge: ({u}, {v}). Nodes must be between 0 and {num_nodes - 1}.")
            continue
            
        adj_list[u].append(v)
        adj_list[v].append(u)

    print("\n--- Graph Input Complete ---")
    print(f"Graph has {num_nodes} nodes.")

    # Find Articulation Points
    aps = find_articulation_points_naive(adj_list, num_nodes)
    print(f"Naive Articulation Points: {aps if aps else 'None'}")

    # Find Bridges
    bridges = find_bridges_naive(adj_list, num_nodes)
    print(f"Naive Bridges: {bridges if bridges else 'None'}")

except ValueError:
    print("Invalid input. Please enter integers for nodes and edges.")
except EOFError:
    pass