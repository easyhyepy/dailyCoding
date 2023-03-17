N = int(input())
arr = []
for i in range(N):
    arr.append( (input()) )
#M[0][1]로 접근

def quad(arr, x, y, size):
    #전체가 같은 숫자인가 -> 반복문으로 모든 원소들에 대해 검사
    for j in range(size):
        for k in range(size):
            # !=이라고 해야함.첫원소(x,y)예를들어 0,0이 0,1 0,2 ... 등과 같다(==)라고 하면 안된다. 다 확인 하는게 아니라, 처음으로 같은 순간에 (리턴)출력해서;;
            if ( arr[x][y] != arr[x+k][y+j] ):   
    
    #전체가 같지X -> 분할해가면서 같은지
            
                #사이즈 반으로 쪼개고 / 마지막으로 원소 1개 남는 경우
                # 연산자 '/'와 '//'의 차이. / 는 나눗셈을 의미하며 결과가 float 로 나타납니다. // 는 나눗셈을 의미하며 결과가 int 로 나타납니다.
                size = size // 2
                
                if (size >  0):             #@@@ size>1이면 안됨. 만약 size==1일때, ul~dr 코드 실행 -> 전체가 같은 숫자인지 확인시, arr[x][y]==arr[x+0][x+y]함 
                    ul = str ( quad(arr, x, y, size) )
                    ur = str ( quad(arr, x, y+size, size) )     #@@@ 아래랑 순서 바뀌었음. y먼저. ∵ y가 열임. 1행1열 -> 1행2,3,4열 순서여서! 이중for문의 밖은 행/ 안은 열.
                    dl = str ( quad(arr, x+size, y, size) )
                    dr = str ( quad(arr, x+size, y+size, size) )
                    return '(' + ul + ur + dl + dr + ')' 
                    
            #@@@ 전체가 다 같을 때 리턴 - 마지막에 이거 안넣어서 안떴음. 근데 tap 위치가 왜 저기지. 여기에 ( 넣으면 안됨
            # 전체가 같은 경우! 하나씩 리턴하고 -> 그 젤작은 경우 바닥찍고 -> 아래서 위로 되돌아가듯이 가서 -> return ( ~~ ) 찍히는가보다.
    return arr[x][y] 
   
   
            
#호출 -> 배열과 시작x좌표
print ( quad(arr, 0, 0, N) )
