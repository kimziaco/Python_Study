from collections import deque

N, M, V = map(int, input().split())

graph = [[0] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    m1, m2 = map(int, input().split())
    graph[m1][m2] = graph[m2][m1] = 1


def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in range(1, N+1):
        if not visited[i] and graph[v][i] == 1:
            dfs(i)


def bfs(v):
    queue = [v]
    visited[v] = False
    while queue:
        v = queue.pop(0)
        print(v, end=' ')
        for i in range(1, N+1):
            if visited[i] and graph[v][i] == 1:
                queue.append(i)
                visited[i] = False


dfs(V)
print()
bfs(V)
