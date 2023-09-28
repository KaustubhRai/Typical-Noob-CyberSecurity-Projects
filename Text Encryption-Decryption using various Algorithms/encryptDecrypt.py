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
    
def main():
    print("\n Welcome to a shitty Encryption-Decryption program made by your's truly \n")
    while True:
        spam = input("Enter some text for encryption or decryption \n")
        print("\n Do you want to \n 1] Encrypt \n 2] Decrypt \n ")
        decision = int(input())
        # print(decision)
        match decision:
            case 1:
                print("\n what algorithm do you want to encrypt in?\n a] caesar\n")
                encryption_decision = input()
                match encryption_decision:
                    case "a":
                        text = caesar_encrypt(spam)
                        print(text, "\n")
            case 2: 
                print("\n what algorithm do you want to decrypt in?\n a] caesar\n")
                decryption_decision = input()
                match decryption_decision:
                    case "a":
                        text = caesar_decrypt(spam)
                        print(text, "\n")
        continue_or_exit = input("\n Do you want to continue (y/n)? ")
        if continue_or_exit != "y":
            break

if __name__ == "__main__":
    main()
