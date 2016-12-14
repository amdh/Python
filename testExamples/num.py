
def checkEqual(lst):
   return lst[1:] == lst[:-1]

def incrOthers(index,nums):
    for i in xrange(len(nums)):
        if(i == index):
            continue
        else:
            val = nums[i]
            val+=1
            nums[i] =val

def  countMoves(numbers):
    counter = 1;
    index= 0;
    l = len(numbers)
    while(True):
        m_val = max(numbers)
        print m_val
        index = numbers.index(m_val)
        incrOthers(index,numbers)
        if (checkEqual(numbers)):
            break
        else:
            counter+=1
        print index


    print "counter %d" %counter

numbers = [2,3,3,4]
countMoves(numbers)