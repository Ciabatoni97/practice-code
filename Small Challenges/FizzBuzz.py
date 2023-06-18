#!/bin/python3


def fizzBuzz(n):
    # Write your code here
    for i in range(1,n+1):
        if i % 3 and i % 5:
            print(i)
        elif i % 3 and i % 5 == False:
            print("Buzz")
        elif i % 3 == False and i % 5:
            print("Fizz")
        else:
            print("FizzBuzz")

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
