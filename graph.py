class Graph:
    def __init__(self):
        self.adjacent_list={}
    def add_vertex(self,vertex):
        if vertex not in self.adjacent_list.keys():
            self.adjacent_list[vertex]=[]
            return True
        return False
    def print_graph(self):
        for vertex in self.adjacent_list:
            print(vertex,":",self.adjacent_list[vertex])

    def addedge(self,vertex1,vertex2):
        if vertex1 in self.adjacent_list.keys() and vertex2 in self.adjacent_list.keys():
            self.adjacent_list[vertex1].append(vertex2)
            return True
        return False
    def removevertex(self,vertex):
        if vertex in self.adjacent_list.keys():
            for other_vertex in self.adjacent_list:
                self.adjacent_list[other_vertex] = [v for v in self.adjacent_list[other_vertex] if v != vertex]
            del self.adjacent_list[vertex]
            return True
        
        return False






mygraph=Graph()
mygraph.add_vertex("A")
mygraph.add_vertex("B")
mygraph.add_vertex("C")
mygraph.add_vertex("D")
mygraph.add_vertex("E")

mygraph.addedge("A","B")
mygraph.addedge("A","C")
mygraph.addedge("A","D")
mygraph.addedge("B","A")
mygraph.addedge("B","E")
mygraph.addedge("D","A")
mygraph.addedge("D","C")
mygraph.addedge("D","E")
mygraph.addedge("E","B")
mygraph.addedge("E","D")
mygraph.addedge("C","A")
mygraph.addedge("C","D")
mygraph.removevertex("E")
mygraph.print_graph()
