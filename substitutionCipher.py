alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

plaintext_Dict = {}
for num in range(1, 27):
    plaintext_Dict[num] = ""
counter = 0
for letter in alphabet:
    counter += 1
    plaintext_Dict[counter] = letter


def key_error(key):
    letterList = []
    for let in key:
        if let in letterList:
            return False
        letterList.append(let)
        return True


def substitution_encrypt(plaintext_file, ciphertext_file, key):
    alphabetList = alphabet.copy()
    ciphertext_Dict = {}
    for numb in range(1, 27):
        ciphertext_Dict[numb] = ""
    if key_error(key) == False:
        print("Key not valid")

    try:
        read_file = open(plaintext_file)
    except:
        print("Cannot open input file")
    try:
        write_file = open(ciphertext_file, "w")
    except:
        print("Cannot open output file")

    for let in key:
        alphabetList.remove(let)

    cipherList = []
    for let in key:
        cipherList.append(let)
    for let in alphabetList:
        cipherList.append(let)

    loc_counter = 0
    for let in cipherList:
        loc_counter += 1
        ciphertext_Dict[loc_counter] = let

    for let in read_file:
        if let not in alphabet:
            # every single char is coming into this if-block for some reason
            write_file.write(let)
        for key in plaintext_Dict.keys():
            # not writing anything into output file for some reason
            if plaintext_Dict[key] == let:  # finds the key corresponding to current letter
                write_file.write(ciphertext_Dict[key])  # writes the letter at that key in the encrypted dict
            else:
                continue
    read_file.close()
    write_file.close()


substitution_encrypt("/Users/nathanielnowel/PycharmProjects/Substitution-Cipher-Project/plainText.txt",
                     "/Users/nathanielnowel/PycharmProjects/Substitution-Cipher-Project/cipherText.txt",
                     "zebras")
