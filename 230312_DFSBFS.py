'''
https://www.acmicpc.net/problem/1260
N(정점의 개수), M(간선의 개수), V(탐색시작할 정점번호) input으로 받아옴.
M개 줄 - 간선이 연결하는 두 정점의 번호 (간선은 양방향)
-> DFS 결과, BFS 결과 (V부터 방문된 점 순서대로 출력)

<<<<<<< HEAD
풀이 참고
https://chanos.tistory.com/m/entry/%EB%B0%B1%EC%A4%80-1260%EB%B2%88-DFS%EC%99%80-BFS-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4
이해 안 가서 DFSBFS2.py통해서 이해하고 돌아옴. 
오류나는건 input 줘야해서 그럼.
'''

# 인접 행렬로 표현된 그래프에 대해 깊이 우선 탐색 <-> 인접리스트(희소행렬에서 성능 굳)
def DFS(v): 
=======
풀이참고
https://chanos.tistory.com/m/entry/%EB%B0%B1%EC%A4%80-1260%EB%B2%88-DFS%EC%99%80-BFS-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4
'''

# 인접 행렬로 표현된 그래프에 대해 깊이우선탐색 <-> 인접리스트(희소행렬에서 성능 굳)
def DFS(v):
>>>>>>> d97b751fe58dbb5dbe581e00ace470e883779de3
    visited[v]=1        #정점v 방문 표시
    dfs.append(v)       #얜 원래 자구 수업떄 안배움 -> 나중에 방문한 순서대로 출력하려고 따로 저장
    for i in node[v]:   #모든 정점들에 대해 알아봄
        if (visited[i]==0):     #만약 방문하지 않은 인접 정점이면
            DFS(i)              #정점 w에서 DFS 새로 시작

def BFS(v):
    visited[v]=1        #정점v 방문 표시
    bfs.append(v)       #얜 원래 자구 수업떄 안배움 -> 나중에 방문한 순서대로 출력하려고 따로 저장
    queue = [v]         #시작 정점을 큐에 저장

    while (queue):      #방문할 노드가 없을 떄까지. 큐가 empty 상태 아닐 때까지
        for i in node[queue.pop(0)]:
            if(visited[i] == 0):
                visited[i]=1        #방문 표시
                bfs.append(i)
                queue.append(i)     #방문한 정점을 큐에 저장


################## MAIN ##################

N, M, V = map(int, input().split())

node = [ [] for _ in range(N+1) ]
<<<<<<< HEAD
visited = [0] * (N+1)
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
    print(m, end = ' ')

for n in bfs:
    print(n, end = ' ')
=======
visited 
>>>>>>> d97b751fe58dbb5dbe581e00ace470e883779de3
