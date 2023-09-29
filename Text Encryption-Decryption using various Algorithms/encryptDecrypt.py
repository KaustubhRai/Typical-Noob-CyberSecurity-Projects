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