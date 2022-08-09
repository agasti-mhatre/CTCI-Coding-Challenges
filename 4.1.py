class Stack:
    def __init__(self, nodes = []):
            if len(nodes) == 0:
                self._stack = []
            else:
                for node in nodes:
                    self.push(node)

    
    def push(self, node):
        self._stack.append(node)

    
    def pop(self):
        return self._stack.pop()


    def isEmpty(self):
        if len(self._stack) == 0:
            return True
        else:
            return False


class DirectedAdjacencyGraph:
    def __init__(self, edges = []):
        if len(edges) == 0:
            raise Exception("The graph needs edges!")
        else:
            self._edges = dict()

            for start, end in edges:                
                if start in self._edges:
                    self._edges[start].append(end)
                else:
                    self._edges[start] = list()
                    self._edges[start].append(end)

                    

def DFS(graph, start, end):
    nbr_stack = Stack()
    visited = dict()
    path = ""

    nbr_stack.push(start)
    
    while not(nbr_stack.isEmpty()):
        temp = nbr_stack.pop()
        visited[temp] = temp


        if temp in graph._edges:
            for neighbor in graph._edges[temp]:
                if neighbor in visited:
                    continue
                else:
                    nbr_stack.push(neighbor)

        if (start in visited) and (end in visited):
            return "Path found between nodes {} and {}.".format(start, end)


    return "Path not found between nodes {} and {}.".format(start, end)



if __name__ == "__main__":
    edges = [
            ('S', 'B'),
            ('S', 'A'), 
            ('A', 'C'), 
            ('A', 'B'), 
            ('A', 'D'), 
            ('D', 'E')
            ]

    graph = DirectedAdjacencyGraph(edges)
    
    print(DFS(graph, 'D', 'B'))