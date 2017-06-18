import itertools, re
import vigenereCipher, freqAnalysis

LETTERS = """абвгдежзиклмнопрстуфхцчшщъыьэюя""".upper()
SILENT_MODE = True 
NUM_MOST_FREQ_LETTERS = 4 
MAX_KEY_LENGTH = 16 
NONLETTERS_PATTERN = re.compile('[^а-я]')


def main():

    ciphertext = """г рсш юувебу рхщт тэюкюао л ъютчщршрытмъ, ъ г иашя тчоз ьч ьючеъютънэ ерюсчбр юхяфаюгйй, ык чоьйр угт ыъ слхэ ъу вжгохюн щб няи юрая хьъыачозшэл фъишк. мьувгжу шъ р аеуышдугуну шяэвбнцхюн ь рыьсэойощъэ ыхчсю, тш чьдпыьны ьд ещък ойэп щшшшь бпцбцхщъ, цыолэь ътьщпсьфбц фпшаея ъьхыяьф ъщйуо, чър гъныъггби ющчеж ышр ухп аьсмчьй, у яцтща илайпштм шо лтххслытдынк ъюшюаас чуъгорърсш ыхчсл ц чн пчмжг бнуь, лщашэйч лыбрхщъ ф шуны ыте оьхырак, нйыщодсуркм рнвыьвтыяфй ык оувжо юеоб. бйэуъа цгрщщчхщатз аъх ъчткдк. тзч гвуън ья вжщ ъыпьйч зпъшан, у рыт ралыбн чощбцьый уюф щсъыъяьч, ыпььяаэыещ ц гуыовъйю; трсшсыс зр ьч эцглшбх п ьцйшьбчб грюяьхаотк эш яюаруыфт ш аирюэ, ыы даншкш, ыа оушьы ыч рщяцтщ фьфат ю ыън шо лыч, ъ жоь ытюцчр цыььэоущшюк фжццфхъ юфсуыяран у яьыщо зр рпшцьйч щиоьбьэяьпью. гща щыечню ык ыпвбэышщ эеуу ьч ыядбшьмхщга шо шьбклр сэюаак ъьъыяэй мохйхтнуепюшъц рщпц ц бсуэкш ш щжчщп, аядсрътп фтешйу пххмкт лшугукзтв сэбтучыш ф дюяьам эжьыэл ачоз, яьнютаьк эроцбэк, фншъж эоуъй ьсщмьюн ф юэця ъуфжпьциг юслечиг хмюптъоз."""
    hackedMessage = hackVigenere(ciphertext)

    if hackedMessage != None:
        print(hackedMessage)
    else:
        print('Failed to hack encryption.')


def findRepeatSequencesSpacings(message):
    
    
    

    
    message = NONLETTERS_PATTERN.sub('', message.upper())

    
    seqSpacings = {} 
    for seqLen in range(3, 6):
        for seqStart in range(len(message) - seqLen):
            
            seq = message[seqStart:seqStart + seqLen]

            
            for i in range(seqStart + seqLen, len(message) - seqLen):
                if message[i:i + seqLen] == seq:
                    
                    if seq not in seqSpacings:
                        seqSpacings[seq] = [] 

                    
                    
                    seqSpacings[seq].append(i - seqStart)
    return seqSpacings


def getUsefulFactors(num):
    
    
    

    if num < 2:
        return [] 

    factors = [] 

    
    
    for i in range(2, MAX_KEY_LENGTH + 1): 
        if num % i == 0:
            factors.append(i)
            factors.append(int(num / i))
    if 1 in factors:
        factors.remove(1)
    return list(set(factors))


def getItemAtIndexOne(x):
    return x[1]


def getMostCommonFactors(seqFactors):
    
    factorCounts = {} 

    
    
    
    for seq in seqFactors:
        factorList = seqFactors[seq]
        for factor in factorList:
            if factor not in factorCounts:
                factorCounts[factor] = 0
            factorCounts[factor] += 1

    
    
    factorsByCount = []
    for factor in factorCounts:
        
        if factor <= MAX_KEY_LENGTH:
            
            
            factorsByCount.append( (factor, factorCounts[factor]) )

    
    factorsByCount.sort(key=getItemAtIndexOne, reverse=True)

    return factorsByCount


def kasiskiExamination(ciphertext):
    
    
    
    repeatedSeqSpacings = findRepeatSequencesSpacings(ciphertext)

    
    seqFactors = {}
    for seq in repeatedSeqSpacings:
        seqFactors[seq] = []
        for spacing in repeatedSeqSpacings[seq]:
            seqFactors[seq].extend(getUsefulFactors(spacing))

    
    factorsByCount = getMostCommonFactors(seqFactors)

    
    
    
    allLikelyKeyLengths = []
    for twoIntTuple in factorsByCount:
        allLikelyKeyLengths.append(twoIntTuple[0])

    return allLikelyKeyLengths


def getNthSubkeysLetters(n, keyLength, message):
    
    
    
    
    

    
    message = NONLETTERS_PATTERN.sub('', message)

    i = n - 1
    letters = []
    while i < len(message):
        letters.append(message[i])
        i += keyLength
    return ''.join(letters)


def attemptHackWithKeyLength(ciphertext, mostLikelyKeyLength):
    
    ciphertextUp = ciphertext.upper()
    
    
    allFreqScores = []
    for nth in range(1, mostLikelyKeyLength + 1):
        nthLetters = getNthSubkeysLetters(nth, mostLikelyKeyLength, ciphertextUp)

        
        
        
        
        freqScores = []
        for possibleKey in LETTERS:
            decryptedText = vigenereCipher.decryptMessage(possibleKey, nthLetters)
            keyAndFreqMatchTuple = (possibleKey, freqAnalysis.englishFreqMatchScore(decryptedText))
            freqScores.append(keyAndFreqMatchTuple)
        
        freqScores.sort(key=getItemAtIndexOne, reverse=True)

        allFreqScores.append(freqScores[:NUM_MOST_FREQ_LETTERS])

    if not SILENT_MODE:
        for i in range(len(allFreqScores)):
            
            print('Possible letters for letter %s of the key: ' % (i + 1), end='')
            for freqScore in allFreqScores[i]:
                print('%s ' % freqScore[0], end='')
            print() 

    
    
    for indexes in itertools.product(range(NUM_MOST_FREQ_LETTERS), repeat=mostLikelyKeyLength):
        
        possibleKey = ''
        for i in range(mostLikelyKeyLength):
            possibleKey += allFreqScores[i][indexes[i]][0]

        if not SILENT_MODE:
            print('Attempting with key: %s' % (possibleKey))

        decryptedText = vigenereCipher.decryptMessage(possibleKey, ciphertextUp)

        
        origCase = []
        for i in range(len(ciphertext)):
            if ciphertext[i].isupper():
                origCase.append(decryptedText[i].upper())
            else:
                origCase.append(decryptedText[i].lower())
        decryptedText = ''.join(origCase)

        
        print('Possible encryption hack with key %s:' % (possibleKey))
        print(decryptedText[:200]) 
        print()
        print('Enter D for done, or just press Enter to continue hacking:')
        response = input('> ')

        if response.strip().upper().startswith('D'):
            return decryptedText

    return None


def hackVigenere(ciphertext):
    
    
    allLikelyKeyLengths = kasiskiExamination(ciphertext)
    hackedMessage = None
    if not SILENT_MODE:
        keyLengthStr = ''
        for keyLength in allLikelyKeyLengths:
            keyLengthStr += '%s ' % (keyLength)
        print('Kasiski Examination results say the most likely key lengths are: ' + keyLengthStr + '\n')

    for keyLength in allLikelyKeyLengths:
        if not SILENT_MODE:
            print('Attempting hack with key length %s (%s possible keys)...' % (keyLength, NUM_MOST_FREQ_LETTERS ** keyLength))
        hackedMessage = attemptHackWithKeyLength(ciphertext, keyLength)
        if hackedMessage != None:
            break

    
    
    if hackedMessage == None:
        if not SILENT_MODE:
            print('Unable to hack message with likely key length(s). Brute forcing key length...')
        for keyLength in range(1, MAX_KEY_LENGTH + 1):
            
            if keyLength not in allLikelyKeyLengths:
                if not SILENT_MODE:
                    print('Attempting hack with key length %s (%s possible keys)...' % (keyLength, NUM_MOST_FREQ_LETTERS ** keyLength))
                hackedMessage = attemptHackWithKeyLength(ciphertext, keyLength)
                if hackedMessage != None:
                    break
    return hackedMessage




if __name__ == '__main__':
    main()