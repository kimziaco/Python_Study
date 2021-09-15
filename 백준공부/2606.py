N = int(input())
M = int(input())
cnt = 0

graph = [[0] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    m1, m2 = map(int, input().split())
    graph[m1][m2] = graph[m2][m1] = 1


def dfs(v):
    visited[v] = True
    global cnt
    cnt += 1
    for i in range(1, N+1):
        if not visited[i] and graph[v][i] == 1:
            dfs(i)


dfs(1)
print(cnt - 1)
