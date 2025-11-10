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
