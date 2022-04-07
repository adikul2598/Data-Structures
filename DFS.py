# Adjaceny Matrix
class Graph:
    def __init__(self, num_nodes, edges):
        self.data = [[] for _ in range(num_nodes)]
        for v1, v2 in edges:
            self.data[v1].append(v2)
            self.data[v2].append(v1)

    def __repr__(self):
        return "\n".join(["{} : {}".format(i, neighbors) for (i, neighbors) in enumerate(self.data)])

    def __str__(self):
        return repr(self)


def dfs(graph, source):
    visited = [False] * len(graph.data)
    stack = [source]
    result = []

    while len(stack) > 0:
        current = stack.pop()
        if not visited[current]:
            result.append(current)
            visited[current] = True
            for v in graph.data[current]:
                stack.append(v)

    return result

num_nodes1 = 5
edges1 = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (1, 4), (1, 3)]
num_nodes1, len(edges1)

g1 = Graph(num_nodes1, edges1)

dfs(g1, 0)
