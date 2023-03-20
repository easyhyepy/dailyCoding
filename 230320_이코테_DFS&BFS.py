# dfs, bfs: https://www.youtube.com/watch?v=7C9RgOcvkvo&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98

'''
stack = []
stack.append(5)
stack.append(1)
stack.append(2)
stack.append(3)
stack.pop()

print(stack[::-1])#최상단부터
print(stack) #최하단부터




from collections import deque

queue = deque()
queue.append(5)
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()

print(queue)
queue.reverse()
print(queue)





def recursive():
    print('재귀호출')
    recursive()
recursive()
#output Limit reached - 깊이제한 있어서 걍 재귀하면 컴 M 스택 한계



#일반 코테에선, 재귀함수 함수 종료조건 필수
def recursive(i):
    
    #10번쨰 호출시 종료
    if i ==10:
        return
    
    print(i, '번째 재귀에서', i+1, '번쨰 재귀함수 호출')
    
    recursive(i+1)
    
    print(i, '번째 재귀 종료!')
recursive(1)



#재귀적으로 구현한 n!
def factorial(n):
    if n <= 1:      #0!과 1!은 1이므로 
        return 1
    #n = n*factorial(n-1)   #걍 출력시키면 안됨. return임!
    return n*factorial(n-1)

print( factorial(3) )


#유클리드 호제법
def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)
print(gcd(200,300))

##모든 재귀함수는 반복문을 이용하여 동일한 기능 구현O
#재귀함수 vs 반복문 = 유불리






#DFS/BFS 문제풀이

def dfs(x,y):
    
    #주어진 범위 벗어나는 경우 즉시 종료
    if x <= -1 or x >=n or y <= -1 or y >= m:
        return False    #왜지
    
    #현재 노드를 아직 방문하지X
    if graph[x][y] == 0:
        #해당 노드 방문 처리
        graph[x][y] = 1
        
        #상하좌우 위치 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True     #왜지 -현재위치에서 DFS 수행 -> 아래쪽 result에서 ++
    return False


n,m = map(int, input().split())


#2차원 리스트 맵 정보 입력받기
#graph = []
#for i in range(n):
    #graph.append(input())
#이런식으로 하면 문자열로 점근해서 문제생김.
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
print(graph)

result=0    
for i in range(n):
    for j in range(m):
        #print(int(graph[i][j]))
        #현재위치에서 DFS 수행 -> 아 각위치에서 dfs 수행한단 소린가?
        if dfs(i, j) == True:
            result += 1

print()
print(result)



'''


'''
#최대한 안보고 코드 작성 - 분명히 위랑 같은데, 답이 안 나와서 일단 패스..
#dfs를 통해 연결된 노드개수 구하기.
#ㄴ 연결된 == 상하좌우

def dfs(x, y):
    #한계에 도달하면 False 리턴. dfs 재호출x
    if x <= -1 or x >= row or y <= -1 or y >= col:  #내생각엔 col,row인거 같은데.
        return False
    #우리의 대상은 0으로 둘러쌓인 곳 개수 세는 것! 왜 graph라는 멀쩡한 애를 1로 덧씌우나 했네. 어차피 dfs 재호출될떄 좌표 아니까 ㄱㅊ흘걸.
    # 방문 안했으면 했다고 표시 -> 안했으면 
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x, y-1)
        dfs(x, y+1)
        dfs(x-1, y)
        dfs(x+1, y)
        return True     #==0인 부분 하나만임. 이게 만약 아래줄(=if 조건 밖)에 있었으면 0인곳 다 더했을걸..?
    return False

row, col = map( int, input().split() )


cnt=0
graph = []
for i in range(row):
    graph.append( list(map(int, input())) )     ##for j in range(col): 필요없음!!

for i in range(row):
    for j in range(col):
        # 호출해서 True인 곳만, 엮인부분. 다 탐색해서 일정 바운더리가 True로 리턴하기. 나머진 False
        
        if dfs(row, col) == True:    #내생각엔 col,row인거 같은데.
            cnt += 1
print(cnt)
'''
