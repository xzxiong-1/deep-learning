def split_sort(A):
    if len(A) == 0:
        return 0
    j = 0
    for i in range(len(A)):
        if A[i] > A[j]:
            temp = A[i]
            A[i+1] = temp
            A[i] = A[i+1]
            j += 1
    return A

A = [2, 1, 4, 7, 8, 5, 0]
B = split_sort(A)
print(B)
            
            