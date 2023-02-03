alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

textDict = {}                       # create global alphabet dict
counter = 0
for let in alphabet:
    counter += 1
    textDict[let] = counter


def key_error(key):                       # checks key for duplicate letters
    letterList = []
    for letter in key:
        if letter in letterList:
            return False
        letterList.append(letter)
        return True


def encrypt(line, cipherList):
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
    cipherDict = {}
    let_counter = 0
    for char in cipherList:  # create cipher dict
        let_counter += 1
        cipherDict[char] = let_counter
    decryptedLine = ""
    for char in line:
        if char not in alphabet:  # if special char, just write, don't encrypt
            decryptedLine += char
        else:
            loc = cipherDict[char]      # determines location of current char in cipher dict
            for key in textDict.keys():  # loops through letters in alphabet until the letter
                if textDict[key] == loc:  # corresponding to correct location is found
                    decryptedLine += key
    return decryptedLine


def substitution_encrypt(textFile, cipherFile, cipherList):
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
    alphabetList = alphabet.copy()  # creating cipher list from keyword
    cipherList = []
    for letter in keyword:
        alphabetList.remove(letter)
        cipherList.append(letter)
    for letter in alphabetList:
        cipherList.append(letter)
    print(cipherList)
    return cipherList


def keyword_encrypt(textFile, cipherFile, keyword):
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
    try:
        read_file = open(textFile)
    except:
        print("Cannot open input file")
    try:
        write_file = open(cipherFile, "w")
    except:
        print("Cannot open output file")
    alphabetList = alphabet.copy()
    cipherList = []
    for i in range(len(alphabetList)):
        num = (i+shift) % len(alphabetList)   # the modulo prevents the index from being out of range
        cipherList.append(alphabetList[num])  # ex: 27 % 26 returns 1
    for line in read_file:
        write_file.write(encrypt(line, cipherList))


general_cipherList1 = ['e', 'b', 'c', 'd', 'a', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

cipherList1 = ['z', 'e', 'b', 'r', 'a', 's', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 't', 'u',
 'v', 'w', 'x', 'y']

# substitution_decrypt("/Users/nathanielnowel/PycharmProjects/Substitution-Cipher-Project/plainText.txt",
                    # "/Users/nathanielnowel/PycharmProjects/Substitution-Cipher-Project/cipherText.txt",
                    # cipherList1)

keyword_decrypt("/Users/nathanielnowel/PycharmProjects/Substitution-Cipher-Project/cipherText.txt",
                "/Users/nathanielnowel/PycharmProjects/Substitution-Cipher-Project/plainText.txt", "zebras")

# caesar_encrypt("/Users/nathanielnowel/PycharmProjects/Substitution-Cipher-Project/plainText.txt",
                # "/Users/nathanielnowel/PycharmProjects/Substitution-Cipher-Project/cipherText.txt", 23)
