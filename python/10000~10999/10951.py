while True:
    try:
        a, b = map(int, input().split())
    except: # 에러 발생시 실행 코드
        break
    print(a+b)