def solution(A):
    # write your code in Python 3.6
    setA = set(A)
    
    for i in range(1,len(A)+1):
        if i not in setA:
            return i
    else:
        return i+1
        
