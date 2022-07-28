def Sort(A):
    n = len(A)

    swapped = False

    for i in range(n-1):

        for j in range(0, n-i-1):
 
            if A[j] > A[j + 1]:
                swapped = True
                A[j], A[j + 1] = A[j + 1], A[j]
         
        if not swapped:
            return
 
 
A = [64, 34, 25, 12, 22, 11, 90]
 
Sort(A)

print(A)