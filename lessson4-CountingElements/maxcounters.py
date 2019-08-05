def solution(N, A):
    # write your code in Python 3.6
    maxcounter=0
    result=[0]*N
    for i in A:
        if i <=N:
            result[i-1]= result[i-1]+1
            if maxcounter<result[i-1]:
                maxcounter=result[i-1]
        else:
            if i==N+1:
                result=[maxcounter]*N
    return result            
