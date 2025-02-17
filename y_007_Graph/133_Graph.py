class Graph:
    def __init__(self, edge):
        self.edge = edge
        self.graph_dict = {}
        for start, end in self.edge:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print(self.graph_dict)


if __name__ == '__main__':
    routes = [("mumbai", "paris"),
              ("mumbai", "dubai"),
              ("paris", "dubai"),
              ("dubai", "new york"),
              ("paris", "new york"),
              ("new york", "tronto")]

    route_graph = Graph(routes)

    d = {"mumbai": ["paris", "dubai"]}
