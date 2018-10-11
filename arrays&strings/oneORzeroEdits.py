

def check(str1, str2):
    # 3 cases

#case 1: if lenth are simialr then its a replace
#case 2: if lengths are odd then its either insert or remove
# if one chara is diff then its

    if len(str1) == len(str2):
        onlyOnereplace = 0
        for i in str1:
            index = str1.index(i)
            if i != str2[index]:
                onlyOnereplace+=1

        if onlyOnereplace > 1:
            print("false")
        else:
            print('true')

    else:
        cntdict = {}
        for i in str1:
            if i in cntdict.keys():
                cntdict[i] +=1
            else:
                cntdict[i] = 1

        for i in str2:
            if i in cntdict.keys():
                if cntdict[i] > 1:
                    cntdict[i] -= 1
                else:
                    cntdict.pop(i)
            else:
                cntdict[i] = 1


        if len(cntdict) >1 :
            print('false')
        else:
            print('true')


check('pale','ple')
check('pales','pale')
check('pale','bale')
check('pale','bake')