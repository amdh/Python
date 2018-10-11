def checkMagazine(magazine, note):
    notesize = len(note)
    cnt = 0
    i = 0
    print(notesize)
    for w in magazine:

        if w == note[i]:

            cnt += 1
            i += 1
            if cnt == notesize:
                return 'Yes'
        else:
            cnt = 0

    return 'No'

magazine = 'I am not here coz I am there'
mag = magazine.split(' ')
note = 'I am there'
n = note.split(' ')
v = checkMagazine(mag,n)
print(v)