import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    print(f"alphabet: {alphabet}")
    str1 = str1.lower()
    for letter in str1:
        if letter in alphabet:
            alphabet = alphabet.replace(letter, '')
    if len(alphabet) == 0:
        print("Is a pangram")
    else:
        print("Not a pangram")
    print(f"alphabet: {alphabet} ")

ispangram("The quick brown fox jumps over the lazy dog")
ispangram("The quick")