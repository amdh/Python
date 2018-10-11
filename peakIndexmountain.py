

def findPeak(arr):

    curr = 1
    index = 0
    if len(arr) < 3:
        return 0

    for i in range(1,len(arr)):
        j = i-1
        if arr[j] > arr[i]:

            if curr > index:
                index = curr
                curr = 0
        else:
            curr = curr + 1
        print(curr, index)

    if curr > index:
        return curr
    else:
        return index

print(findPeak([1,2,3,0,4,5,6,7,8,0,1]))