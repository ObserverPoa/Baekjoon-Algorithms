import sys

vertex_count, edge_count, start_vertex = list(map(int, sys.stdin.readline().split()))

edge_lists = [[] for i in range(vertex_count + 1)]

for i in range(edge_count):
    vertex1, vertex2 = list(map(int, sys.stdin.readline().split()))
    edge_lists[vertex1].append(vertex2)
    edge_lists[vertex2].append(vertex1)

for i in range(len(edge_lists)):
    edge_lists[i] = list(set(edge_lists[i])) # remove duplicated edges
    edge_lists[i].sort()

# DFS
def do_dfs():
    visited = [False for i in range(vertex_count + 1)]

    def dfs(current_vertex):
        print(current_vertex, end=' ')
        visited[current_vertex] = True

        for v in edge_lists[current_vertex]:
            if not visited[v]:
                dfs(v)
        
    dfs(start_vertex)

# BFS
def do_bfs():
    visited = [False for i in range(vertex_count + 1)]
    vertex_queue = [start_vertex]
    visited[start_vertex] = True

    while len(vertex_queue):
        current_vertex = vertex_queue.pop(0)
        print(current_vertex, end=' ')

        for v in edge_lists[current_vertex]:
            if not visited[v]:
                vertex_queue.append(v)
                visited[v] = True

do_dfs()
print()
do_bfs()



