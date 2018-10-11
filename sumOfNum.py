


def getsum(n):
    sum = getRecu(n)
    print(sum)

def getRecu(n):
    if n == 0:
        return 0
    else:
        return n%10 + getRecu(int(n/10))


print(getsum(151))