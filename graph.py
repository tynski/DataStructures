class Vertex(object):
    def __init__(self, node):
        self.id = node
        self.neighbours = {}
    
    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x for x in self.neighbours])

    def add_neighbour(self, node, weight):
        self.neighbours[node] = weight
    
class Graph(object):
    def __init__(self):
        self.vert_dict = {}

    def add_vertex(self, node):
        self.vert_dict[node] = Vertex(node)
    
    def add_edge(self, frm, to, weight):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)
        
        self.vert_dict[frm].add_neighbour(to, weight)
        self.vert_dict[to].add_neighbour(frm, weight)
    
    def get_weight(self, frm, to):
        return self.vert_dict[frm].neighbours[to]

g = Graph()

g.add_vertex('a')
g.add_vertex('b')
g.add_vertex('c')
g.add_vertex('d')
g.add_vertex('e')
g.add_vertex('f')

g.add_edge('a', 'b', 7)  
g.add_edge('a', 'c', 9)
g.add_edge('a', 'f', 14)
g.add_edge('b', 'c', 10)
g.add_edge('b', 'd', 15)
g.add_edge('c', 'd', 11)
g.add_edge('c', 'f', 2)
g.add_edge('d', 'e', 6)
g.add_edge('e', 'f', 9)

for (k, v) in g.vert_dict.items():
    print(v)

print(g.get_weight('d', 'e'))