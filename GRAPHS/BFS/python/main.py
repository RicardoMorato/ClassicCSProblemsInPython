#implementation of a DFS algorithm using recursion for tracking the graph
# made of an adjacency list

graph = {
    'B' : ['D','E'],
    'D' : ['F', 'A'],
    'E' : ['C'],
    'F' : [],
    'A' : ['C'],
    'C' : []
}

graph2 = {
    1 : [3,2],
    2 : [1,3,4],
    3 : [6],
    4 : [5],
    5 : [6],
    6 : []
}

visited = set() # set to keep track of which nodes already been visited

visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
    visited.append(node)
    queue.append(node)

    while queue:          # Creating loop to visit each node
        m = queue.pop(0)
        print (m, end = " ")

    for neighbor in graph[m]:
        if neighbor not in visited:
            visited.append(neighbor)
            queue.append(neighbor)


if __name__ == "__main__":
    bfs(visited, graph, 'B')
    bfs(visited, graph2, 1)