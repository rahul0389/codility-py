# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    count = [0]*len(A)
    flag =1
    for i in A:
        if i<=len(A):
            count[i-1]= count[i-1] +1
        else:
            return 0
    for i in count:
        if(i!=1):
            return 0
            
    return 1
