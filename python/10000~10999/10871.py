n, x = map(int, input().split())

N_list = list(map(int, input().split()))
for i in N_list(0, n+1):
    if(x>i):
        print(i, end=" ")
