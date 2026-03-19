"""
================================================================================
                    BINARY TREE - COMPLETE LEARNING GUIDE
================================================================================

WHAT IS A BINARY TREE?
-----------------------
A hierarchical data structure where each node has at most two children,
referred to as left child and right child.

Node Structure:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None


================================================================================
                        TREE TERMINOLOGY
================================================================================

Visual Example:
                    1 (Root)
                   / \\
                  2   3
                 / \\   \\
                4   5   6
               /
              7

TERMS:
- ROOT: Top node (1)
- LEAF: Node with no children (4, 5, 6, 7)
- PARENT: Node with children (1 is parent of 2,3)
- CHILD: Node connected to parent
- SIBLINGS: Nodes with same parent (2 and 3)
- ANCESTOR: Nodes on path from node to root
- DESCENDANT: Nodes in subtree of a node
- EDGE: Connection between nodes
- PATH: Sequence of nodes connected by edges
- DEPTH: Length of path from root to node
  - Depth of 1 = 0, Depth of 4 = 2
- HEIGHT: Length of longest path from node to leaf
  - Height of tree = Height of root = 3
- LEVEL: Depth + 1
  - Level 1: {1}, Level 2: {2,3}, Level 3: {4,5,6}
- SUBTREE: Tree consisting of node and its descendants


================================================================================
                        TYPES OF BINARY TREES
================================================================================

1. FULL BINARY TREE (STRICT BINARY TREE)
   Every node has 0 or 2 children (no node has 1 child)
   
           1
          / \\
         2   3
        / \\
       4   5
   
   ✓ Nodes 1,2 have 2 children
   ✓ Nodes 3,4,5 have 0 children


2. COMPLETE BINARY TREE
   All levels filled except possibly last, which fills left to right
   
           1
          / \\
         2   3
        / \\  /
       4  5 6
   
   ✓ All levels filled except last
   ✓ Last level filled from left
   
   Used in: Heap data structure


3. PERFECT BINARY TREE
   All internal nodes have 2 children, all leaves at same level
   
           1
          / \\
         2   3
        / \\ / \\
       4  5 6  7
   
   Properties:
   - Nodes at level i = 2^i
   - Total nodes = 2^(h+1) - 1
   - Height h, has 2^h leaves


4. BALANCED BINARY TREE
   Height of left and right subtrees differ by at most 1
   
           1
          / \\
         2   3
        / \\
       4   5
   
   |height(left) - height(right)| ≤ 1 for all nodes
   
   Examples: AVL tree, Red-Black tree


5. DEGENERATE TREE (PATHOLOGICAL TREE)
   Each parent has only one child (like linked list)
   
       1
        \\
         2
          \\
           3
            \\
             4
   
   Worst case for binary tree operations


6. SKEWED BINARY TREE
   All nodes aligned to one side
   
   Left Skewed:        Right Skewed:
       1                   1
      /                     \\
     2                       2
    /                         \\
   3                           3


================================================================================
                        BINARY SEARCH TREE (BST)
================================================================================

DEFINITION:
A binary tree where for each node:
- Left subtree has values less than node
- Right subtree has values greater than node

Example:
           8
          / \\
         3   10
        / \\    \\
       1   6    14
          / \\   /
         4   7 13

Property: Inorder traversal gives sorted order


BST OPERATIONS:

1. SEARCH:
   def search(root, key):
       if root is None or root.val == key:
           return root
       if key < root.val:
           return search(root.left, key)
       return search(root.right, key)
   
   Time: O(h) where h is height
   Best: O(log n) balanced, Worst: O(n) skewed

2. INSERT:
   def insert(root, key):
       if root is None:
           return Node(key)
       if key < root.val:
           root.left = insert(root.left, key)
       else:
           root.right = insert(root.right, key)
       return root

3. DELETE:
   Three cases:
   a) Leaf node - simply remove
   b) One child - replace with child
   c) Two children - replace with inorder successor/predecessor


================================================================================
                        TREE TRAVERSALS
================================================================================

Given Tree:
           1
          / \\
         2   3
        / \\
       4   5

1. INORDER (Left-Root-Right)
   Order: 4, 2, 5, 1, 3
   
   def inorder(root):
       if root:
           inorder(root.left)
           print(root.val)
           inorder(root.right)
   
   Use: BST gives sorted order

2. PREORDER (Root-Left-Right)
   Order: 1, 2, 4, 5, 3
   
   def preorder(root):
       if root:
           print(root.val)
           preorder(root.left)
           preorder(root.right)
   
   Use: Create copy of tree, prefix expression

3. POSTORDER (Left-Right-Root)
   Order: 4, 5, 2, 3, 1
   
   def postorder(root):
       if root:
           postorder(root.left)
           postorder(root.right)
           print(root.val)
   
   Use: Delete tree, postfix expression

4. LEVEL ORDER (BFS)
   Order: 1, 2, 3, 4, 5
   
   def levelorder(root):
       if not root:
           return
       queue = [root]
       while queue:
           node = queue.pop(0)
           print(node.val)
           if node.left:
               queue.append(node.left)
           if node.right:
               queue.append(node.right)
   
   Use: Level by level processing


================================================================================
                        TREE VIEWS
================================================================================

Given Tree:
                1
               / \\
              2   3
             / \\   \\
            4   5   6
           /     \\   \\
          8       9   7

1. TOP VIEW: [8, 4, 2, 1, 3, 6, 7]
   Nodes visible from top

2. BOTTOM VIEW: [8, 4, 9, 6, 7]
   Nodes visible from bottom

3. LEFT VIEW: [1, 2, 4, 8]
   First node at each level from left

4. RIGHT VIEW: [1, 3, 6, 7]
   Last node at each level

5. VERTICAL ORDER: Group by vertical line
   HD -3: [8]
   HD -2: [4]
   HD -1: [2]
   HD  0: [1, 5, 9]
   HD +1: [3]
   HD +2: [6]
   HD +3: [7]


================================================================================
                        COMMON OPERATIONS
================================================================================

1. HEIGHT/DEPTH OF TREE
   def height(root):
       if not root:
           return 0
       return 1 + max(height(root.left), height(root.right))
   
   Time: O(n)

2. COUNT NODES
   def count_nodes(root):
       if not root:
           return 0
       return 1 + count_nodes(root.left) + count_nodes(root.right)

3. CHECK IF BALANCED
   def is_balanced(root):
       def check(node):
           if not node:
               return 0
           left = check(node.left)
           if left == -1:
               return -1
           right = check(node.right)
           if right == -1:
               return -1
           if abs(left - right) > 1:
               return -1
           return 1 + max(left, right)
       
       return check(root) != -1

4. DIAMETER (Longest path between any two nodes)
   def diameter(root):
       self.max_dia = 0
       
       def dfs(node):
           if not node:
               return 0
           left = dfs(node.left)
           right = dfs(node.right)
           self.max_dia = max(self.max_dia, left + right)
           return 1 + max(left, right)
       
       dfs(root)
       return self.max_dia

5. LOWEST COMMON ANCESTOR (LCA)
   def lca(root, p, q):
       if not root or root == p or root == q:
           return root
       left = lca(root.left, p, q)
       right = lca(root.right, p, q)
       if left and right:
           return root
       return left if left else right


================================================================================
                        SPECIAL BINARY TREES
================================================================================

1. AVL TREE
   - Self-balancing BST
   - Balance factor: height(left) - height(right) ∈ {-1, 0, 1}
   - Rotations: LL, RR, LR, RL

2. RED-BLACK TREE
   - Self-balancing BST with color property
   - Every node is red or black
   - Root and leaves are black
   - Red node has black children
   - All paths have same number of black nodes

3. SEGMENT TREE
   - For range queries
   - Build: O(n), Query: O(log n)

4. TRIE (PREFIX TREE)
   - For string operations
   - Each path represents a word


================================================================================
                        TREE CONSTRUCTION
================================================================================

1. FROM INORDER AND PREORDER
   Preorder: [1, 2, 4, 5, 3]
   Inorder:  [4, 2, 5, 1, 3]
   
   - First of preorder is root (1)
   - Find root in inorder, split into left/right
   - Recursively build left and right subtrees

2. FROM INORDER AND POSTORDER
   Similar approach, last of postorder is root

Note: Cannot construct uniquely from preorder and postorder alone!


================================================================================
                        SERIALIZATION & DESERIALIZATION
================================================================================

Convert tree to string and back:

def serialize(root):
    if not root:
        return \"null\"
    return f\"{root.val},{serialize(root.left)},{serialize(root.right)}\"

def deserialize(data):
    def build(nodes):
        val = next(nodes)
        if val == \"null\":
            return None
        node = Node(int(val))
        node.left = build(nodes)
        node.right = build(nodes)
        return node
    
    return build(iter(data.split(',')))


================================================================================
                        TIME COMPLEXITY
================================================================================

Operation           | Balanced BST | Skewed BST | General Tree
--------------------|--------------|------------|-------------
Search              | O(log n)     | O(n)       | O(n)
Insert              | O(log n)     | O(n)       | O(1)*
Delete              | O(log n)     | O(n)       | O(n)
Height              | O(n)         | O(n)       | O(n)
Traversal           | O(n)         | O(n)       | O(n)
Space (recursion)   | O(log n)     | O(n)       | O(h)

* If node pointer is given


================================================================================
                        APPLICATIONS
================================================================================

1. BINARY SEARCH TREE
   - Searching, sorting
   - Database indexing

2. EXPRESSION TREES
   - Arithmetic expressions
   - Compilers

3. HUFFMAN CODING TREE
   - Data compression

4. DECISION TREES
   - Machine learning

5. FILE SYSTEMS
   - Directory structure

6. DOM (HTML)
   - Web page structure


================================================================================
                        COMMON PROBLEMS
================================================================================

BEGINNER:
1. Maximum depth of tree
2. Invert binary tree
3. Same tree
4. Path sum
5. Symmetric tree

INTERMEDIATE:
1. Validate BST
2. Lowest common ancestor
3. Level order traversal
4. Diameter of tree
5. Balanced binary tree check
6. Right/left view
7. Vertical order traversal
8. Top/bottom view

ADVANCED:
1. Maximum path sum
2. Serialize/deserialize tree
3. Construct tree from traversals
4. Morris traversal (O(1) space)
5. Count complete tree nodes
6. Flatten tree to linked list
7. All nodes at distance k


================================================================================
                        IMPORTANT NOTES
================================================================================

1. Always check if node is None before accessing
2. Height = edges from node to deepest leaf
3. Depth = edges from root to node
4. Complete tree ≠ Full tree ≠ Perfect tree
5. BST inorder gives sorted sequence
6. Use queue for level order (BFS)
7. Use stack/recursion for DFS
8. Balance factor crucial for performance
9. NULL nodes count as leaves in some problems
10. Tree cannot have cycles

================================================================================
"""
