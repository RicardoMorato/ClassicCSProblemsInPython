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

visited = set() # set to keep track of which nodes already been visied

def dfs(visited, graph, node):
    if node not in visited:
        print(f'Visitting node {node}')
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)

if __name__ == "__main__":
    dfs(visited, graph, 'B')
    dfs(visited, graph2, 1)