wordCount = {}
text = str(input("Text: "))
wordList = text.split(" ")
letterCount = []
for word in wordList:
    letterCount.append(len(word))
    if word in wordCount:
        wordCount[word] += 1
    else:
        wordCount[word] = 1

for word in wordCount:
    print("{:{}} : {}".format(word, max(letterCount), wordCount[word]))
