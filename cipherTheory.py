general_cipherList1 = ['e', 'b', 'c', 'd', 'a', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

cipherList1 = ['z', 'e', 'b', 'r', 'a', 's', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 't', 'u',
 'v', 'w', 'x', 'y']

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

textDict = {}                       # create global alphabet dict
counter = 0
for let in alphabet:
    counter += 1
    textDict[let] = counter

def main_function(textFile, cipherFile):
    try:
        read_file = open(textFile)
    except:
        print("Cannot open input file")
    try:
        write_file = open(cipherFile, "w")
    except:
        print("Cannot open output file")

    cipherType_input = input("Please enter the type of cipher")
    if (cipherType_input == "substitution"):
        sub_cipherList = input("enter your cipher list")
        for line in read_file:
            write_file.write(encrypt(line,sub_cipherList))
    elif (cipherType_input == "keyword"):
        sub_keyword = input("Enter a keyword")
        for line in read_file:
            write_file.write(encrypt(line,keywordListCreator(sub_keyword)))
    elif(cipherType_input == "caesar"):
        sub_ceasar = input("Enter a shift")
        eord = input("eord")
        if eord == "e":
            for line in read_file:
                write_file.write(caesar_encrypt(line,sub_ceasar))
        else:
            for line in read_file:
                write_file.write(caesar_decrypt(line,sub_ceasar))
    elif(cipherType_input == "rot13"):
        for line in read_file:
            write_file.write(caesar_encrypt(line,13))
    elif(cipherType_input == "atbash"):
        for line in read_file:
            write_file.write(atbash_encrypt(line))


def key_error(key):                       # checks key for duplicate letters
    letterList = []
    for letter in key:
        if letter in letterList:
            return False
        letterList.append(letter)
        return True


def encrypt(line, cipherList):
    choice = input("Do you want to Encrypt or decrypt")
    cipherDict = {}
    let_counter = 0
    for char in cipherList:               # create cipher dict
        let_counter += 1
        cipherDict[char] = let_counter
    Line = ""
    for char in line:
        if char not in alphabet:          # if special char, just write, don't encrypt
            Line += char
        elif choice == "e":
            loc = textDict[char]            # determines location of current char in alphabet
            for key in cipherDict.keys():     # loops through keys in cipher dict until the letter
                if cipherDict[key] == loc:    # corresponding to correct location is found
                    Line += key
        else:
            loc = cipherDict[char]      # determines location of current char in cipher dict
            for key in textDict.keys():  # loops through letters in alphabet until the letter
                if textDict[key] == loc:  # corresponding to correct location is found
                    Line += key
    return Line

def keywordListCreator(keyword):
    alphabetList = alphabet.copy()  # creating cipher list from keyword
    cipherList = []
    for letter in keyword:
        alphabetList.remove(letter)
        cipherList.append(letter)
    for letter in alphabetList:
        cipherList.append(letter)
    return cipherList
def keyword_decrypt(cipherFile, textFile, keyword):
    alphabetList = alphabet.copy()  # creating cipher list from keyword
    cipherList = []
    for letter in keyword:
        alphabetList.remove(letter)
        cipherList.append(letter)
    for letter in alphabetList:
        cipherList.append(letter)
    return cipherList


def caesar_encrypt(line, shift):
    alphabetList = alphabet.copy()
    cipherList = []
    for i in range(len(alphabetList)):
        num = (i+shift) % len(alphabetList)   # the modulo prevents the index from being out of range
        cipherList.append(alphabetList[num])  # ex: 27 % 26 returns 1
    return encrypt(line,cipherList)
def caesar_decrypt(line,shift):
    alphabetList = alphabet.copy()
    decrypted_message = ""
    for char in line:
        if char in alphabetList:
            char_index = alphabetList[char]
            char_index = (char_index - shift) % 26
            decrypted_char = alphabetList[char_index]
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message
    

def atbash_encrypt(line):
    cipher_list = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g',
                   'f', 'e', 'd', 'c', 'b', 'a']
    return encrypt(line, cipher_list)
def atbash_decrypt():
    cipher_list = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g',
                   'f', 'e', 'd', 'c', 'b', 'a']
    return encrypt(line, cipher_list)




# substitution_decrypt("/Users/nathanielnowel/PycharmProjects/Substitution-Cipher-Project/plainText.txt",
                    # "/Users/nathanielnowel/PycharmProjects/Substitution-Cipher-Project/cipherText.txt",
                    # cipherList1)

#keyword_decrypt("/Users/nathanielnowel/PycharmProjects/Substitution-Cipher-Project/cipherText.txt",
                #"/Users/nathanielnowel/PycharmProjects/Substitution-Cipher-Project/plainText.txt", "zebras")

# caesar_encrypt("/Users/nathanielnowel/PycharmProjects/Substitution-Cipher-Project/plainText.txt",
                # "/Users/nathanielnowel/PycharmProjects/Substitution-Cipher-Project/cipherText.txt", 23)

main_function('plaintext.txt','cipherText.txt')