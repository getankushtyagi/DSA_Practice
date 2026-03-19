"""
================================================================================
                    GRAPH THEORY - COMPLETE LEARNING GUIDE
================================================================================

WHAT IS A GRAPH?
----------------
A graph is a non-linear data structure consisting of vertices (nodes) and edges 
that connect these vertices. It's used to represent relationships between objects.

Mathematically: G = (V, E)
Where:
- V = Set of vertices/nodes
- E = Set of edges connecting the vertices


================================================================================
                        GRAPH TERMINOLOGY
================================================================================

1. VERTEX (NODE)
   - A fundamental unit of a graph
   - Represents an entity or object
   - Example: Cities in a map, People in a social network
   
   Diagram:
        ●  <- This is a vertex/node
        A

2. EDGE (LINK/ARC)
   - A connection between two vertices
   - Represents a relationship between entities
   - Can be directed or undirected
   
   Diagram:
        A ●———● B  <- This line is an edge
        
3. DEGREE OF A VERTEX
   - Number of edges connected to a vertex
   - In Directed graphs:
     * In-degree: Number of incoming edges
     * Out-degree: Number of outgoing edges
   
   Example:
        Undirected Graph:
             B
            / \
           A   C
            \ /
             D
        
        Degree(A) = 2 (connected to B and D)
        Degree(B) = 2 (connected to A and C)
        Degree(C) = 2 (connected to B and D)
        Degree(D) = 2 (connected to A and C)

4. PATH
   - A sequence of vertices where each adjacent pair is connected by an edge
   - Example: A → B → C → D is a path
   
   Diagram:
        A ——→ B ——→ C ——→ D
        This is a path from A to D

5. CYCLE
   - A path where the first and last vertices are the same
   - Starts and ends at the same vertex
   
   Diagram:
           A
          / \
         B   C
          \ /
           D
        
        Cycle: A → B → D → C → A

6. ADJACENT VERTICES
   - Two vertices are adjacent if they are connected by an edge
   - Example: If edge (A, B) exists, then A and B are adjacent
   
   Diagram:
        A ●———● B  <- A and B are adjacent
        
        C ●   ● D  <- C and D are NOT adjacent

7. CONNECTED GRAPH
   - A graph where there is a path between every pair of vertices
   
   Connected Graph:
        A ——— B
        |     |
        C ——— D
   
   Disconnected Graph:
        A ——— B    E ——— F
        |     |
        C ——— D

8. COMPLETE GRAPH
   - A graph where every vertex is connected to every other vertex
   - Denoted as Kn where n is number of vertices
   
   Complete Graph (K4):
           A
          /|\
         / | \
        B——|——C
         \ | /
          \|/
           D

9. WEIGHTED GRAPH
   - A graph where edges have weights/costs associated with them
   
   Diagram:
            5
        A ——— B
        |  3  |
       2|     |4
        |     |
        C ——— D
            7

10. SELF LOOP
    - An edge that connects a vertex to itself
    
    Diagram:
         ↻
        ● A
        
11. PARALLEL EDGES (MULTI-GRAPH)
    - Multiple edges between the same pair of vertices
    
    Diagram:
        A ═══ B  (Two or more edges between A and B)


================================================================================
                         TYPES OF GRAPHS
================================================================================

1. UNDIRECTED GRAPH
   ------------------
   - Edges have no direction
   - Edge (A, B) = Edge (B, A)
   - Bidirectional relationship
   
   Example:
        A ——— B
        |     |
        C ——— D
   
   Edges: {(A,B), (A,C), (B,D), (C,D)}
   
   Real-world: Facebook friendships (mutual)

2. DIRECTED GRAPH (DIGRAPH)
   -------------------------
   - Edges have direction (arrows)
   - Edge A → B is different from B → A
   - One-way relationship
   
   Example:
        A ——→ B
        ↑     ↓
        C ←—— D
   
   Edges: {(A,B), (B,D), (D,C), (C,A)}
   
   Real-world: Twitter follows (one-way), Web page links

3. WEIGHTED GRAPH
   ---------------
   - Each edge has a numerical value (weight/cost)
   - Used to represent distances, costs, capacities
   
   Example:
            10
        A ———— B
        |   5  |
       3|      |7
        |      |
        C ———— D
            4
   
   Real-world: Road networks (distances), Flight routes (prices)

4. UNWEIGHTED GRAPH
   -----------------
   - All edges are considered to have equal weight (usually 1)
   
   Example:
        A ——— B
        |     |
        C ——— D

5. CYCLIC GRAPH
   -------------
   - Contains at least one cycle
   
   Example:
        A → B
        ↑   ↓
        D ← C
        
        Cycle: A → B → C → D → A

6. ACYCLIC GRAPH
   --------------
   - Contains no cycles
   
   Example:
        A → B → D
        ↓
        C → E
        
   Special case: DAG (Directed Acyclic Graph)

7. DIRECTED ACYCLIC GRAPH (DAG)
   -----------------------------
   - Directed graph with no cycles
   - Used in: Task scheduling, dependency resolution
   
   Example:
        A → B → D
        ↓   ↓
        C → E
   
   Real-world: Course prerequisites, Build systems

8. TREE
   -----
   - Connected acyclic undirected graph
   - Special case of graph
   - N vertices have N-1 edges
   
   Example:
            A
           / \
          B   C
         / \
        D   E

9. BIPARTITE GRAPH
   ----------------
   - Vertices can be divided into two disjoint sets
   - No edge connects vertices within the same set
   
   Example:
        Set 1: {A, C}    Set 2: {B, D}
        
        A          B
         \        /|
          \      / |
           \    /  |
            \  /   |
             \/    |
             /\    |
            /  \   |
           /    \  |
          /      \ |
        C          D
   
   Real-world: Job matching, Task assignment

10. DENSE GRAPH
    ------------
    - Graph with many edges
    - |E| ≈ |V|²
    
    Example (lots of connections):
         A——B
         |\/|
         |/\|
         C——D

11. SPARSE GRAPH
    ------------
    - Graph with few edges
    - |E| ≈ |V|
    
    Example (few connections):
        A——B    E
        |      
        C  D   F


================================================================================
                    GRAPH REPRESENTATION METHODS
================================================================================

Let's use this sample graph for all representations:

        0 ——— 1
        |     |
        |     |
        2 ——— 3

Edges: {(0,1), (0,2), (1,3), (2,3)}
Vertices: {0, 1, 2, 3}


METHOD 1: ADJACENCY MATRIX
---------------------------
A 2D array where matrix[i][j] = 1 if edge exists between vertex i and j

For UNDIRECTED graph:
    0   1   2   3
0 [[0,  1,  1,  0],
1  [1,  0,  0,  1],
2  [1,  0,  0,  1],
3  [0,  1,  1,  0]]

Properties:
✓ Space: O(V²) - inefficient for sparse graphs
✓ Time to check if edge exists: O(1)
✓ Time to find all neighbors: O(V)
✓ Symmetric for undirected graphs
✓ Good for dense graphs

For WEIGHTED graph (distances instead of 1s):
    0   1   2   3
0 [[0,  5,  3,  ∞],
1  [5,  0,  ∞,  7],
2  [3,  ∞,  0,  4],
3  [∞,  7,  4,  0]]

Python Implementation:
"""

# Adjacency Matrix Representation
def create_adjacency_matrix(num_vertices, edges, directed=False):
    """
    Create adjacency matrix from edge list
    
    Args:
        num_vertices: Number of vertices in graph
        edges: List of tuples (u, v) or (u, v, weight)
        directed: True if graph is directed
    """
    # Initialize matrix with zeros
    matrix = [[0] * num_vertices for _ in range(num_vertices)]
    
    for edge in edges:
        if len(edge) == 2:  # Unweighted
            u, v = edge
            weight = 1
        else:  # Weighted
            u, v, weight = edge
        
        matrix[u][v] = weight
        if not directed:
            matrix[v][u] = weight  # Undirected graph
    
    return matrix


# Example Usage:
edges = [(0, 1), (0, 2), (1, 3), (2, 3)]
matrix = create_adjacency_matrix(4, edges)
print("Adjacency Matrix (Unweighted):")
for row in matrix:
    print(row)
print()

# Weighted graph example
weighted_edges = [(0, 1, 5), (0, 2, 3), (1, 3, 7), (2, 3, 4)]
weighted_matrix = create_adjacency_matrix(4, weighted_edges)
print("Adjacency Matrix (Weighted):")
for row in weighted_matrix:
    print(row)
print()

"""
OUTPUT:
Adjacency Matrix (Unweighted):
[0, 1, 1, 0]
[1, 0, 0, 1]
[1, 0, 0, 1]
[0, 1, 1, 0]

Adjacency Matrix (Weighted):
[0, 5, 3, 0]
[5, 0, 0, 7]
[3, 0, 0, 4]
[0, 7, 4, 0]
"""


"""
METHOD 2: ADJACENCY LIST
-------------------------
An array of lists where each index represents a vertex and stores its neighbors

For UNDIRECTED graph:
    0 → [1, 2]
    1 → [0, 3]
    2 → [0, 3]
    3 → [1, 2]

Visual representation:
    0: 1 → 2 → None
    1: 0 → 3 → None
    2: 0 → 3 → None
    3: 1 → 2 → None

Properties:
✓ Space: O(V + E) - efficient for sparse graphs
✓ Time to check if edge exists: O(degree of vertex)
✓ Time to find all neighbors: O(1) + O(degree)
✓ Most commonly used representation
✓ Good for both sparse and dense graphs

For WEIGHTED graph (store tuples):
    0 → [(1, 5), (2, 3)]
    1 → [(0, 5), (3, 7)]
    2 → [(0, 3), (3, 4)]
    3 → [(1, 7), (2, 4)]

Python Implementation:
"""

from collections import defaultdict

# Adjacency List Representation
class Graph:
    def __init__(self, num_vertices, directed=False):
        """
        Initialize graph with adjacency list
        
        Args:
            num_vertices: Number of vertices
            directed: True if graph is directed
        """
        self.num_vertices = num_vertices
        self.directed = directed
        # Using defaultdict for cleaner code
        self.adj_list = defaultdict(list)
    
    def add_edge(self, u, v, weight=None):
        """Add an edge to the graph"""
        if weight is None:
            self.adj_list[u].append(v)
            if not self.directed:
                self.adj_list[v].append(u)
        else:
            self.adj_list[u].append((v, weight))
            if not self.directed:
                self.adj_list[v].append((u, weight))
    
    def print_graph(self):
        """Print the adjacency list"""
        for vertex in range(self.num_vertices):
            print(f"{vertex} → {self.adj_list[vertex]}")


# Example Usage:
print("Adjacency List (Unweighted):")
g1 = Graph(4, directed=False)
g1.add_edge(0, 1)
g1.add_edge(0, 2)
g1.add_edge(1, 3)
g1.add_edge(2, 3)
g1.print_graph()
print()

print("Adjacency List (Weighted):")
g2 = Graph(4, directed=False)
g2.add_edge(0, 1, 5)
g2.add_edge(0, 2, 3)
g2.add_edge(1, 3, 7)
g2.add_edge(2, 3, 4)
g2.print_graph()
print()

print("Adjacency List (Directed):")
g3 = Graph(4, directed=True)
g3.add_edge(0, 1)
g3.add_edge(0, 2)
g3.add_edge(1, 3)
g3.add_edge(2, 3)
g3.print_graph()
print()

"""
OUTPUT:
Adjacency List (Unweighted):
0 → [1, 2]
1 → [0, 3]
2 → [0, 3]
3 → [1, 2]

Adjacency List (Weighted):
0 → [(1, 5), (2, 3)]
1 → [(0, 5), (3, 7)]
2 → [(0, 3), (3, 4)]
3 → [(1, 7), (2, 4)]

Adjacency List (Directed):
0 → [1, 2]
1 → [3]
2 → [3]
3 → []
"""


"""
METHOD 3: EDGE LIST
-------------------
A list of all edges in the graph

For UNDIRECTED graph:
    [(0, 1), (0, 2), (1, 3), (2, 3)]

For WEIGHTED graph:
    [(0, 1, 5), (0, 2, 3), (1, 3, 7), (2, 3, 4)]

Properties:
✓ Space: O(E) - very space efficient
✓ Time to check if edge exists: O(E) - inefficient
✓ Time to find all neighbors: O(E) - inefficient
✓ Useful for algorithms like Kruskal's MST
✓ Simple to implement

Python Implementation:
"""

class EdgeListGraph:
    def __init__(self):
        """Initialize graph with edge list"""
        self.edges = []
    
    def add_edge(self, u, v, weight=None):
        """Add an edge to the graph"""
        if weight is None:
            self.edges.append((u, v))
        else:
            self.edges.append((u, v, weight))
    
    def print_graph(self):
        """Print all edges"""
        print("Edge List:", self.edges)


# Example Usage:
print("Edge List (Unweighted):")
g_edge = EdgeListGraph()
g_edge.add_edge(0, 1)
g_edge.add_edge(0, 2)
g_edge.add_edge(1, 3)
g_edge.add_edge(2, 3)
g_edge.print_graph()
print()

print("Edge List (Weighted):")
g_edge_weighted = EdgeListGraph()
g_edge_weighted.add_edge(0, 1, 5)
g_edge_weighted.add_edge(0, 2, 3)
g_edge_weighted.add_edge(1, 3, 7)
g_edge_weighted.add_edge(2, 3, 4)
g_edge_weighted.print_graph()
print()

"""
OUTPUT:
Edge List (Unweighted):
Edge List: [(0, 1), (0, 2), (1, 3), (2, 3)]

Edge List (Weighted):
Edge List: [(0, 1, 5), (0, 2, 3), (1, 3, 7), (2, 3, 4)]
"""


"""
================================================================================
                    COMPARISON OF REPRESENTATIONS
================================================================================

Operation           | Adjacency Matrix | Adjacency List | Edge List
--------------------|------------------|----------------|------------
Space Complexity    | O(V²)           | O(V + E)       | O(E)
Add Edge            | O(1)            | O(1)           | O(1)
Remove Edge         | O(1)            | O(V)           | O(E)
Check if edge exists| O(1)            | O(V)           | O(E)
Find all neighbors  | O(V)            | O(degree)      | O(E)
Good for            | Dense graphs    | Sparse graphs  | Edge-based algos


================================================================================
                        SPECIAL GRAPH EXAMPLES
================================================================================

EXAMPLE 1: SOCIAL NETWORK (Undirected Graph)
---------------------------------------------
People and their friendships

        Alice ——— Bob
          |       |
        Carol ——— David

Adjacency List:
    Alice → [Bob, Carol]
    Bob → [Alice, David]
    Carol → [Alice, David]
    David → [Bob, Carol]


EXAMPLE 2: WEB PAGES (Directed Graph)
--------------------------------------
Web pages and their links

    Page A ——→ Page B
      ↓          ↓
    Page C ←—— Page D

Adjacency List:
    A → [B, C]
    B → [D]
    C → []
    D → [C]


EXAMPLE 3: CITY ROADS (Weighted Graph)
---------------------------------------
Cities and distances

            50km
    NYC ————————— Boston
     |              |
  80km|             |120km
     |              |
    Philly ———————— DC
           90km

Adjacency List (Weighted):
    NYC → [(Boston, 50), (Philly, 80)]
    Boston → [(NYC, 50), (DC, 120)]
    Philly → [(NYC, 80), (DC, 90)]
    DC → [(Boston, 120), (Philly, 90)]


EXAMPLE 4: PREREQUISITES (DAG)
-------------------------------
Course dependencies

    Math101 → Math201 → Math301
       ↓         ↓
    CS101  →  CS201

Topological order: Math101, CS101, Math201, CS201, Math301


================================================================================
                        COMMON GRAPH PROBLEMS
================================================================================

1. GRAPH TRAVERSAL
   - BFS (Breadth-First Search)
   - DFS (Depth-First Search)

2. SHORTEST PATH
   - Dijkstra's Algorithm (weighted)
   - Bellman-Ford (negative weights)
   - Floyd-Warshall (all pairs)

3. MINIMUM SPANNING TREE
   - Kruskal's Algorithm
   - Prim's Algorithm

4. CYCLE DETECTION
   - DFS-based detection
   - Union-Find

5. TOPOLOGICAL SORTING
   - DFS-based
   - Kahn's Algorithm (BFS)

6. CONNECTIVITY
   - Connected Components
   - Strongly Connected Components (Kosaraju's)

7. BIPARTITE CHECK
   - BFS/DFS with 2-coloring


================================================================================
                        KEY PROPERTIES & FORMULAS
================================================================================

1. For Undirected Graph:
   - Sum of all degrees = 2 × |E|
   - Maximum edges = V × (V - 1) / 2

2. For Directed Graph:
   - Sum of in-degrees = Sum of out-degrees = |E|
   - Maximum edges = V × (V - 1)

3. For Tree (Special Graph):
   - |E| = |V| - 1
   - Exactly one path between any two vertices
   - Connected and acyclic

4. Complete Graph:
   - Every vertex connected to every other vertex
   - |E| = V × (V - 1) / 2 (undirected)
   - |E| = V × (V - 1) (directed)


================================================================================
                        REAL-WORLD APPLICATIONS
================================================================================

1. SOCIAL NETWORKS
   - Facebook: Undirected graph (mutual friends)
   - Twitter: Directed graph (followers)
   - LinkedIn: Finding connections

2. MAPS & NAVIGATION
   - Google Maps: Weighted graph (distances/time)
   - GPS routing
   - Flight connections

3. COMPUTER NETWORKS
   - Internet topology
   - Router connections
   - Network flow problems

4. WEB CRAWLING
   - Web page links (directed graph)
   - PageRank algorithm

5. RECOMMENDATION SYSTEMS
   - Product recommendations
   - Movie/music suggestions
   - Friend suggestions

6. DEPENDENCIES
   - Package managers (npm, pip)
   - Build systems (Makefile)
   - Task scheduling

7. BIOLOGY
   - Protein interaction networks
   - Food webs
   - Neural networks


================================================================================
                        PRACTICE PROBLEMS
================================================================================

BEGINNER:
1. Implement graph using adjacency list
2. Count number of edges
3. Find degree of all vertices
4. Check if graph is connected
5. Print all neighbors of a vertex

INTERMEDIATE:
1. Implement BFS and DFS
2. Detect cycle in undirected graph
3. Find shortest path (BFS)
4. Count connected components
5. Check if graph is bipartite

ADVANCED:
1. Dijkstra's shortest path
2. Detect cycle in directed graph
3. Topological sort
4. Find strongly connected components
5. Minimum spanning tree


================================================================================
                        NOTES & TIPS
================================================================================

1. Choose adjacency list for most problems (space-efficient)
2. Use adjacency matrix when you need O(1) edge lookup
3. Remember: Trees are special graphs (acyclic, connected)
4. For shortest path: BFS (unweighted), Dijkstra (weighted)
5. Always consider if graph is directed or undirected
6. Watch out for disconnected components
7. Use visited array to avoid infinite loops in traversal

================================================================================
"""
