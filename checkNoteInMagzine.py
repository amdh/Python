

def checkMagazine(magazine, note):
    cntdict = {}

    for i in magazine:
        if i in cntdict.keys():
            cntdict[i] += 1
        else:
            cntdict[i] = 1

    for u in note:
        if u not in cntdict.keys():
            return 'No'
        else:
            cntdict[u] -= 1

    return 'Yes'

magazine = 'give me one grand today night'
mag = magazine.split(' ')
note = 'give one grand today'
n = note.split(' ')
v = checkMagazine(mag,n)
print(v)