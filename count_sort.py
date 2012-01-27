#!/usr/bin/python3
'''
Created on 2012-01-26

@author: kevin
'''
def get_max_item(A):
    the_max = 0
    for i in A:
        if i > the_max: the_max = i
    return the_max

def count_sort(A, k):
    C = [0] * k
    # count all the elements
    for i in A:
        C[i] = C[i]+1
    # create a range of indexes
    for i in range(1,k):
        C[i] = C[i] + C[i-1]
    B = list(A)
    # populate the values to their proper indexes
    for i in range(len(A)-1,0,-1):
        C[B[i]] = C[B[i]]-1
        A[C[B[i]]] = B[i]
    return A

def main():
    size = eval(input("Enter the size of your array: "))
    a = []
    for i in range(size):
        a.append(eval(input("["+repr(i)+"]: ")))
    k = get_max_item(a) + 1
    a = count_sort(a,k)
    print(a)

if __name__ == "__main__": main()