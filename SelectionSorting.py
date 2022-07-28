import sys
A = [100, 420, 69, 21, 23442]
 
# Search all elements
for i in range(len(A)):
  
 # Find the minimum element
 minimumIdex = i
 for j in range(i+1, len(A)):
  if A[minimumIdex] > A[j]:
   minimumIdex = j
    
 # Swap the minimum element with first element  
 A[i], A[minimumIdex] = A[minimumIdex], A[i]
 
print(A)