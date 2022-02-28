A = [89, 80, 67, 54, 86, 3, 2, 5]

for i in range(len(A) - 2):
    lowest = None
    for j in range(i, len(A) - 1):
        key = A[j]
        if lowest is None or lowest[0] > key:
            lowest = (key, j)

    A[i], A[lowest[1]] = lowest[0], A[i]

print (A)