#!/bin/python3

# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    for x in arr:
        if x > 0:
            pos = pos+1
        elif x < 0:
            neg = neg + 1
        else:
            zero = zero +1
    print("You have this ratio of positive numbers: "f'{(pos/len(arr)):.6f}')
    print("You have this ratio of negative numbers: "f'{(neg/len(arr)):.6f}')
    print("You have this ration of zeros: "f'{(zero/len(arr)):6f}')
    
if __name__ == '__main__':

    print("Please enter a series of integers seperated by spaces: ")

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
