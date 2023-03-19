#참고: https://leejunggae.tistory.com/10
cnt = 0
def hanoi(n, src, dst, tmp):        #src, dst, tmp 필요하다고 함.
    global cnt
    if (n==1):
        print(src, dst)
        return
        
    hanoi(n-1, src, tmp, dst)
    print(src, dst)
    hanoi(n-1, tmp, dst, src)

    

n=int(input())
print(2**n-1)   #하노이 이동횟수 
hanoi(n, 1, 3, 2)
