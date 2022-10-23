import math
from copy import deepcopy


class Graph:
    __adjacency_list = None
    __incidence_matrix = None

    def __init__(self, adjacency_list):
        self.__adjacency_list = deepcopy(adjacency_list)

    @classmethod
    def from_matrix(cls, incidence_matrix):
        cls.__incidence_matrix = incidence_matrix
        return cls(None)

    def __len__(self):
        return len(self.__adjacency_list)

    def size(self):
        return len(self)

    def vertex_degree(self, index):
        if self.__adjacency_list:
            return len(self.__adjacency_list[index])
        else:
            degree = 0
            for i in len(self.__incidence_matrix[index]):
                if self.__incidence_matrix[index][i] != 0:
                    degree += 1
            return degree

    def dfs(self, index):
        graph = self.__adjacency_list
        result = []
        stack = []
        visited = set()

        stack.append(index)

        while len(stack):
            current_index = stack.pop()

            if current_index not in visited:
                visited.add(current_index)
                result.append(current_index)
                for i in range(len(graph[current_index]) - 1, -1, -1):
                    stack.append(graph[current_index][i][0])

        return result

    def bfs(self, index):
        graph = self.__adjacency_list
        result = []
        queue = []
        visited = set()

        queue.append(index)

        while len(queue):
            current_index = queue.pop(0)

            if current_index not in visited:
                visited.add(current_index)
                result.append(current_index)
                for neighbour in graph[current_index]:
                    queue.append(neighbour[0])

        return result

    def dfs_recursive(self, index, visited=None, result=None):
        graph = self.__adjacency_list
        if not result:
            result = []
        if not visited:
            visited = set()

        visited.add(index)
        result.append(index)
        for i in range(len(graph[index])):
            if graph[index][i][0] not in visited:
                self.dfs_recursive(graph[index][i][0], visited, result)

        return result

    def dijkstra(self, start, end):
        graph = self.__adjacency_list
        parents, distances, path, visited = [], [], [], set()
        for i in range(len(graph)):
            parents.append(i)
            distances.append(math.inf)
        distances[start] = 0

        for i in range(len(graph)):
            v = -1
            for j in range(len(graph)):
                if j not in visited and (v == -1 or distances[j] < distances[v]):
                    v = j
            if distances[v] == math.inf:
                break
            visited.add(v)

            for j in range(len(graph[v])):
                to = graph[v][j][0]
                weight = graph[v][j][1]
                if distances[v] + weight < distances[to]:
                    distances[to] = distances[v] + weight
                    parents[to] = v

        length = distances[end]
        path.append(end)
        while end != start:
            end = parents[end]
            path.insert(0, end)

        return length, path

    def prim(self):
        start, end = 0, 0
        graph = self.__adjacency_list
        parents, path, distances, visited = [], [], [], set()
        for i in range(len(graph)):
            parents.append(i)
            distances.append(math.inf)
        distances[start] = 0

        for i in range(len(graph)):
            v = -1
            for j in range(len(graph)):
                if j not in visited and (v == -1 or distances[j] < distances[v]):
                    v = j
            if distances[v] == math.inf:
                break
            visited.add(v)
            print(i, v, distances)

            for j in range(len(graph[v])):
                to = graph[v][j][0]
                weight = graph[v][j][1]
                if distances[v] + weight < distances[to]:
                    distances[to] = weight
                    parents[to] = v
                    end = v

        length = distances[end]
        # path.append(end)
        # while end != start:
        #     end = parents[end]
        #     path.insert(0, end)

        return length, distances

    def floyd_warshall(self):
        graph = self.__incidence_matrix
        n = len(graph)
        distances = [[0] * len(graph) for _ in range(len(graph))]
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                if i != j:
                    distances[i][j] = graph[i][j]

        for k in range(len(distances)):
            for i in range(len(distances)):
                for j in range(len(distances)):
                    if distances[i][k] != 0 and distances[k][j] != 0 and i != j:
                        if distances[i][k] + distances[k][j] < distances[i][j] or distances[i][j] == 0:
                            distances[i][j] = distances[i][k] + distances[k][j]

        return distances








