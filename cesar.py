import string

def caeser_chipher(text, alphabets, shift):
    def shift_alphabet(alphabet):
        return alphabet[shift:] + alphabet[:shift]
    
    shift_alphabets = tuple(map(shift_alphabet, alphabets))
    final_alphabet = "".join(alphabets)
    final_shifted_alphabet = "".join(shift_alphabets)
    table = str.maketrans(final_alphabet, final_shifted_alphabet)
    return text.translate(table)

original_text = "Hello World!"
print(caeser_chipher(original_text,[string.ascii_letters, string.punctuation], 3))

original_text = "hello world"
shift = 26
alphabet = string.ascii_letters
shifted = alphabet[shift:] + alphabet[:shift]
table = str.maketrans(alphabet,shifted)
encrypted = original_text.translate(table)
print(encrypted)
