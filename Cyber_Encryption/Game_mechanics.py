def zigzag_encrypt(text, rails):
    if rails == 1:
        return text

    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1

    for char in text:
        fence[rail].append(char)
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1

    return ''.join(''.join(row) for row in fence)

def zigzag_decrypt(cipher, rails):
    if rails == 1:
        return cipher

    fence = [[] for _ in range(rails)]
    n = len(cipher)

    rail_pattern = []
    rail = 0
    direction = 1
    for _ in range(n):
        rail_pattern.append(rail)
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1

    counts = [rail_pattern.count(r) for r in range(rails)]

    index = 0
    for r in range(rails):
        fence[r] = list(cipher[index:index+counts[r]])
        index += counts[r]

    result = []
    rail_indices = [0]*rails
    for r in rail_pattern:
        result.append(fence[r][rail_indices[r]])
        rail_indices[r] += 1

    return ''.join(result)
def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            offset = shift if mode == 'encrypt' else -shift
            result += chr((ord(char) - base + offset) % 26 + base)
        else:
            result += char
    return result
def vigenere_encrypt(text, key):
    result = ''
    key = key.upper()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

def vigenere_decrypt(text, key):
    result = ''
    key = key.upper()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result
def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            offset = shift if mode == 'encrypt' else -shift
            result += chr((ord(char) - base + offset) % 26 + base)
        else:
            result += char
    return result
def azby_encrypt(text):
    result = ''
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr(155 - ord(char))
            else:
                result += chr(219 - ord(char))
        else:
            result += char
    return result

def azby_decrypt(text):
    return azby_encrypt(text)  # Symmetric