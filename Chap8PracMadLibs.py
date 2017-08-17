#! \usr\bin\env python3

# Chapter 8 Practice Mad Libs

# Replaces all ADJECTIVE, NOUN, ADVERB, VERB keywords with user input in text.

import re


with open('madlibs.txt') as madLibFile:
    madLibContents = madLibFile.read()
madLibWords = list(madLibContents.split())

adjectiveRegex = re.compile(r'ADJECTIVE*')
nounRegex = re.compile(r'NOUN*')
adverbRegex = re.compile(r'ADVERB*')
verbRegex = re.compile(r'VERB*')

for i in range(len(madLibWords)):
    if adjectiveRegex.match(madLibWords[i]):
        print('Enter an adjective', end=': ')
        sub = input()
        madLibWords[i] = adjectiveRegex.sub(sub, madLibWords[i])
    elif nounRegex.match(madLibWords[i]):
        print('Enter a noun', end =': ')
        sub = input()
        madLibWords[i] = nounRegex.sub(sub, madLibWords[i])
    elif adverbRegex.match(madLibWords[i]):
        print('Enter an adverb', end =': ')
        sub = input()
        madLibWords[i] = adverbRegex.sub(sub, madLibWords[i])
    elif verbRegex.match(madLibWords[i]):
        print('Enter a verb', end =': ')
        sub = input()
        madLibWords[i] = verbRegex.sub(sub, madLibWords[i])
    else:
        madLibWords[i] = madLibWords[i] + ' '
        continue

    madLibWords[i] = madLibWords[i] + ' '

joinWordsList = ''

newString = joinWordsList.join(madLibWords)
n = len(newString)


with open('madlibsNew.txt', 'w') as newMadLibFile:
    newMadLibFile.write(newString[0:n-1])
print(newString)

newMadLibFile.close()
