import math

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

textDict = {}                               # create global alphabet dict
counter = 0
for let in alphabet:
    counter += 1
    textDict[let] = counter

def main_function(textFile, cipherFile):
    cipherType_input = input("Please enter the type of cipher")
    eord = input("Do you want to encrypt or decrypt \"e\" or \"d\"")
    if (cipherType_input == "substitution"):
        sub_cipherList = input("enter your cipher list")
        if eord == "e":
            substitution_encrypt(textFile, cipherFile,sub_cipherList)
        else:
            substitution_decrypt(textFile, cipherFile,sub_cipherList)
    elif (cipherType_input == "keyword"):
        sub_keyword = input("Enter a keyword")
        if eord == "e":
            keyword_encrypt(textFile, cipherFile,sub_keyword)
        else:
            keyword_decrypt(textFile, cipherFile,sub_keyword)
    elif(cipherType_input == "caesar"):
        sub_caesar = input("Enter a shift")
        if eord == "e":
            caesar_encrypt(textFile, cipherFile,sub_caesar)
        else:
            caesar_decrypt(textFile, cipherFile,sub_caesar)
    elif(cipherType_input == "rot13"):
        if eord == "e":
            rot13_encrypt(textFile, cipherFile)
        else:
            rot13_decrypt(textFile, cipherFile)
    elif(cipherType_input == "atbash"):
        if eord == "e":
            atbash_encrypt(textFile, cipherFile)
        else:
            atbash_decrypt(textFile, cipherFile)
    elif(cipherType_input == "affine"):
        a = input("Enter a value for a: ")
        b = input("Enter a value for b: ")
        if eord == "e":
            affine_encrypt(textFile, cipherFile,a,b)
        else:
            affine_decrypt(textFile, cipherFile,a,b)

def key_error(key):
    """
    checks if key has any duplicate letters
    :param key: list containing encrypted alphabet
    :return: true if no duplicates, false if duplicate detected
    """
    letterList = []
    for letter in key:
        if letter in letterList:
            return False
        letterList.append(letter)
        return True


def createCipherDict(cipherList):
    '''
    creates a numbered dictionary based on the encrypted alphabet
    :param cipherList: encrypted alphabet as a list
    :return: encrypted dictionary numbered 1-26
    '''
    cipherDict = {}
    let_counter = 0
    for char in cipherList:  # create cipher dict
        let_counter += 1
        cipherDict[char] = let_counter
    return cipherDict


def encrypt(line, cipherList):
    """
    takes an encrypted list and turns it into dictionary, then writes letter from encrypted
    dict according to corresponding letter in alphabet dict
    :param line: the line in the plain text file
    :param cipherList: the encrypted list
    :return: encrypted line
    """
    cipherDict = createCipherDict(cipherList)   # calls function to created numbered dictionary based on encrypted list
    encryptedLine = ""
    for char in line:
        upper = False
        if char.isupper() == True:
            char = char.lower()
            upper = True
        if char not in alphabet:                # if special char, just write, don't encrypt
            encryptedLine += char
        else:
            loc = textDict[char]                # determines location of current char in alphabet
            for key in cipherDict.keys():       # loops through keys in cipher dict until the letter
                if cipherDict[key] == loc:      # corresponding to correct location is found
                    if upper == True:           # if the char was uppercase, add the uppercase version of the key
                        upperKey = key.upper()
                        encryptedLine += upperKey
                    else:
                        encryptedLine += key
    return encryptedLine


def decrypt(line, cipherList):
    """
    takes encrypted list and turns it into dictionary, then writes the letter from
    the alphabet dictionary according to the corresponding letter in the cipher dict
    :param line: line in cipher file to be decrypted
    :param cipherList: encrypted list
    :return: decrypted line
    """
    cipherDict = createCipherDict(cipherList)   # calls function to created numbered dictionary based on encrypted list
    decryptedLine = ""
    for char in line:
        upper = False
        if char.isupper() == True:
            char = char.lower()
            upper = True
        if char not in alphabet:                # if special char, just write, don't encrypt
            decryptedLine += char
        else:
            loc = cipherDict[char]              # determines location of current char in cipher dict
            for key in textDict.keys():         # loops through letters in alphabet until the letter
                if textDict[key] == loc:        # corresponding to correct location is found
                    if upper == True:           # if the char was uppercase, add the uppercase version of the key
                        upperKey = key.upper()
                        decryptedLine += upperKey
                    else:
                        decryptedLine += key
    return decryptedLine


def substitution_encrypt(textFile, cipherFile, cipherList):
    """
    encrypts the plain text file using the substitution a = b
    :param textFile: plain text file
    :param cipherFile: encrypted file
    :param cipherList: encrypted alphabet as list
    :return: encrypted file
    """
    if key_error(cipherList) == False:              # calls function to check is key (represented as list) is valid
        print("Key not valid")
    try:
        read_file = open(textFile)
    except:
        print("Cannot open input file")
    try:
        write_file = open(cipherFile, "w")
    except:
        print("Cannot open output file")
    for line in read_file:
        write_file.write(encrypt(line, cipherList))  # calls function to encrypt file based on encrypted list


def substitution_decrypt(textFile, cipherFile, cipherList):
    """
    decrypts encrypted file with substitution a = b
    :param textFile: decrypted/plain text file
    :param cipherFile: encrypted file
    :param cipherList: encrypted alphabet as list
    :return: decrypted/plain text file
    """
    if key_error(cipherList) == False:
        print("Key not valid")
    try:
        read_file = open(cipherFile)
    except:
        print("Cannot open input file")
    try:
        write_file = open(textFile, "w")
    except:
        print("Cannot open output file")
    for line in read_file:
        write_file.write(decrypt(line, cipherList))  # calls function to decrypt file based on encrypted list


def keywordListCreator(keyword):
    """
    takes a keyword and creates an encrypted alphabet as a list
    :param keyword: any string with no repeated letters
    :return: encrypted alphabet stored in a list
    """
    alphabetList = alphabet.copy()
    cipherList = []
    for letter in keyword:
        alphabetList.remove(letter)
        cipherList.append(letter)
    for letter in alphabetList:
        cipherList.append(letter)
    return cipherList


def keyword_encrypt(textFile, cipherFile, keyword):
    """
    encrypts plain text file based on keyword
    :param textFile: plain text file
    :param cipherFile: encrypted file
    :param keyword: any str with no repeated letters
    :return: encrypted file
    """
    if key_error(keyword) == False:
        print("Key not valid")
    try:
        read_file = open(textFile)
    except:
        print("Cannot open input file")
    try:
        write_file = open(cipherFile, "w")
    except:
        print("Cannot open output file")
    cipherList = keywordListCreator(keyword)            # calls function to create encrypted alphabet based on keyword
    for line in read_file:
        write_file.write(encrypt(line, cipherList))


def keyword_decrypt(textFile, cipherFile, keyword):
    """
    decrypts encrypted file based on keyword
    :param cipherFile: encrypted file
    :param textFile: decrypted/plain text file
    :param keyword: any str with no repeated char
    :return: decrypted/plain text file
    """
    if key_error(keyword) == False:
        print("Key not valid")
    try:
        read_file = open(cipherFile)
    except:
        print("Cannot open input file")
    try:
        write_file = open(textFile, "w")
    except:
        print("Cannot open output file")
    cipherList = keywordListCreator(keyword)
    for line in read_file:
        write_file.write(decrypt(line, cipherList))


def caesarListGenerator(shift):
    '''
    creates an encrypted alphabet list based on the shift
    :param shift: int value corresponding to the number each letter should shift to the right
    :return: encrypted alphabet list based on shift
    '''
    cipherList = []
    alphabetList = alphabet.copy()
    for i in range(len(alphabetList)):
        num = (i + shift) % len(alphabetList)           # the modulo prevents the index from being out of range
        cipherList.append(alphabetList[num])            # ex: 27 % 26 returns 1
    return cipherList


def caesar_encrypt(textFile, cipherFile, shift):
    """
    encrypted plain text file based on shift
    :param textFile: plain text file
    :param cipherFile: encrypted file
    :param shift: int value corresponding to the number each letter should shift to the right
    :return: encrypted file
    """
    try:
        read_file = open(textFile)
    except:
        print("Cannot open input file")
    try:
        write_file = open(cipherFile, "w")
    except:
        print("Cannot open output file")
    cipherList = caesarListGenerator(shift)                 # calls function to create encrypted list based on shift
    for line in read_file:
        write_file.write(encrypt(line, cipherList))


def caesar_decrypt(textFile, cipherFile, shift):
    """
    decrypts encrypted file based on shift
    :param cipherFile: encrypted file
    :param textFile: decrypted/ plain text file
    :param shift: int value corresponding to the number each letter should shift to the right
    :return: decrypted/ plain text file
    """
    try:
        read_file = open(cipherFile)
    except:
        print("Cannot open input file")
    try:
        write_file = open(textFile, "w")
    except:
        print("Cannot open output file")
    cipherList = caesarListGenerator(shift)
    for line in read_file:
        write_file.write(decrypt(line, cipherList))


def rot13_encrypt(textFile, cipherFile):
    """
    encrypts file based on shift of each letter 13 places to the right
    :param textFile: plain text file
    :param cipherFile: encrypted file
    :return: encrypted file
    """
    caesar_encrypt(textFile, cipherFile, 13)


def rot13_decrypt(textFile, cipherFile):
    """
    decrypts encrypted file based on shift of each letter 13 places to the right
    :param textFile: decrypted/plain text file
    :param cipherFile: encrypted file
    :return: decrypted/ plain text file
    """
    caesar_decrypt(textFile, cipherFile, 13)


def atbash_encrypt(textFile, cipherFile):
    """
    encrypts file by reversing the alphabet
    :param textFile: plain text file
    :param cipherFile: encrypted file
    :return: encrypted file
    """
    try:
        read_file = open(textFile)
    except:
        print("Cannot open input file")
    try:
        write_file = open(cipherFile, "w")
    except:
        print("Cannot open output file")
    cipherList = alphabet.copy()
    cipherList.reverse()
    for line in read_file:
        write_file.write(encrypt(line, cipherList))


def atbash_decrypt(textFile, cipherFile):
    """
    decrypts encrypted file based on encrypted alphabet being reversed
    :param textFile: decrypted/plaint text file
    :param cipherFile: encrypted file
    :return: decrypted/plain text file
    """
    try:
        read_file = open(cipherFile)
    except:
        print("Cannot open input file")
    try:
        write_file = open(textFile, "w")
    except:
        print("Cannot open output file")
    cipherList = alphabet.copy()
    cipherList.reverse()
    for line in read_file:
        write_file.write(decrypt(line, cipherList))


def affine_encrypt(textFile, cipherFile, a, b):
    """
    encrypts file based on encrypt function y = (ax+b) % m, where m is the length of the alphabet
    :param textFile: plain text file
    :param cipherFile: encrypted file
    :param a: int value to transform each letter, x. Must be coprime with m
    :param b: int value used to transform each letter, x
    :return: encrypted file
    """
    try:
        read_file = open(textFile)
    except:
        print("Cannot open input file")
    try:
        write_file = open(cipherFile, "w")
    except:
        print("Cannot open output file")
    if math.gcd(a, 26) != 1:                        # checks if a and m are coprime (gcd should equal 1)
        print("Key not valid")
    cipherList = []
    for i in range(len(alphabet)):
        encryptedLetter = (a*i + b) % len(alphabet)  # affine encryption function
        cipherList.append(alphabet[encryptedLetter])
    for line in read_file:
        write_file.write(encrypt(line, cipherList))


def affine_decrypt(textFile, cipherFile, a, b):
    """
    decrypts encrypted file based on decryption function y = a^-1(x-b) % m, where a^-1 is the
    modular multiplicative inverse of a % m and m is the length of the alphabet
    :param textFile: decrypted/plain text file
    :param cipherFile: encrypted file
    :param a: int value to transform each letter, x. Must be coprime with m
    :param b: int value used to transform each letter, x
    :return: decrypted/plain text file
    """
    try:
        read_file = open(textFile)
    except:
        print("Cannot open input file")
    try:
        write_file = open(cipherFile, "w")
    except:
        print("Cannot open output file")
    if math.gcd(a, 26) != 1:
        print("Key not valid")
    cipherList = []
    for i in range(len(alphabet)):
        encryptedLetter = (((pow(a, -1, 26)) * (i-b)) % len(alphabet))  # affine decryption function
        cipherList.append(alphabet[encryptedLetter])                    # pow() is the modular multiplicative inverse
    for line in read_file:
        write_file.write(encrypt(line, cipherList))


AtoBSubList = ['b', 'a', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

main_function("plainText.txt","cipherText.txt")