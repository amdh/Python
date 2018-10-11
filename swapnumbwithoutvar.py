
def swap3(a,b):

    print(a,b)
    a = a ^ b
    b = a^b
    a = a^b

    print(a,b)



def swap2(a,b):

    print(a,b)
    a = a + b
    b = a - b
    a = a - b

    print(a,b)


def swap1(a,b):

    print(a,b)
    a = a* b
    b = a/ b
    a = a/b

    print(a,b)

swap2(5,6)

