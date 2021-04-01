from Graph import Graph
from Queue import MyQueue
# You can check the input graph in console tab

# Create Queue => queue = MyQueue()
# Functions of Queue => enqueue(int), dequeue(), size(), front(), is_empty()
# Create Stack => stack = MyStack()
# Functions of Stack => push(int), pop(), top(), is_empty() 
# Create Graph => graph = Graph(vertices)
# Create LinkedList => link_list = LinkedList()
# Functions of LinkedList => insert_at_head(Node), is_empty(), delete(),
#                            delete_at_head(list), search(), print_list()
# class Node => data, next_element
# Breadth First Traversal of Graph g from source vertex

def get_children_vertices(graph, vertex):
    children = []
    edge_list = graph.array[vertex]
    if not edge_list.is_empty():
        node = edge_list.head_node
        while node is not None:
            children.append(node.data)
            node = node.next_element
    return children

def bfs_traversal(g, source):
    result = ""
    num_of_vertices = g.num_vertices
    # Write - Your - Code
    # For the above graph, it should return "01234" or "02143" etc

    visited = ""
    expand_queue = MyQueue()
    expand_queue.enqueue(source)
    visited_set = set()

    while not expand_queue.is_empty():
        vertex = expand_queue.dequeue()

        if vertex in visited_set:
            continue
        visited_set.add(vertex)
        
        visited += str(vertex)

        children = get_children_vertices(g, vertex)
        for child in children:
            expand_queue.enqueue(child)

    return visited
