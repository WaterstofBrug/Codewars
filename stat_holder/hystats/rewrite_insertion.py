A = [45, 67, 9, 23, 0, 16, 99]

for j, key in enumerate(A):
    i = j - 1

    while i >= 0 and A[i] < key:
        A[i + 1] = A[i]
        i -= 1

    A[i + 1] = key

print(A)