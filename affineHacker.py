import affineCipher, cryptomath

SILENT_MODE = True

def main():
    
    
    myMessage = """блцкзуьл щнунэкепулубке-еу–утшдшг"""

    hackedMessage = hackAffine(myMessage)

    if hackedMessage != None:
        
        
        print(hackedMessage)
    else:
        print('Failed to hack encryption.')


def hackAffine(message):
    print('Hacking...')
    print('(Press Ctrl-C or Ctrl-D to quit at any time.)')

    for key in range(len(affineCipher.SYMBOLS) ** 2):
        keyA = affineCipher.getKeyParts(key)[0]
        if cryptomath.gcd(keyA, len(affineCipher.SYMBOLS)) != 1:
            continue

        decryptedText = affineCipher.decryptMessage(key, message)
        if not SILENT_MODE:
            print('Tried Key %s... (%s)' % (key, decryptedText[:40]))

        print()
        print('Possible encryption hack:')
        print('Key: %s' % (key))
        print('Decrypted message: ' + decryptedText[:200])
        print()
        print('Enter D for done, or just press Enter to continue hacking:')
        response = input('> ')

        if response.strip().upper().startswith('D'):
            return decryptedText
    return None




if __name__ == '__main__':
    main()