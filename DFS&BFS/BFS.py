from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    
    visited[start] = True

    while queue: #큐가 비어있지 않다면 반복적으로 실행!
        v = queue.popleft() #큐는 방문후 없애고 실행을 계속한다.
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9
bfs(graph,1,visited)

