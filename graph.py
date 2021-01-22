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
    print(current_vertex)
    list_adjacent = graph.get_adjacent_vertices(current_vertex)
    for vertex in list_adjacent:
        depth_first_traversal(graph, vertex, visited)



def depth_first_traversal_non_recursive(graph: AdjacencyMatrixGraph, current_vertex):
    visited = set()
    visited.add(current_vertex)
    adjacent = list()
    adjacent.extend(graph.get_adjacent_vertices(current_vertex))
    print(current_vertex)
    while adjacent:
        temp_node = adjacent.pop()
        if temp_node not in visited:
            adjacent.extend(graph.get_adjacent_vertices(temp_node))
            visited.add(temp_node)
            print(temp_node)



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


def find_num_islands(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                dfs_island_helper(grid, i, j)
                count += 1
    return count

def dfs_island_helper(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j]!=1:
        return
    grid[i][j] = '#'
    dfs_island_helper(grid, i+1, j)
    dfs_island_helper(grid, i, j+1)
    dfs_island_helper(grid, i, j-1)
    dfs_island_helper(grid, i-1, j)

def topological_sort():
    pass


if __name__ == '__main__':
    graph = AdjacencyMatrixGraph(6, "undirected")
    graph.add_edge(0, 1)
    graph.add_edge(1, 3)
    graph.add_edge(3, 4)
    graph.add_edge(1, 2)
    graph.add_edge(2, 5)
    graph.add_edge(4, 5)
    # depth_first_traversal(graph, 1, set())
    print()
    # depth_first_traversal_non_recursive(graph, 1)
    # breadth_first_traversal(graph, 1)
    print(find_num_islands([[1, 1, 0, 0 , 0], [1, 1,  0, 1, 0]]))
    print(find_num_islands([[1, 1, 0, 0 , 0, 0], [1, 1,  0, 1, 0, 0], [1, 1,  0, 1, 0, 1]]))