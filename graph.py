class Graph:
    def __init__(self, graphtype):
        self.graph_type = graphtype

    def add_edge(self, v1, v2):
        pass

    def get_adjacent_vertices(self, v):
        return list()


class AdjacencyMatrixGraph(Graph):
    def __init__(self, num_vertices, graph_type):
        super(AdjacencyMatrixGraph, self).__init__(graph_type)
        self.num_vertices = num_vertices
        self.adacency_matrix = []
        for i in range(num_vertices):
            self.adacency_matrix.append([0]*num_vertices)

    def add_edge(self, v1, v2):
        if (0 <= v1 < self.num_vertices) and (0 <= v2 < self.num_vertices):
            self.adacency_matrix[v1][v2] = 1
            if self.graph_type == "undirected":
                self.adacency_matrix[v2][v1] = 1

    def get_adjacent_vertices(self, v):
        adjacent = []
        if 0 <= v < self.num_vertices:
            for i in range(self.num_vertices):
                if self.adacency_matrix[v][i] == 1:
                    adjacent.append(i)
        return adjacent


def depth_first_traversal(graph: AdjacencyMatrixGraph, current_vertex, visited: set):
    if current_vertex in visited:
        return
    visited.add(current_vertex)
    list_adjacent = graph.get_adjacent_vertices(current_vertex)
    for vertex in list_adjacent:
        depth_first_traversal(graph, vertex, visited)
    print(current_vertex, "^")


def breadth_first_traversal(graph: AdjacencyMatrixGraph, current_vertex):
    queue = []
    visited = set()
    queue.append(current_vertex)
    while queue:
        vertex = queue.pop(0)
        if vertex in visited:
            continue
        print(vertex, "^")
        visited.add(vertex)
        adjacent = graph.get_adjacent_vertices(vertex)
        for v in adjacent:
            if v not in visited:
                queue.append(v)


if __name__ == '__main__':
    graph = AdjacencyMatrixGraph(6, "undirected")
    graph.add_edge(0, 1)
    graph.add_edge(1, 3)
    graph.add_edge(3, 4)
    graph.add_edge(1, 2)
    graph.add_edge(2, 5)
    graph.add_edge(4, 5)
    depth_first_traversal(graph, 1, set())
    print()
    breadth_first_traversal(graph, 1)
