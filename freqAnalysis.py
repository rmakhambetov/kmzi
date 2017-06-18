englishLetterFreq = {'О': 9.28, 'А': 8.66, 'Е': 8.10, 'И': 7.45, 'Н': 6.35, 'Т': 6.30, 'Р': 5.53, 'С': 5.45, 'Л': 4.32,
 'В': 4.19, 'К': 3.47, 'П': 3.35, 'М': 3.29, 'У': 2.90, 'Д': 2.56, 'Я': 2.22, 'Ы': 2.11, 'Ь': 1.90, 'З': 1.81, 'Б': 1.51,
  'Г': 1.41, 'Й': 1.31, 'Ч': 1.27, 'Ю': 1.03, 'Х': 0.92, 'Ж': 0.78, 'Ш': 0.77, 'Щ': 0.49, 'Ф': 0.40, 'Э': 0.17, 'Ъ':0.04}
ETAOIN = 'оаеинтрслвкпмудяыьзбгйчюхжшцщфэъ'.upper()
LETTERS = 'абвгдежзиклмнопрстуфхцчшщъыьэюя'.upper()



def getLetterCount(message):
    letterCount = {'А': 0, 'Б': 0, 'В': 0, 'Г': 0, 'Д': 0, 'Е': 0, 'Ж': 0, 'З': 0, 'И': 0, 'К': 0, 'Л': 0, 'М': 0, 'Н': 0,
     'О': 0, 'П': 0, 'Р': 0, 'С': 0, 'Т': 0, 'У': 0, 'Ф': 0, 'Х': 0, 'Ц': 0, 'Ч': 0, 'Ш': 0, 'Щ': 0, 'Ъ': 0, 'Ы': 0, 'Ь': 0,
     'Э':0, 'Ю':0, 'Я':0}

    for letter in message.upper():
        if letter in LETTERS:
            letterCount[letter] += 1

    return letterCount


def getItemAtIndexZero(x):
    return x[0]


def getFrequencyOrder(message):
    letterToFreq = getLetterCount(message)



    freqToLetter = {}
    for letter in LETTERS:
        if letterToFreq[letter] not in freqToLetter:
            freqToLetter[letterToFreq[letter]] = [letter]
        else:
            freqToLetter[letterToFreq[letter]].append(letter)



    for freq in freqToLetter:
        freqToLetter[freq].sort(key=ETAOIN.find, reverse=True)
        freqToLetter[freq] = ''.join(freqToLetter[freq])

    freqPairs = list(freqToLetter.items())
    freqPairs.sort(key=getItemAtIndexZero, reverse=True)

    freqOrder = []
    for freqPair in freqPairs:
        freqOrder.append(freqPair[1])

    return ''.join(freqOrder)

def englishFreqMatchScore(message):
    freqOrder = getFrequencyOrder(message)

    matchScore = 0

    for commonLetter in ETAOIN[:6]:
        if commonLetter in freqOrder[:6]:
            matchScore += 1

    for uncommonLetter in ETAOIN[-6:]:
        if uncommonLetter in freqOrder[-6:]:
            matchScore += 1

    return matchScore