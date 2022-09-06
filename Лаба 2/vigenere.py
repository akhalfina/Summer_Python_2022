dic = { "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 14, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25 }

def get_shift(keyword, currentIndex):
    newIndex = 0 if currentIndex == len(keyword) - 1 else currentIndex + 1
    return (dic[keyword[currentIndex]], newIndex)

def encrypt(char, shift):
    charNum = ord(char)
    newCharNum = charNum + shift
    if (ord("A") <= charNum <= ord("Z")) and (newCharNum > ord("Z")):
        newCharNum = newCharNum - ord("Z") + ord("A") - 1
    if (ord("a") <= charNum <= ord("z")) and (newCharNum > ord("z")):
        newCharNum = newCharNum - ord("z") + ord("a") - 1
    if (charNum < ord("A") or charNum > ord('z') or (ord('Z') < charNum < ord('a'))):
        newCharNum = charNum
    return chr(newCharNum)

def decrypt(char, shift):
    charNum = ord(char)
    newCharNum = charNum - shift
    if (ord("A") <= charNum <= ord("Z")) and (newCharNum < ord("A")):
        newCharNum = newCharNum - ord("A") + ord("Z") + 1
    if (ord("a") <= charNum <= ord("z")) and (newCharNum < ord("a")):
        newCharNum = newCharNum - ord("a") + ord("z") + 1
    if (charNum < ord("A") or charNum > ord('z') or (ord('Z') < charNum < ord('a'))):
        newCharNum = charNum
    return chr(newCharNum)

def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ""
    shiftIndex = 0
    keyword = keyword.upper()
    for c in plaintext:
        (shift, shiftIndex) = get_shift(keyword, shiftIndex)
        ciphertext += encrypt(c, shift)
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    plaintext = ""
    shiftIndex = 0
    for c in ciphertext:
        (shift, shiftIndex) = get_shift(keyword, shiftIndex)
        plaintext += decrypt(c, shift)
    return plaintext
