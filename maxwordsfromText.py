import operator


def retrieveMostFrequentlyUsedWords(literatureText, wordsToExclude):
    # WRITE YOUR CODE HERE
    # Algo
    # split the text by words
    # iterator over it
    # if word is not in wordsToExclude check if its present in wordCountDict
    # if yes increment the count
    # if not add into dictionary
    # return the list of words having count more than 1

    wordCountDict = {}
    for word in literatureText.split():
        if word not in wordsToExclude:
            if word not in wordCountDict:
                wordCountDict[word] = 1
            else:
                wordCountDict[word] += 1
    output = []
    output = {k for k, v in wordCountDict.items() if v != 1}

    return output


print(retrieveMostFrequentlyUsedWords("Jack in the Jack rose and rose",["in"]))