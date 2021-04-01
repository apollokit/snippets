from Graph import Graph
from Queue import MyQueue
from Stack import MyStack

def get_children_vertices(graph, vertex):
    children = []
    edge_list = graph.array[vertex]
    if not edge_list.is_empty():
        node = edge_list.head_node
        while node is not None:
            children.append(node.data)
            node = node.next_element
    return children

def dfs_traversal(g, source):
    result = ""
    num_of_vertices = g.num_vertices
    # Write - Your - Code
    # For the above graph, it should return "01234" or "02143" etc

    visited = ""
    expand_queue = MyStack()
    nodes = range(g.num_vertices)
    for child in nodes:
        expand_queue.push(child)
    expand_queue.push(source)
    visited_set = set()

    while not expand_queue.is_empty():
        vertex = expand_queue.pop()

        if vertex in visited_set:
            continue
        visited_set.add(vertex)
        
        visited += str(vertex)

        children = get_children_vertices(g, vertex)
        print("vertex")
        print(vertex)
        print("children")
        print(children)
        for child in children:
            expand_queue.push(child)

    return visited