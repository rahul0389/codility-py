

def solution(X, A):
    # write your code in Python 3.6
    arr = [0]*(X+1)
    count =0
    for i in A:
        if arr[i]==0:
            arr[i]=1
            X =X-1
        if X == 0:
            return count
        count =count+1
        
    return -1
