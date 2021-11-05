def isMono(arr):
    result = True
    for i in range(len(arr)-1):
        if arr[i + 1] < arr[i]:
            result = False
    return result

print("Enter array: ", end='')
while True:
    try:
        userArr = list(map(int, input().split()))
        break
    except:
        print('Please, enter correct list: ', end='')

print(isMono(userArr))
