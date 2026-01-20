from collections import deque

from Dec1_Directed_Graph import DirectedGraph


def bfs(graph, start_node):
    """
    Performs a Breadth-First Search on a graph.
    graph: A dictionary (adjacency list) or object with a get_neighbors method.
    """
    # Use a deque for the queue structure
    queue = deque([start_node])
    # Keep track of visited nodes to avoid cycles and redundant work
    visited = {start_node}                    #visited = [] 리스트로 변경시                          #set 사용했고, 아이템추가하려면 add() 사용
    # print(type(visited))        #{원소1} 원소가 하나라도 있으면 set()한것과 동일하게 set으로 인식
    # visited2 = {}               #원소없이 {} 중괄호는 dictionary로 인식
    # print(type(visited2))
    traversal_order = []

    while queue:
        # Dequeue the current node
        current_node = queue.popleft()          # O(1) 처음 큐에 A만 있었으니 이걸로시작하고 for loop 다 돌고나면 다시 current_node가 그다음 큐에있던 B로 바뀌고 다시 for loop으로 이웃확인
        traversal_order.append(current_node)

        # Iterate over all unvisited neighbors
        for neighbor in graph.get_neighbors(current_node):  #처음 A에서 시작해서 첫번째 for loop에서 이웃 B, 두번째 for loop에서 C 나왔으니 일단 현재노드 A에 대해서는 for loop종료
            if neighbor not in visited:     #visited가 set인 경우 O(1), 리스트인 경우 O(n) 차이
                visited.add(neighbor)        # 리스트인경우, visited.append(neighbor)
                queue.append(neighbor)

    return traversal_order #최종 순회한 리스트 반환

graph_ex = DirectedGraph()
graph_ex.add_edge('A', 'B'); graph_ex.add_edge('A', 'C'); graph_ex.add_edge('B', 'D')
print(f"BFS Order: {bfs(graph_ex, 'A')}") # BFS Order: ['A', 'B', 'C', 'D']


#while queue: 큐안에 있는 순서대로 current_node 업데이트해가며 for loop으로 이웃방문
    # ┌─────────────────────────────────────────┐
    # │ 1) current_node = queue.popleft()       │
    # │ 2) for neighbor in neighbors(current):  │
    # │        - 방문 안했으면 visited 추가         │
    # │        - queue.append()                 │
    # └─────────────────────────────────────────┘


# from collections import deque
# from Dec1_Directed_Graph import DirectedGraph
#
# def bfs(graph, start_node):
#     queue = deque([start_node])
#     visited = {start_node}
#     traversal_order = []
#
#     while queue:
#         current_node = queue.popleft()
#         traversal_order.append(current_node)
#
#         for neighbor in graph.get_neighbors(current_node):
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 queue.append(neighbor)
#
#     return traversal_order
#
# graph_ex = DirectedGraph()
# graph_ex.add_edge('A', 'B')
# graph_ex.add_edge('A', 'C')
# graph_ex.add_edge('B', 'D')
#
# print(f"BFS Order: {bfs(graph_ex, 'A')}")
# def get_neighbors(self, u):
#     neighbors = []
#     for v in range(self.size):
#         if self.adj_matrix[u][v] == 1:
#             neighbors.append(v)
#     return neighbors
