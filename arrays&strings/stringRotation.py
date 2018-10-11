


#left rotation:
def rotate(str, n):

    lfrist = str[0:n]
    lsecond = str[n:]
    #left rotation
    lstr = lsecond + lfrist
    print(lstr)
    rfirst = str[-n:]
    rsecond = str[0:len(str)-n]
    rstr = rfirst + rsecond
    print(rstr)

rotate('abcdsrt', 2)