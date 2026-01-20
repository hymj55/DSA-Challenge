class Graph:

    def __init__(self):
        self.vertices = []
        self.adj_matrix = []
        self.vertex_data_map = {}

    def get_vertex_index(self, data):
        try:
            return self.vertices.index(data)
        except ValueError:
            return -1

    def add_vertex(self, data):
        new_index = len(self.vertices)
        self.vertices.append(data)

        self.vertex_data_map[new_index] = data

        for row in self.adj_matrix:             # Add a new column to the existing row
            row.append(0)

        new_row = [0]*(new_index+1)             # Add a new row  # No connections yet, so all values are 0
        self.adj_matrix.append(new_row)

        print(f"Added vertex {data} to vertex index {new_index}")

    def add_vertex_data(self, vertex_data, label):
        """
        vertex_data_map에서 기존 data값을 label로 교체하기 위한 함수
        기존 vertex data를 새 값(label)로 업데이트하는 것
        """
        vertex_index = self.get_vertex_index(vertex_data)
        if vertex_index == -1:
            print(f"Error: vertex {vertex_data} not found in graph")
            return

        self.vertex_data_map[vertex_index] = label
        print(f"updated data for vertex {vertex_data} (index {vertex_index}) with label {label}")

    def add_edge(self, source_data, destination_data):
        source_index = self.get_vertex_index(source_data)
        destination_index = self.get_vertex_index(destination_data)

        if source_index == -1 or destination_index == -1:
            print("Error one or both vertices not found in graph")
            return

        self.adj_matrix[source_index][destination_index] = 1
        self.adj_matrix[destination_index][source_index] = 1

        print(f"Added edge between vertex {source_data} and vertex {destination_data}")

    def display_matrix(self):
        print("\nAdjacency Matrix (Undirected graph)")
        header = [""] + self.vertices
        print()
        print("-"*(len(header)*5))

        for i, vertex_data in enumerate(self.vertices):
            row_output = [vertex_data] + [str(val) for val in self.adj_matrix[i]]
            print("---------------------------")

        print("\n-----Vertex Data/ Labels--------")
        for index, data in self.vertex_data_map.items():
            print(f"vertex {self.vertices[index]} (index {index}): {data}")





my_graph = Graph()
my_graph.add_vertex('A')
print(my_graph.get_vertex_index('A'))
my_graph.add_vertex('B')
print(my_graph.get_vertex_index('B'))
my_graph.add_vertex('C')

for row in my_graph.adj_matrix:
    print(row)

print(my_graph.vertex_data_map)

print(my_graph.vertex_data_map[1])

my_graph.add_vertex_data('B','Conestoga')
print(my_graph.vertex_data_map)


my_graph.add_edge('A','B')
my_graph.add_edge('A','C')



my_graph.display_matrix()

print()
print("my_graph.vertices",my_graph.vertices)

print()
print("my_graph.adj_matrix",my_graph.adj_matrix)

print()
print("my_graph.vertex_data_map",my_graph.vertex_data_map)