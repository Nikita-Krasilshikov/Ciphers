def crypt(text: str, key: str, func):
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    res = ''
    key_index = 0
    for c in text:
        sym_pos = alphabet.find(c.lower())
        key_pos = alphabet.find(key[key_index % len(key)].lower())
        if sym_pos != -1:
            res += func(sym_pos, key_pos, alphabet)
            key_index += 1
        else:
            res += c
    return res


def encrypt(text: str, key: str) -> str:
    return crypt(text, key, lambda sym_pos, key_pos, alphabet: alphabet[(sym_pos + key_pos) % len(alphabet)])


def decrypt(text: str, key: str) -> str:
    return crypt(text, key, lambda sym_pos, key_pos, alphabet: alphabet[(sym_pos - key_pos) % len(alphabet)])


key = open('key.txt').read()
print(decrypt(encrypt(open('input.txt').read(), key), key))
