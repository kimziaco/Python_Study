def dfs(graph, v, visited):
    visited[v] = True #현재노드를 방문처리
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

#그래프리스트에서 노드1부터 시작할 경우 0번 인덱스를 비워주고 시작하는 것이 메모리에 더 효율적
#또한 인접한 노드번호를 함께 리스트에 넣어준다.
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False] * 9
#인덱스[0]은 사용하지 않기 위해서 일부로 1더 큰 수로 삼았다

dfs(graph, 1, visited)
