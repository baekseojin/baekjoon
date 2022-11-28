a = int(input())
b = int(input())

first = b%10
print(a*first)

second = b%100 - first
print(int(a*second/10))

third = b - (second+first)
print(int(a*third/100))

print(a*b)