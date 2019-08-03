def solution(X, A):
    # write your code in Python 3.6
    arr=[0]*X
    flag=0
    for i in range(len(A)):
        arr[A[i]-1]=1
        flag=0
        for j in arr:
            if j==0:
                flag=-1
        if flag==0:
            return i
            
    return flag
