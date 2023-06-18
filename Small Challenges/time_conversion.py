#!/bin/python3
from datetime import datetime

def timeConversion(s):
    
    return datetime.strptime(s, '%I:%M:%S%p').strftime('%H:%M:%S')
    
if __name__ == '__main__':
    
    print("Please enter the time in 12hr format ex: 07:05:45PM ")
    s = input()

    #Expecting input format similar to > 07:05:45PM

    result = timeConversion(s)

    print(result)
