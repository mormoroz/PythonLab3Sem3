def printTriangleString(rows):
    row = [1]
    for i in range(rows):
        print(" ".join(list(map(str, row))))
        row = [sum(x) for x in zip([0]+row, row+[0])]

n = 0
while True:
    try:
        print("Input number of lines of Pascal's triangle: ")
        n = int(input())
        if n > 0: break
        print('Wrong input')
    except:
        print('Wrong input')
printTriangleString(n)