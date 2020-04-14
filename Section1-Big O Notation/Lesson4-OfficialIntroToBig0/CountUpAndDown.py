def countUpAndDown(n):
    print('Going Up')
    for i in range(1, n + 1):
        print(i)
    print('Going Down')
    for j in range(n, -1, -1):
        print(j)
    print('Back Down')


countUpAndDown(10)