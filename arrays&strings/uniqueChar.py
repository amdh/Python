
#using external datastructure
def isUnique(str):
    arr = []
    for i in str:

        if i in arr:
            print('not unique')
            break
        else:
            arr.append(i)
        print(ord(i))

#without usign external datastructure
def isUni(str):
    f = False
    for i in str:
        cnt = str.index(i) + 1
        for j in str[cnt:]:
            print(j,cnt)

            if j == i:
                f=True
                break

        cnt+=1

        if f == True:
            print('not unique')
            break
        else:
            continue

    if f == False:
        print('is uniuq')




isUni('asdlkjk')