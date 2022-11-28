a,b,c,d = map(int, input().split())
e,f,g,h = map(int, input().split())

minguk = a+b+c+d
manse = e+f+g+h

if(minguk>=manse):
    print(minguk)
else:
    print(manse)