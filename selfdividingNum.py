
def getDigits( num):
    digits = []
    while num > 0:
        digit = num%10
        num = int(num/10)
        print(digit)
        if digit !=0 :
            digits.append(digit)


    return digits

def getSelfDivingNum(num):

    digits = getDigits(num)

    for  i in digits:
        if num%i ==0:
            continue
        else:
            print("no self dividing");
            break;


getSelfDivingNum(51)