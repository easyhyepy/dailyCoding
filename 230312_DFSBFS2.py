#https://daekyoulibrary.tistory.com/entry/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9D%84-%ED%86%B5%ED%95%B4-%EA%B5%AC%ED%98%84%ED%95%9C-DFS%EC%99%80-BFS

## DFS ##

#방문 정보를 리스트 자료형으로 표현
visited = [False] * 9

#각 노드가 연결된 정보를 리스트 자료형으로 표현
graph = [
 [],        # 1번 노드와 연결된 노드들
 [2, 3, 8], # 2번 노드와 연결된 노드들
 [1, 7],    # 3번 노드와 연결된 노드들
 [1, 4, 5], # 4번 노드와 연결된 노드들
 [3, 5],    # 5번 노드와 연결된 노드들
 [3, 4],    # 6번 노드와 연결된 노드들
 [7],       # 7번 노드와 연결된 노드들
 [2, 6, 8], # 8번 노드와 연결된 노드들
 [1, 7]     # 9번 노드와 연결된 노드들
]

def DFS (graph, v, visited):        #그래프(그림), 시작노드, 방문관리리스트
    #현재 노드를 방문 처리
    visited[v] = True               

    #노드 출력
    print(v, end = ' ')             

    for i in graph[v]:

        #방문하지 않았으면
        if not visited[i]:  

            #재귀 -> 타고타고 DFS        
            DFS(graph, i, visited)  


## main ##
DFS(graph, 1, visited)


##################################################################

## BFS ##
from collections import deque

#BFS
def BFS(graph, start, visited):
    #queue 구현을 위해 deque lib 사용
    queue = deque([start])

    #현재노드 방문 처리
    visited[start] = True

    #큐가 빌 때까지 반복
    while queue:
        #큐에서 하나 원소 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')

        #해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited = [False] * 9

#각 노드가 연결된 정보를 리스트 자료형으로 표현
graph = [
 [],        # 1번 노드와 연결된 노드들
 [2, 3, 8], # 2번 노드와 연결된 노드들
 [1, 7],    # 3번 노드와 연결된 노드들
 [1, 4, 5], # 4번 노드와 연결된 노드들
 [3, 5],    # 5번 노드와 연결된 노드들
 [3, 4],    # 6번 노드와 연결된 노드들
 [7],       # 7번 노드와 연결된 노드들
 [2, 6, 8], # 8번 노드와 연결된 노드들
 [1, 7]     # 9번 노드와 연결된 노드들
]

print()
BFS(graph, 1, visited)
