

def isColindrom(word):

    # for i in word:
    #     if i == len(word)- 2:
    #         return False
    #     else:
    #         subword = word[i]
    #
    #     print(i)

    for i in range(0, len(word)):
        if i == len(word) - 2:
            return False
        else:
            subword = word[i] + word[i+1] + word[i+2]
            subword = subword[::-1]
            print(subword)
            if word.find(subword) == -1:
                continue
            else:
                return True

print(isColindrom('abcaskybh'))