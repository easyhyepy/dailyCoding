'''
https://www.acmicpc.net/problem/1260
N(정점의 개수), M(간선의 개수), V(탐색시작할 정점번호) input으로 받아옴.
M개 줄 - 간선이 연결하는 두 정점의 번호 (간선은 양방향)
-> DFS 결과, BFS 결과 (V부터 방문된 점 순서대로 출력)

풀이 참고
https://chanos.tistory.com/m/entry/%EB%B0%B1%EC%A4%80-1260%EB%B2%88-DFS%EC%99%80-BFS-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4
이해 안 가서 DFSBFS2.py통해서 이해하고 돌아옴. 
오류나는건 input 줘야해서 그럼.
'''

def DFS(v):
    visited[v]=1
    dfs.append(v)
    for i in node[v]:
        if (visited[i]==0):
            DFS(i)

def BFS(v):
    visited[v]=1
    bfs.append(v)
    queue = [v]

    while(queue):
        for i in node[queue.pop(0)]:
            if(visited[i]==0):
                visited[i]=1
                bfs.append(i)
                queue.append(i)
##################MAIN##################
N, M, V = map(int, input().split())

node =[[]for _ in range(N+1)]
visited = [0]*(N+1)
dfs = []
bfs = []

for i in range(M):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

for j in range(N+1):
    node[j].sort()

DFS(V)
for j in range(N+1):
    visited[j]=0
BFS(V)

for m in dfs:
    print(m, end=' ')
print()
for n in bfs:
    print(n, end=' ')