def countDividers(n):
    r = 0
    i = 1
    while i*i <= n:
        if n % i == 0:
            if (n // i != i): r += 2
            else: r += 1
        i += 1
    return r
def findNumsWithDoubleDividers(a, b):
    nums = []
    for i in range(a, b+1):
        countInputDividers = countDividers(i)
        if countInputDividers == 2:
            nums.append(i)
    return tuple(nums)

a = b = 0

while True:
    try:
        print("Input distance: ")
        a, b = list(map(int, input().split()))
        break
    except:
        print('Wrong input')

print(findNumsWithDoubleDividers(a, b))
