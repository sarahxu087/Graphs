from util import Stack, Queue

class Graph:
    def __init__(self):
        self.vertives ={}
    def add_vertex(self,vertex):
        if vertex not in self.vertives:
            self.vertives[vertex] = set()


    def add_edge(self,v1,v2):
        if v1 and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('Vertex does not exist')






def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        graph.add_edge(pair[1],pair[0])


    q = Queue()
    q.enqeue([starting_node])
    max_path_len = 1
    earliest_ancestor = -1
    while q.size()>0:
        path=q.dequeue()
        v = path[-1]
        if(len(path) >= max_path_len and v<earliest_ancestor)or(len(path) > max_path_len):
            earliest_ancestor = v
            max_path_len = len(path)
        for neighbor in graph.add_vertex[v]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)
    return earliest_ancestor