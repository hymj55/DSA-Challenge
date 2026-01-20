from collections import deque

vertexData = ['A', 'B', 'C', 'D']

adjacency_matrix = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 0],
    [1, 0, 0, 0]
]

def print_adjacency_matrix(matrix):
    print("\nAdjacency Matrix:")
    for row in matrix:
        print(row)

def print_connections(matrix, vertices):
    print("\nConnections for each vertex:")
    for i in range(len(vertices)):
        print(f"{vertices[i]}: ", end="")       # i = 0
        for j in range(len(vertices)):          # j = 0, 1, 2, 3
            if matrix[i][j]:                    # matrix[0][0], matrix[0][1], matrix[0][2], matrix[0][3]
                print(vertices[j], end=" ")     # In Python, 0은 False, 0이 아닌 모든숫자(값) True
        print()



# distances = [float('inf')] * 5
# print(distances)



# print('vertexData:', vertexData)
# print_adjacency_matrix(adjacency_matrix)
# print_connections(adjacency_matrix, vertexData)
#
queue1 = deque()
print(queue1)

queue2 = deque([1,2])
print(queue2.popleft())

