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


# Шифратор
def encrypt(text: str, key: str) -> str:
    return crypt(text, key, lambda sym_pos, key_pos, alphabet: alphabet[(sym_pos + key_pos) % len(alphabet)])


# Дешифратор
def decrypt(text: str, key: str) -> str:
    return crypt(text, key, lambda sym_pos, key_pos, alphabet: alphabet[(sym_pos - key_pos) % len(alphabet)])


key = open('key.txt').read()
print(f'Ключ: {key}')

text = open('input.txt').read()
print(f'Текст для шифровки: {text}')

encrypt_text = encrypt(text, key)
print(f'Зашифрованный текст: {encrypt_text}')

open('output.txt', 'w').write(encrypt_text)

decrypt_text = decrypt(open('output.txt').read(), key)
print(f'Расшифрованный текст: {decrypt_text}')
