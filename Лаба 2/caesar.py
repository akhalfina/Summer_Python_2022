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

def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    result = ''
    for c in plaintext:
        result = result + encrypt(c, shift)
    return result

def decrypt_caesar(plaintext: str, shift: int = 3) -> str:
    result = ''
    for c in plaintext:
        result = result + decrypt(c, shift)
    return result
