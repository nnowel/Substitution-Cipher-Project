alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

plaintext_Dict = {}                       # create global alphabet dict
counter = 0
for let in alphabet:
    counter += 1
    plaintext_Dict[let] = counter


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
        print(char)
        if char not in alphabet:          # if special char, just write, don't encrypt
            encryptedLine += char
        else:
            loc = plaintext_Dict[char]        # determines location of current char in alphabet
        # encryptedLine += cipherDict[loc]   loc would be an int, which is not a key and can't be used
            for key in cipherDict.keys():     # loops through keys in cipher dict until the letter
                if cipherDict[key] == loc:    # corresponding to correct location is found
                    encryptedLine += key
    return encryptedLine

# def decrypt():


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
    read_file.close()
    write_file.close()


def keyword_encrypt(plaintext_file, ciphertext_file, keyword):
    if key_error(keyword) == False:
        print("Key not valid")
    try:
        read_file = open(plaintext_file)
    except:
        print("Cannot open input file")
    try:
        write_file = open(ciphertext_file, "w")
    except:
        print("Cannot open output file")
    alphabetList = alphabet.copy()         # creating cipher list from keyword
    cipherList = []
    for letter in keyword:
        alphabetList.remove(letter)
        cipherList.append(letter)
    for letter in alphabetList:
        cipherList.append(letter)
    for line in read_file:                  # encrypt
        write_file.write(encrypt(line, cipherList))
    read_file.close()
    write_file.close()


cipherList1 = ['e', 'b', 'c', 'd', 'a', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


substitution_encrypt("/Users/nathanielnowel/PycharmProjects/Substitution-Cipher-Project/plainText.txt",
                     "/Users/nathanielnowel/PycharmProjects/Substitution-Cipher-Project/cipherText.txt",
                     cipherList1)

keyword_encrypt()
