def findIntersections(*params):
    params = list(params)
    for i in range(len(params)): params[i] = set(params[i])

    intersections = params[0]

    for i in range(1, len(params)):
        intersections = intersections.intersection(params[i])

    if len(intersections) == 0: result = "NULL"
    else: result = list(intersections)

    return result

a = [1, 2, 3, 4, 5]
b = [2, 3]
c = [5, 6, 7]

print(findIntersections(a, b, c))
print(findIntersections(a, b))
print(findIntersections(b, c))
print(findIntersections(a, c))
