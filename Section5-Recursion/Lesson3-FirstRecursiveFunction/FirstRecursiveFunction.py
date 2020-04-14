def countDown(num):
    if num <= 0:
        print('All Done')
        return
    print(num)
    countDown(num - 1)

countDown(17)