# for문은 끝수가 실행되면 종료

n = int(input())

sum = 1

for i in range(n, 0, -1):
    sum = sum * i

print(sum)

