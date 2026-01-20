"""
Program: City Emergency Routing
Project: SnowRescueMobile emergency dispatch tool
Purpose: To locate the nearest station, resolve building codes, and compute safe routes during a city snowstorm
Revision History
    created by Myungjeong Han Dec 2025
"""
from collections import deque


# ------------------------------------
# Part A — Set Emergency Stations
# ------------------------------------

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class StationBST:
    def __init__(self):
        self.root = None

    def insert(self, id:int) -> None:
        """
        Handles empty tree case
        Time Complexity: O(h) where h is height - Average O(log n), Worst O(n) for unbalanced tree
        Space Complexity: O(h) due to recursive call stack
        """
        # If tree is empty, make this the root
        if self.root is None:
            self.root = TreeNode(id)
        else:
            # Call recursive helper to find the right spot and insert
            self.root = self._insert_recursive(self.root,id)

    def _insert_recursive(self, node, id):
        """
        Private helper: handles the recursion for insertion
        Time Complexity: O(h) - traverse down one path from root to leaf
        Space Complexity: O(h) - recursion stack
        """
        # Base case: create a new node when we reach an empty spot in the tree
        if node is None:
            return TreeNode(id)
        if id < node.data:
            node.left = self._insert_recursive(node.left, id)
        elif id > node.data:
            node.right = self._insert_recursive(node.right, id)
        # Returns the node with its updated subtree
        return node

    def find(self, id:int) -> TreeNode | None:
        """
        Start searching from the root
        User doesn't need to pass the root. we start from it automatically
        Time Complexity: O(h) - Average O(log n), Worst O(n)
        Space Complexity: O(h) - recursion stack
        """
        return self._find_recursive(self.root, id)

    def _find_recursive(self, node, id):
        """
        Internal recursive function that moves left or right to find the id
        Time Complexity: O(h) - one comparison per level
        Space Complexity: O(h) - recursion stack
        """
        # Base case: not found
        if node is None:
            return None
        # Case 1: found the target ID
        elif node.data == id:
            return node
        # Case 2: Target ID is less than the node, go left
        elif id < node.data:
            return self._find_recursive(node.left, id)
        # Case 3: Target ID is greater than the node, go right
        elif id > node.data:
            return self._find_recursive(node.right, id)

    def _find_min(self, node):
        """
        Helper Method: Find In-Order Successor, which is the leftmost node (Minimum Node)
        Time Complexity: O(h) - traverse left path to minimum
        Space Complexity: O(1) - no extra space
        """
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, id:int) -> None:
        """
        Time Complexity: O(h) - find node O(h) + delete O(h)
        Space Complexity: O(h) - recursion stack
        """
        self.root = self._delete_recursive(self.root, id)

    def _delete_recursive(self, node, id):
        """
        This function always returns the current node.
        If no deletion happens, it just returns the same node.
        If a deletion happens, it returns the node with its children updated.
        Time Complexity: O(h) - traverse to find
        Space Complexity: O(h) - recursion stack
        """
        # Base Case: ID not found or tree is empty
        if node is None:
            print(f"{id} not found")
            return node

        # Step 1. Traverse to find the node
        if id < node.data:
            node.left = self._delete_recursive(node.left, id)
        elif id > node.data:
            node.right = self._delete_recursive(node.right, id)
        # Step 2. node(=id) Found: 'node' is the node to be deleted.
        else:   # id == node.data
            # Case 1. No children: the first 'if' is True, so it returns immediately
            # Case 2. One child: either the 'if' or the 'elif' is True, so it returns immediately
            if node.left is None:
                temp = node.right
                return temp
            elif node.right is None:
                temp = node.left
                return temp
            # Case 3. Two children: both 'if' and 'elif' above are False, so the code below runs.
            # 1. Find the in-order successor(the minimum node in the right subtree)
            temp = self._find_min(node.right)
            # 2. Copy the successor's data to the current node
            node.data = temp.data
            # 3. Recursively delete the successor node from the right subtree.
            # The in-order successor has at most one child
                # Case 1): no children (leaf)
                # Case 2): only right child (left is always None)
            node.right = self._delete_recursive(node.right, temp.data)
        return node

    def in_order(self) -> list[int]:
        """
        Time Complexity: O(n) - visit every node once
        Space Complexity: O(n) - result list + O(h) recursion stack
        """
        # Start in-order traversal and return sorted list
        result = []
        self._in_order_recursive(self.root, result)
        return result

    def _in_order_recursive(self, node, result):
        """
        Time Complexity: O(n) - visit all nodes
        Space Complexity: O(h) - recursion stack depth
        """
        # Base case: if node is empty, go back to previous call
        if node is None:
            return
        # Step 1: Visit left subtree
        self._in_order_recursive(node.left, result)
        # Step 2: Process current node
        result.append(node.data)
        # Step 3: Visit right subtree
        self._in_order_recursive(node.right, result)

    def nearest_ge(self, target_id) -> int | None:
        """
        Finds the smallest station ID >= target_id. (That is, next closest usable station)
        Assume stations < target ID are already passed/unreachable.
        Returns the station ID (int) if found, otherwise None.
        Time Complexity: O(n) - in_order traversal O(n) + binary search O(log n) = O(n)
        Space Complexity: O(n) - stores sorted list
        """
        sorted_stations = self.in_order()
        left, right = 0, len(sorted_stations) - 1
        result = None

        while left <= right:
            mid = (left + right) // 2
            if sorted_stations[mid] >= target_id:
                result = sorted_stations[mid]
                right = mid - 1
            else:
                left = mid + 1

        return result


# ------------------------------------
# Part B — Implement Building Catalog
# ------------------------------------

class BuildingTable:
    def __init__(self, capacity, load_factor_threshold=0.7):
        self.capacity = capacity
        self.size = 0   # Number of stored key-value pairs
        self.threshold = load_factor_threshold
        self.buckets = [[] for _ in range(self.capacity)]

    def _hash(self, key):
        """
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return hash(key) % self.capacity

    def load_factor(self) -> float:
        """
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return self.size/self.capacity

    def _resize(self):
        """
        Time Complexity: O(n) - rehash all n items
        Space Complexity: O(n) - create new table
        """
        print(f"-----Resizing from {self.capacity} to {self.capacity * 2}-----")
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0

        for chain in old_buckets:
            for code, info in chain:
                self.put(code, info)

    def put(self, code:str, info:dict) -> None:  #key = building code, value = building info(dict)
        """
        Time Complexity: Average O(1), Worst O(n) - all keys in one bucket
        Space Complexity: O(n) - stores one key-value pair
        """
        #1. Use the hash of the key to find the right bucket
        index = self._hash(code)
        chain = self.buckets[index]

        #2. Update the existing key(code), if key exists
        for i, (k, v) in enumerate(chain):
            if k == code:
                chain[i] = (code, info)     # chain[i] = buckets[index][i]
                return                      # Size didn't change, no need to check load factor

        #3. Insert the new key(code)
        chain.append((code, info))
        self.size += 1                      # New item added, so size increased

        #4. Check for resizing
        if self.load_factor() >= self.threshold:
            self._resize()

    def get(self, code:str) -> dict | None:
        """
        Time Complexity: Average O(1), Worst O(n) - all keys in same bucket
        Space Complexity: O(1)
        """
        index = self._hash(code)
        chain = self.buckets[index]

        for k, v in chain:
            if k == code:
                return v
        print(f"Code'{code}' not found")
        return None

    def remove(self, code:str) -> bool:
        """
        Time Complexity: Average O(1), Worst O(n) - all in one bucket
        Space Complexity: O(1)
        """
        index = self._hash(code)
        chain = self.buckets[index]

        for i, (k, v) in enumerate(chain):
            if k == code:
                del chain[i]
                self.size -= 1
                return True
        print(f"Code'{code}' not found")
        return False


# ------------------------------------
# Part C — District Network Graph
# ------------------------------------


class DistrictGraph:
    def __init__(self, nodes:list[str]) -> None:
        """
        Explanation of 'self.node_index'
        I use a dictionary (self.node_index) to map each node name to its index in the adjacency matrix.
        If I used nodes.index(name) each time, it would have to search through the list from the beginning,
        which takes O(n) time in the worst case.
        Since adding or removing edges calls this lookup often, it becomes inefficient.
        With the dictionary, I can look up the index in O(1) average time,
        making all graph operations faster and simpler.
        """
        self.nodes = nodes
        self.n = len(nodes)
        # Map node name(str) to index ex.{'D1': 0, 'D2': 1, 'D3': 2}
        self.node_index = {node:i for i, node in enumerate(nodes)}
        # Create adjacency matrix: n x n matrix initialized to 0 (no edges)
        self.matrix = [[0 for _ in range(self.n)] for _ in range(self.n)]

    def add_edge(self, u:str, v:str) -> None:
        """
        Adds an undirected edge between districts u and v
        Updates both [u][v] and [v][u] to 1
        Time Complexity: O(1) - direct matrix access
        Space Complexity: O(1)
        """
        # Check both nodes exist
        if u not in self.node_index:
            print(f"Error: Node {u} not found in the graph")
            return
        if v not in self.node_index:
            print(f"Error: Node {v} not found in the graph")
            return

        # Find the indices of nodes u and v
        i = self.node_index[u]  #Insetead of using 'i = self.nodes.index(u)' which takes O(n) time,
        j = self.node_index[v]  #using 'self.node_index[u]' takes O(1) average time

        # Set both positions to 1 (undirected = symmetric)
        self.matrix[i][j] = 1
        self.matrix[j][i] = 1

    def remove_edge(self, u:str, v:str) -> None:
        """
        Removes the undirected edge between districts u and v
        Set both [u][v] and [v][u] to 0
        Time Complexity: O(1) - direct matrix access
        Space Complexity: O(1)
        """
        if u not in self.node_index:
            print(f"Error: Node {u} not found in the graph")
            return
        if v not in self.node_index:
            print(f"Error: Node {v} not found in the graph")
            return

        i = self.node_index[u]
        j = self.node_index[v]

        # Remove edge (set to 0)
        self.matrix[i][j] = 0
        self.matrix[j][i] = 0

    def bfs_shortest_path(self, src:str, dst:str) -> list[str] | None:
        """
        Finds the shortest path (fewest edges) from src to dst using BFS
        Returns list of district names forming the path if exists
        Time Complexity: O(n^2) - visit n nodes, each checks n columns = n × n
        Space Complexity: O(n) - visited, previous, queue
        """
        if src not in self.node_index:
            print(f"Error: Source {src} not found in the graph")
            return None
        if dst not in self.node_index:
            print(f"Error: Destination {dst} not found in the graph")
            return None

        # Early return if source = destination
        if src == dst:
            return [src]

        start = self.node_index[src]
        end = self.node_index[dst]

        # BFS setup (visits all vertices at the same distance first)
        visited = [False] * self.n
        previous = [None] * self.n     # To reconstruct the path later
        queue = deque([start])      #The queue holds the indices of nodes we will visit next
        visited[start] = True

        # BFS traversal
        while queue:
            current = queue.popleft()

            # Check if we reached the destination node
            if current == end:
                # Reconstruct path from end to start
                path = []
                # current starts at the destination index, follow previous nodes back to the start
                # Loop ends when we reach the start node (previous[start] is always None)
                while current is not None:
                    path.append(self.nodes[current])
                    current = previous[current]
                return path[::-1]   #Reverse the path list

            # Check all neighbors
            for neighbor in range(self.n):
                # Check if there's an edge from current to neighbor and neighbor hasn't been visited yet
                if self.matrix[current][neighbor] == 1 and visited[neighbor] is False:
                    visited[neighbor] = True
                    previous[neighbor] = current
                    queue.append(neighbor)      #Add neighbor to the queue

        print(f"No path from {src} to {dst}")
        return None

    def dfs_component_count(self) -> int:
        """
        Returns the number of connected components in the graph using DFS
        Time Complexity: O(n^2) - visit n nodes, each checks n columns = n × n
        Space Complexity: O(n) - visited O(n) + recursion stack O(n) in worst case
        """
        visited = [False] * self.n      # Track visited nodes
        count = 0                       # Connected components counter

        for i in range(self.n):
            if visited[i] is False:
                self._dfs_helper(i, visited)    #This DFS call explores all nodes in one connected component
                count += 1
        return count

    def _dfs_helper(self, node:int, visited: list) -> None:
        """
        Performs DFS from given node index
        Marks all reachable nodes as visited
        Time Complexity: O(n^2) - in worst case
        Space Complexity: O(n) - recursion depth
        """
        visited[node] = True

        for neighbor in range(self.n):
            if self.matrix[node][neighbor] == 1 and visited[neighbor] is False:
                self._dfs_helper(neighbor, visited)


# ------------------------------------
# Part D — End-to-End Dispatch Query
# ------------------------------------

def dispatch_route(building_code: str, target_station_hint: int,
                   building_table: BuildingTable,
                   station_bst: StationBST,
                   district_graph: DistrictGraph) -> dict:
    """
    Complete dispatch workflow: resolve building, pick station, find route
    Returns dictionary with route info or {"status": "UNREACHABLE"} if route cannot be found
    Time Complexity: O(n^2) - building_table.get() O(1) + nearest_ge() O(n) + BFS O(n^2)
    Space Complexity: O(n) - BFS/DFS arrays and path storage
    """
    #Step 1. Find building info using HashTable
    building_info = building_table.get(building_code)
    if building_info is None:
        return {"status": f"Building code {building_code} not found"}

    building_name = building_info["name"]
    building_district = building_info["district"]

    #Step 2. Pick nearest station
    station_id = station_bst.nearest_ge(target_station_hint)
    if station_id is None:
        # No station >= target hint, use the maximum station ID
        station_ids = station_bst.in_order()
        # Check if list is empty
        if not station_ids:
            return {"status": "NO_STATIONS_AVAILABLE"}
        station_id = station_ids[-1]  #maximum ID

    # Step 3. Map station ID to its district
    number_of_districts = district_graph.n
    station_district = f"D{(station_id % number_of_districts) + 1}"

    # Step 4. Find BFS path
    path = district_graph.bfs_shortest_path(station_district, building_district)

    # Step 5. If city is split and no path exists
    if path is None and district_graph.dfs_component_count() > 1:
        return {"status": "UNREACHABLE"}

    # Step 6. Return dispatch info
    return {
        "building": building_name,
        "from_station": station_id,
        "path": path
    }



# Demo for BST
print("Demo for PartA. BST")
station_bst = StationBST()
station_bst.insert(7)
station_bst.insert(15)
station_bst.insert(23)
station_bst.insert(31)
station_bst.insert(40)

print(station_bst.in_order())  # [7, 15, 23, 31, 40]
print(station_bst.nearest_ge(20))  # 23
print()

# Demo for HashTable
print("Demo for PartB. HashTable")
building_table = BuildingTable(capacity=5)
building_table.put("MH-5", {"name": "Memorial Hospital", "district": "D2"})
building_table.put("LB-8", {"name": "City Library", "district": "D3"})

print(building_table.get("MH-5"))  # {"name": "Memorial Hospital", "district": "D2"}
print()

# Demo for Graph
print("Demo for PartC. Graph")
district_graph = DistrictGraph(["D1", "D2", "D3", "D4"])
district_graph.add_edge("D1", "D2")
district_graph.add_edge("D2", "D3")
district_graph.add_edge("D3", "D4")

path = district_graph.bfs_shortest_path("D1", "D3")
print(path)  # ["D1", "D2", "D3"]
print()

# Demo for dispatch_route() with Custom Example
print("Demo for dispatch_route() with Custom Example\n")
result = dispatch_route("LB-8", 20, building_table, station_bst, district_graph)
print(f"Building: {result.get('building')}")
print(f"From Station: {result.get('from_station')}")
print(f"Station to Building Path: {result.get('path')}")

#
# # ------------------------------------
# # Part A: station BST tests
# # ------------------------------------
# print("")
# print("Part A: station BST tests")
#
# # Test 1: Insert stations
# print("\n[Test 1] Inserting stations")
# station_bst = StationBST()
# station_ids = [42, 18, 64, 7, 29, 50, 71]
# for sid in station_ids:
#     station_bst.insert(sid)
#     print(f"Inserted station {sid}")
#
# # Test 2: In-order traversal (should be sorted)
# print("\n[Test 2] In-order traversal")
# sorted_stations = station_bst.in_order()
# print(f"Stations: {sorted_stations}")
#
# # Test 3: Find existing station
# print("\n[Test 3] Finding existing station 42")
# found = station_bst.find(42)
# if found:
#     print(f"Station 42 found! Data: {found.data}")
# else:
#     print(f"Station 42 not found")
#
# # Test 4: Find non-existing station
# print("\n[Test 4] Finding non-existing station 99:")
# found = station_bst.find(99)
# if found:
#     print(f"Station 99 found! Data: {found.data}")
# else:
#     print(f"Station 99 not found")
#
# # Test 5: Nearest GE - between values
# print("\n[Test 5] nearest_ge(30):")
# result = station_bst.nearest_ge(30)
# print(f"Result: {result}")
#
# # Test 6: Nearest GE - higher than all
# print("\n[Test 6] nearest_ge(100) - higher than all:")
# result = station_bst.nearest_ge(100)
# print(f"Result: {result}")
#
# # Test 7: Delete leaf node
# print("\n[Test 7] Deleting leaf node 7:")
# print(f"Before: {station_bst.in_order()}")
# station_bst.delete(7)
# print(f"After:  {station_bst.in_order()}")
#
# # Test 8: Delete node with one child
# print("\n[Test 8] Deleting node with one child 18:")
# print(f"Before: {station_bst.in_order()}")
# station_bst.delete(18)
# print(f"After:  {station_bst.in_order()}")
#
# # Test 9: Delete node with two children
# print("\n[Test 9] Deleting node with two children 42:")
# print(f"Before: {station_bst.in_order()}")
# station_bst.delete(42)
# print(f"After:  {station_bst.in_order()}")
#
# # Test 10: Delete non-existing node
# print("\n[Test 10] Deleting non-existing node 99:")
# station_bst.delete(99)
#
#
# # ------------------------------------
# # Part B: Building Hash Table Tests
# # ------------------------------------
# print("")
# print("Part B: Building Hash Table Tests")
#
# # Test 1: Create hash table and add buildings
# print("[Test 1] Creating hash table and inserting buildings\n")
# building_table = BuildingTable(capacity=4)
# building_table.put("H-120", {"name": "Hillcrest Seniors Home", "district": "D3"})
# building_table.put("M-005", {"name": "Mapleview Mall", "district": "D2"})
# building_table.put("U-404", {"name": "University Arena", "district": "D1"})
# building_table.put("W-902", {"name": "Winter Operations Depot", "district": "D4"})
# print(f"Total buildings added: {building_table.size}")
# for i, bucket in enumerate(building_table.buckets):
#     print(f"Bucket {i}: {bucket}")
#
# # Test 2: Check load factor
# print("\n[Test 2] Current load factor:")
# print(f"Load factor: {building_table.load_factor():.2f}")
# print(f"Size: {building_table.size}, Capacity: {building_table.capacity}")
#
# # Test 3: Get existing building info
# print("\n[Test 3] Getting existing building info U-404:")
# result = building_table.get("U-404")
# if result:
#     print(f"Found: {result}")
# else:
#     print(f"Not found")
#
# # Test 4: Get non-existing building info
# print("\n[Test 4] Getting non-existing building info X-505:")
# result = building_table.get("X-505")
#
# # Test 5: Update existing building
# print("\n[Test 5] Updating building H-120 name:")
# print(f"Before: {building_table.get('H-120')}")
# building_table.put("H-120", {"name": "Hillcrest Senior Center (Updated)", "district": "D3"})
# print(f"After:  {building_table.get('H-120')}")
#
# # Test 6: Trigger resize by adding more buildings
# print("\n[Test 6] Adding more buildings to trigger resize (threshold=0.7)")
# print(f"Current: Size={building_table.size}, Capacity={building_table.capacity}")
# building_table.put("S-555", {"name": "Sports Complex", "district": "D2"})
# building_table.put("P-333", {"name": "Police Station", "district": "D1"})
# print(f"After resize: Size={building_table.size}, Capacity={building_table.capacity}")
#
# # Test 7: Remove building
# print("\n[Test 7] Removing building M-005:")
# print(f"Before removal: Size={building_table.size}")
# remove_building = building_table.remove("M-005")
# print(f"After removal: Size={building_table.size}")
#
# # Test 8: Try to remove non-existing building
# print("\n[Test 8] Removing non-existing building Z-999:")
# remove_building2 = building_table.remove("Z-999")
#
#
# # ------------------------------------
# # Part C: District Graph Tests
# # ------------------------------------
# print("")
# print("Part C: District Graph Tests")
#
# # Test 1: Create graph
# print("\n[Test 1] Creating district graph with 4 nodes:")
# district_graph = DistrictGraph(['D1', 'D2', 'D3', 'D4'])
# print(f"Nodes: {district_graph.nodes}")
#
# # Test 2: Add edges
# print("\n[Test 2] Adding edges D1-D2, D2-D3, D3-D4:")
# district_graph.add_edge('D1', 'D2')
# district_graph.add_edge('D2', 'D3')
# district_graph.add_edge('D3', 'D4')
# print("Edges added successfully")
#
# # Test 3: Display adjacency matrix
# print("\n[Test 3] Adjacency Matrix:")
# for i, node in enumerate(district_graph.nodes):
#     print(f"{node}: {district_graph.matrix[i]}")
#
# # Test 4: BFS shortest path
# print("\n[Test 4] BFS shortest path from D1 to D4:")
# path = district_graph.bfs_shortest_path('D1', 'D4')
# print(f"Path: {path}")
#
# # Test 5: BFS shortest path - same node
# print("\n[Test 5] BFS shortest path from D1 to D1:")
# path = district_graph.bfs_shortest_path('D1', 'D1')
# print(f"Path: {path}")
#
# # Test 6: Component count - fully connected
# print("\n[Test 6] Component count (fully connected):")
# count = district_graph.dfs_component_count()
# print(f"Number of components: {count}")
#
# # Test 7: Remove edge and check components
# print("\n[Test 7] Removing edge D2-D3 and checking components:")
# district_graph.remove_edge('D2', 'D3')
# count = district_graph.dfs_component_count()
# print(f"Number of components after split: {count}")
#
# # Test 8: BFS after network split
# print("\n[Test 8] BFS shortest path from D1 to D4 after split:")
# path = district_graph.bfs_shortest_path('D1', 'D4')
# print(f"Path: {path}")
#
# # ------------------------------------
# # Part D: Dispatch Route Tests
# # ------------------------------------
# print("")
# print("Part D: Dispatch Route Tests")
#
# # Create Station BST, Building Table, District Graph
# station_bst = StationBST()
# for sid in [42, 18, 64, 7, 29, 50, 71]:
#     station_bst.insert(sid)
#
# building_table = BuildingTable(capacity=10)
# building_table.put("H-120", {"name": "Hillcrest Seniors Home", "district": "D3"})
# building_table.put("M-005", {"name": "Mapleview Mall", "district": "D2"})
# # building_table.put("U-404", {"name": "University Arena", "district": "D1"})
# building_table.put("W-902", {"name": "Winter Operations Depot", "district": "D4"})
#
# district_graph = DistrictGraph(['D1', 'D2', 'D3', 'D4'])
# district_graph.add_edge('D1', 'D2')
# district_graph.add_edge('D2', 'D3')
# district_graph.add_edge('D3', 'D4')
#
# # Test 1: Normal dispatch
# print("\n[Test 1] Dispatch to U-404 with hint 30:")
# result = dispatch_route("U-404", 30, building_table, station_bst, district_graph)
# print(f"Building: {result.get('building')}")
# print(f"From Station: {result.get('from_station')}")
# print(f"Station to Building Path: {result.get('path')}")
#
# # Test 2: Dispatch with hint higher than all stations
# print("\n[Test 2] Dispatch to W-902 with hint 100 (fallback to max):")
# result = dispatch_route("W-902", 100, building_table, station_bst, district_graph)
# print(f"Building: {result.get('building')}")
# print(f"From Station: {result.get('from_station')} (expected: 71, the max)")
# print(f"Path: {result.get('path')}")
#
# # Test 3: Invalid building code
# print("\n[Test 3] Dispatch to invalid building X-505:")
# result = dispatch_route("X-505", 30, building_table, station_bst, district_graph)
# print(f"{result}")
#
# # Test 4: Network split scenario
# print("\n[Test 4] Dispatch after network split:")
# print("Removing edge D2-D3 to split network")
# district_graph.remove_edge('D2', 'D3')
# print(f"Components: {district_graph.dfs_component_count()}")
# result2 = dispatch_route("U-404", 30, building_table, station_bst, district_graph)
# print(f"Status: {result2}")
