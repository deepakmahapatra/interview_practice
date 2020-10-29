class Graph:
    def __init__(self, graphtype):
        self.graph_type = graphtype

    def add_edge(self, v1, v2):
        pass

    def get_adjacent_vertices(self, v):
        return list()


class AdjacencyMatrixGraph(Graph):
    def __init__(self, num_vertices, graph_type):
        super(Graph, self).__init__(graph_type)
        self.num_vertices = 0
        self.adacency_matrix = [[]]
        for i in range(num_vertices):
            self.adacency_matrix.append([0]*num_vertices)

    def add_edge(self, v1, v2):
        if (0 <=v1 < self.num_vertices) and (0 <=v2<self.num_vertices):
            self.adacency_matrix[v1][v2] = 1
            if self.graph_type == "undirected":
                self.adacency_matrix[v2][v1] = 1

    def get_adjacent_vertices(self, v):
        adjacent = []
        if 0 <= v <self.num_vertices:
            for i in range(self.num_vertices):
                if self.adacency_matrix[v][i] == 1:
                    adjacent.append(i)
        return adjacent
