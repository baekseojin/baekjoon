# 가장 큰 약수와 가장 작은 약수를 구하면 N을 구할 수 있다
n = int(input())
num_list = list(map(int, input().split()))

a = min(num_list)
b = max(num_list)

print(a*b)
