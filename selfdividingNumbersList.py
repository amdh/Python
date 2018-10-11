
def getDigits( num):
    digits = []
    while num > 0:
        digit = num%10
        num = int(num/10)
        print(digit)
        if digit !=0 :
            digits.append(digit)
        else:
            return 0


    return digits

def getSelfDivingNum(num):

    digits = getDigits(num)

    if digits == 0:
        print("no self dividing");
        return False

    for  i in digits:
        if num%i ==0:
            continue
        else:
            print("no self dividing");
            return False

    return True


def getListSelfDividingNum(left, right):

    result = []
    for i in range(left,right):
        if getSelfDivingNum(i):
            result.append(i)

    print(result)


getListSelfDividingNum(9,13)