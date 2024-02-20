def ubah_huruf(sentence):
    pattern = ""
    shift_amount = 10 

    for char in sentence:
        if char.isalpha():
            is_upper = char.isupper()
            index = ord(char.upper()) - ord('A')
            encrypted_index = (index + shift_amount) % 26
            encrypted_char = chr(encrypted_index + ord('A'))
            pattern += encrypted_char if is_upper else encrypted_char.lower()
        else:
            pattern += char

    return pattern

if __name__ == '__main__':
    print(ubah_huruf("SEPULSA OKE")) # COZEVCK YUO
    print(ubah_huruf("ALTERRA ACADEMY")) # KVDOBBK KMKNOWI
    print(ubah_huruf("INDONESIA")) # SXNYXOCSK
    print(ubah_huruf("GOLANG")) # QYVKXQ
    print(ubah_huruf("PROGRAMMER")) # ZBYQBKWWOB