# greedy and 구현: https://www.youtube.com/watch?v=2zjoKjt97vQ&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98
# 보고 이해하면서 따라 침

#현재 나이트 위치 입력받기 - c1 이런식으로 입력
input_data = input()        
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a'))+1

#나이트 이동 가능한 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

#8가지 방향 대하여 각 위치로 이동 가능한지 확인
cnt = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    
    if next_row >=1 and next_row <=8 and next_column >=1 and next_column <=8:
        cnt += 1
        
print(cnt)
