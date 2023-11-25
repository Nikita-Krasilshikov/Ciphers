alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'


def encrypt(text: str, key: str) -> str:
    res = ''
    key_index = 0
    for c in text:
        sym_pos = alphabet.find(c.lower())
        key_pos = alphabet.find(key[key_index % len(key)].lower())
        if sym_pos != -1:
            res += alphabet[(sym_pos + key_pos) % len(alphabet)]
            key_index += 1
        else:
            res += c
    return res


def decrypt(text: str, key: str) -> str:
    res = ''
    key_index = 0
    for c in text:
        sym_pos = alphabet.find(c.lower())
        key_pos = alphabet.find(key[key_index % len(key)].lower())
        if sym_pos != -1:
            res += alphabet[(sym_pos - key_pos) % len(alphabet)]
            key_index += 1
        else:
            res += c
    return res


key = open('key.txt').read()
print(decrypt(encrypt(open('input.txt').read(), key), key))
