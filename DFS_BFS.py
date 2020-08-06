# DFS algorithm in Python


# DFS algorithm
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start]:
        if next not in visited:
            dfs(graph, next, visited)
    return visited



def bfs(graph, start):
    if start is None:
        return
    queue = []
    visited = set()
    queue.append(start)
    visited.add(start)
    while queue:
        output = queue.pop(0)
        print(output, end=" ")
        for i in graph[output]:

            if i not in visited:
                queue.append(i)
                visited.add(i)
            

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

print('DFS:')
dfs(graph, 'C')
print('BFS: ')
bfs(graph, 'A')
print()
