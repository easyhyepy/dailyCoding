#혼자 풀었는데 시간초과 에러
''' 
#전체 거치면서 출력하는 것 성공
testarr = [[11,12,13,14], [22,22,23,24], [31,32,33,34], [41,42,43,44]]

def z(x, y, size):
    
    if (size == 1):
        return ( testarr[x][y] )
    
    
    
    if (size > 1):
        size = size //2
        ul = str( z(x, y, size) )
        ur = str( z(x, y+size, size) )     #y가 열이라서 y먼저
        dl = str( z(x+size, y, size) )
        dr = str( z(x+size, y+size, size) )
        return ul + ur + dl + dr
    
    

#main
N, r, c = str( input() ).split(' ')  
N = int(N)
# print ( drawStar(N) )

#리스트를 문자열로 합치기
print ( z(0,0,N) )
'''




count = 0
def z(x, y, size,r,c):
    
    
    if (size == 1):
        global count        #https://hbase.tistory.com/370.  local variable 'count' referenced before assignment
        count = count +1
        #print(x, y, r, c)
        if (x==r and y==c):     #행, 열은 index와 +-1 관계..라고 생각했는데, 걍 index라고 생각하면 된다네.
            print(count-1)        #return count하니까 안되더라 / 계속 +1만큼 나오던데, 그림보니까 0,0은 0번째 방문이네?
        #return ( testarr[x][y] )
    
    
    
    if (size > 1):
        size = size //2
        ul = str( z(x, y, size,r,c) )
        ur = str( z(x, y+size, size,r,c) )     #y가 열이라서 y먼저
        dl = str( z(x+size, y, size,r,c) )
        dr = str( z(x+size, y+size, size,r,c) )
        #return ul + ur + dl + dr
    
    

#main
N, r, c = map(int, input().split())
N = 2**N

#리스트를 문자열로 합치기
#return (z~~) 인데 위에서 return 받으니 안되더라.
z(0,0,N,r,c) 
