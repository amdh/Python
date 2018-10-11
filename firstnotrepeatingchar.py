def firstNotRepeatingCharacter(s):
    dict_char_cnt = {}
    index = []

    for char in s:
        if char in dict_char_cnt:
            dict_char_cnt[char] += 1
        else:
            dict_char_cnt[char] = 1
            index.append(char)

    val = min(dict_char_cnt.items(), key=lambda x: x[1])
    print(val)
    if val[1] == 1:
        return val[0]
    else:
        return '_'


print(firstNotRepeatingCharacter('geekforgeeks'))

