n, x = map(int, input().split())

N_list = list(map(int, input().split()))
for i in range(n):
    if(N_list[i]<x):
        print(N_list[i], end=" ")
