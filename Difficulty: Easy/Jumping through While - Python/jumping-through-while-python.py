def printIncreasingPower(x):
    count = 1
    while count**2 <= x:
        print(count**2, end = " ")
        count += 1