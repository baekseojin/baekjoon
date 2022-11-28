# 26 -> 68 -> 84 -> 42 -> 26 (4번)

n = int(input()) # 26
count=0

if(n<10): a = n*11
b = n
while True:
    a = (int((b%100 - b%10)/10)) + b%10 
    b = (b%10)*10 + a
    count += 1
    if(b==n): break

print(count)