def euler2():
    sum = 0
    currentFib = 1
    lastFib = 0

    while True:
        temp = currentFib
        currentFib += lastFib
        lastFib = temp
        if currentFib % 2 == 0:
            sum += currentFib
        if currentFib > 4000000:
            break

    print(sum)

euler2()
