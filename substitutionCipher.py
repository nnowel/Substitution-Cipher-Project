import math

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

textDict = {}                       # create global alphabet dict
counter = 0
for let in alphabet:
    counter += 1
    textDict[let] = counter


def key_error(key):                       # checks key for duplicate letters
    """

    :param key:
    :return:
    """
    letterList = []
    for letter in key:
        if letter in letterList:
            return False
        letterList.append(letter)
        return True


def encrypt(line, cipherList):
    """

    :param line:
    :param cipherList:
    :return:
    """
    cipherDict = {}
    let_counter = 0
    for char in cipherList:               # create cipher dict
        let_counter += 1
        cipherDict[char] = let_counter
    encryptedLine = ""
    for char in line:
        if char not in alphabet:          # if special char, just write, don't encrypt
            encryptedLine += char
        else:
            loc = textDict[char]            # determines location of current char in alphabet
            for key in cipherDict.keys():     # loops through keys in cipher dict until the letter
                if cipherDict[key] == loc:    # corresponding to correct location is found
                    encryptedLine += key
    return encryptedLine


def decrypt(line, cipherList):
    """

    :param line:
    :param cipherList:
    :return:
    """
    cipherDict = {}
    let_counter = 0
    for char in cipherList:                     # create cipher dict
        let_counter += 1
        cipherDict[char] = let_counter
    decryptedLine = ""
    for char in line:
        if char not in alphabet:                # if special char, just write, don't encrypt
            decryptedLine += char
        else:
            loc = cipherDict[char]              # determines location of current char in cipher dict
            for key in textDict.keys():         # loops through letters in alphabet until the letter
                if textDict[key] == loc:        # corresponding to correct location is found
                    decryptedLine += key
    return decryptedLine


def substitution_encrypt(textFile, cipherFile, cipherList):
    """

    :param textFile:
    :param cipherFile:
    :param cipherList:
    :return:
    """
    if key_error(cipherList) == False:
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
        write_file.write(encrypt(line, cipherList))


def substitution_decrypt(textFile, cipherFile, cipherList):
    """

    :param textFile:
    :param cipherFile:
    :param cipherList:
    :return:
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
        write_file.write(decrypt(line, cipherList))


def keywordListCreator(keyword):
    """

    :param keyword:
    :return:
    """
    alphabetList = alphabet.copy()              # creating cipher list from keyword
    cipherList = []
    for letter in keyword:
        alphabetList.remove(letter)
        cipherList.append(letter)
    for letter in alphabetList:
        cipherList.append(letter)
    print(cipherList)
    return cipherList


def keyword_encrypt(textFile, cipherFile, keyword):
    """

    :param textFile:
    :param cipherFile:
    :param keyword:
    :return:
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
    cipherList = keywordListCreator(keyword)
    for line in read_file:
        write_file.write(encrypt(line, cipherList))


def keyword_decrypt(cipherFile, textFile, keyword):
    """

    :param cipherFile:
    :param textFile:
    :param keyword:
    :return:
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


def caesar_encrypt(textFile, cipherFile, shift):
    """

    :param textFile:
    :param cipherFile:
    :param shift:
    :return:
    """
    try:
        read_file = open(textFile)
    except:
        print("Cannot open input file")
    try:
        write_file = open(cipherFile, "w")
    except:
        print("Cannot open output file")
    cipherList = []
    alphabetList = alphabet.copy()
    for i in range(len(alphabetList)):
        num = (i + shift) % len(alphabetList)           # the modulo prevents the index from being out of range
        cipherList.append(alphabetList[num])            # ex: 27 % 26 returns 1
    for line in read_file:
        write_file.write(encrypt(line, cipherList))


def caesar_decrypt(cipherFile, textFile, shift):
    """

    :param cipherFile:
    :param textFile:
    :param shift:
    :return:
    """
    try:
        read_file = open(cipherFile)
    except:
        print("Cannot open input file")
    try:
        write_file = open(textFile, "w")
    except:
        print("Cannot open output file")
    alphabetList = alphabet.copy()
    cipherList = []
    for i in range(len(alphabetList)):
        num = (i+shift) % len(alphabetList)
        cipherList.append(alphabetList[num])
    for line in read_file:
        write_file.write(decrypt(line, cipherList))


def rot13_encrypt(textFile, cipherFile):
    """

    :param textFile:
    :param cipherFile:
    :return:
    """
    caesar_encrypt(textFile, cipherFile, 13)


def rot13_decrypt(textFile, cipherFile):
    """

    :param textFile:
    :param cipherFile:
    :return:
    """
    caesar_decrypt(textFile, cipherFile, 13)


def atbash_encrypt(textFile, cipherFile):
    """

    :param textFile:
    :param cipherFile:
    :return:
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

    :param textFile:
    :param cipherFile:
    :return:
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

    :param textFile:
    :param cipherFile:
    :param a:
    :param b:
    :return:
    """
    try:
        read_file = open(textFile)
    except:
        print("Cannot open input file")
    try:
        write_file = open(cipherFile, "w")
    except:
        print("Cannot open output file")
    if math.gcd(a, 26) != 1:                        # checks if a and m are coprime
        print("Key not valid")
    cipherList = []
    for i in range(len(alphabet)):
        encryptedLetter = (a*i + b) % len(alphabet)  # affine encryption function
        cipherList.append(alphabet[encryptedLetter])
    for line in read_file:
        write_file.write(encrypt(line, cipherList))


def affine_decrypt(textFile, cipherFile, a, b):
    """

    :param textFile:
    :param cipherFile:
    :param a:
    :param b:
    :return:
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
        cipherList.append(alphabet[encryptedLetter])
    for line in read_file:
        write_file.write(encrypt(line, cipherList))


general_cipherList1 = ['e', 'b', 'c', 'd', 'a', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# substitution_decrypt("/Users/nathanielnowel/PycharmProjects/Substitution-Cipher-Project/plainText.txt",
                    # "/Users/nathanielnowel/PycharmProjects/Substitution-Cipher-Project/cipherText.txt",
                    # cipherList1)
# keyword_decrypt("/Users/nathanielnowel/PycharmProjects/Substitution-Cipher-Project/cipherText.txt",
                # "/Users/nathanielnowel/PycharmProjects/Substitution-Cipher-Project/plainText.txt", "zebras")

# caesar_decrypt("/Users/nathanielnowel/PycharmProjects/Substitution-Cipher-Project/cipherText.txt",
                # "/Users/nathanielnowel/PycharmProjects/Substitution-Cipher-Project/plainText.txt", 23)

# rot13_decrypt("/Users/nathanielnowel/PycharmProjects/Substitution-Cipher-Project/cipherText.txt",
               # "/Users/nathanielnowel/PycharmProjects/Substitution-Cipher-Project/plainText.txt")

# atbash_decrypt("/Users/nathanielnowel/PycharmProjects/Substitution-Cipher-Project/cipherText.txt",
                # "/Users/nathanielnowel/PycharmProjects/Substitution-Cipher-Project/plainText.txt")

affine_decrypt("/Users/nathanielnowel/PycharmProjects/Substitution-Cipher-Project/cipherText.txt",
               "/Users/nathanielnowel/PycharmProjects/Substitution-Cipher-Project/plainText.txt", 5, 8)
