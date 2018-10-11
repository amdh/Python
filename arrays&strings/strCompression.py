

global str


def compress(str1):

    prev =''
    recent = ''
    newstr = []
    cnt = 0
    str1 = str1+'\0'
    for i in str1:
        recent = i
        print(recent)
        if prev == recent:
            cnt +=1
        else:
            if cnt != 0:
                newstr.append(prev)
                w = str(cnt)
                newstr.append(w)
            cnt = 1


        prev = i

    print(' '.join(newstr))


compress('aabccccaaaa')