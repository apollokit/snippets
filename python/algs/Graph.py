# from https://www.educative.io/courses/data-structures-coding-interviews-python/qVl6g4PWYEk

import numpy as np

from LinkedList import LinkedList


class Graph:
    """describes a directed or undirected graph"""

    def __init__(self, vertices):
        # Total number of vertices
        self.num_vertices = vertices
        # definining a list which can hold multiple LinkedLists
        # equal to the number of vertices in the graph
        self.array = []
        # Creating a new Linked List for each vertex/index of the list
        for i in range(vertices):
            temp = LinkedList()
            self.array.append(temp)

    # Function to add an edge from source to destination
    def add_edge(self, source, destination):
        if (source < self.num_vertices and destination < self.num_vertices):
        # As we are implementing a directed graph, (1,0) is not equal to (0,1)
            self.array[source].insert_at_head(destination)

        # If we were to implement an Undirected Graph i.e (1,0) == (0,1)
        # We would create an edge from destination towards source as well
        # i.e self.list[destination].insertAtHead(source)

    def print_graph(self):
        print(">>Adjacency List of Directed Graph<<")
        print
        for i in range(self.num_vertices):
            print("|", i, end=" | => ")
            temp = self.array[i].get_head()
            while(temp is not None):
                print("[", temp.data, end=" ] -> ")
                temp = temp.next_element
            print("None")

    def to_adjacency_mat(self) -> np.ndarray:
        """Get an adjacency matrix describing the graph
        
        see: https://en.wikipedia.org/wiki/Adjacency_matrix
        
        Returns:
            adjacency matrix
        """
        adj_mat = np.zeros((len(self.array), len(self.array)), dtype=np.int8)
        for ivertex in range(self.num_vertices):
            connected_vertex = self.array[ivertex].get_head()
            while(connected_vertex is not None):
                # note it's bi-directional, so the direction of the arrow
                # matters
                adj_mat[ivertex, connected_vertex.data] = 1
                connected_vertex = connected_vertex.next_element
        return adj_mat

if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(1, 4)
    g.add_edge(3, 2)
    g.add_edge(4, 3)

    g.print_graph()
    print(g.to_adjacency_mat())