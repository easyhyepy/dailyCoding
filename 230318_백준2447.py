#참고: https://lucian-blog.tistory.com/57
#거의 정답보고 베낀 수준.


def drawStar (size):
    if size == 1:
        return ['*']  #배열에 넣는거라 []
    
    
    star = drawStar(size//3)  #@@@ 재귀. 이해안됨.
    arr = []
    
    for i in star:
        arr.append( i * 3 )
    for i in star:
        arr.append( i + ' '*(size//3) + i )  #단순히 ' '은 아님!!
    for i in star:
        arr.append( i * 3 )
        
    return arr
    



#main
N = int(input())
# print ( drawStar(N) )

#리스트를 문자열로 합치기
print ( "\n".join(  drawStar(N)  ))
