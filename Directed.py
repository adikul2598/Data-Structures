class Graph:
    def __init__(self, num_nodes, edges, directed=False):
        self.data = [[] for _ in range(num_nodes)]
        self.weight = [[] for _ in range(num_nodes)]

        self.directed = directed
        self.weighted = len(edges) > 0 and len(edges[0]) == 3

        for e in edges:
            self.data[e[0]].append(e[1])
            if self.weighted:
                self.weight[e[0]].append(e[2])

            if not directed:
                self.data[e[1]].append(e[0])
                if self.weighted:
                    self.data[e[1]].append(e[2])

    def __repr__(self):
        result = ""
        for i in range(len(self.data)):
            pairs = list(zip(self.data[i], self.weight[i]))
            result += "{}: {}\n".format(i, pairs)
        return result

    def __str__(self):
        return repr(self)

num_nodes7 = 6
edges7 = [(0, 1, 4), (0, 2, 2), (1, 2, 5), (1, 3, 10), (2, 4, 3), (4, 3, 4), (3, 5, 11)]
num_nodes7, len(edges7)

g7 = Graph(num_nodes7, edges7, directed=True)
