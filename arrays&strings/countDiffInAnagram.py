def anagram(s):
    if len(s) == 0:
        return -1

    else:
        n = len(s)
        f = int(n / 2)
        sec = int(n / 2) + 1
        print(n, f, sec)
        sfirst = s[:f]
        ssecond = s[-sec:]

        if sfirst == ssecond:
            return 0
        else:
            cnt = {}
            for c in sfirst:
                if c in cnt.keys():
                    cnt[c] += 1
                else:
                    cnt[c] = 1

            count = 0
            for c in ssecond:
                if c not in cnt.keys():
                    count += 1

        return count



# method 2

def anagram2(s):

    if len(s) <= 0:
        return -1

    if len(s)%2 != 0:
        return -1

    flen = int(len(s)/2)
    slen = int( len(s)/2)

    print(flen, slen)
    fstr = list(s[:flen])
    sstr = list(s[slen:])
    print( fstr, sstr)
    count  = 0
    for c in sstr:
        if c in fstr:
            fstr.remove(c)
        else:
            count +=1

    return count


print(anagram2("xyyx"))