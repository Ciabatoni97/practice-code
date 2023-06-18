#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    minsum = arr[0]+arr[1]+arr[2]+arr[3]
    maxsum = arr[-1]+arr[-2]+arr[-3]+arr[-4]
    
    print(minsum,maxsum)
    

if __name__ == '__main__':
    print("Please enter a series of numbers seperated by spaces")

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
