def caesar_encrypt(enc_text):
    encrypted_text = ""
    key = int(input("\n What is the key length you want to encrypt in? \n\n Choose any number between 1 and 25 \n"))
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    alphabets = [*alphabets]
    for word in enc_text.split():
        encrypted_word = ""
        for letter in word:
            new_index = (alphabets.index(letter) + key) % len(alphabets)
            encrypted_word += alphabets[new_index]
        encrypted_text += encrypted_word + " "
    return encrypted_text.rstrip()


def caesar_decrypt(dec_text):
    decrypted_text = ""
    key = int(input("\n What is the decryption key length? \n\n Choose any number between 1 and 25 \n"))
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    alphabets = [*alphabets]
    for word in dec_text.split():
        decrypted_word = ""
        for letter in word:
            new_index = (alphabets.index(letter) - key) % len(alphabets)
            decrypted_word += alphabets[new_index]
        decrypted_text += decrypted_word + " "
    return decrypted_text.rstrip()

def vig_encrypt(enc_text):
    key = input("\n enter the key with which you want this encrypted\n")
    key = key.upper()
    enc_text = enc_text.upper()
    encrypted_text = ""
    for i in range(len(enc_text)):
        if enc_text[i] == " ":
            encrypted_text += " "
        else:
            enc_text_index = ord(enc_text[i]) - ord("A")
            key_index = ord(key[i % len(key)]) - ord("A")
            new_index = (enc_text_index + key_index) % 26
            new_char = chr(ord("A") + new_index)
            encrypted_text += new_char
    return encrypted_text

def vig_decrypt(dec_text):
    key = input("\n enter the key with which you want this decrypted\n")
    key = key.upper()
    dec_text = dec_text.upper()
    decrypted_text = ""
    for i in range(len(dec_text)):
        if dec_text[i] == " ":
            decrypted_text += " "
        else:
            dec_text_index = ord(dec_text[i]) - ord("A")
            key_index = ord(key[i % len(key)]) - ord("A")
            new_index = (dec_text_index - key_index) % 26
            new_char = chr(ord("A") + new_index)
            decrypted_text += new_char
    return decrypted_text
