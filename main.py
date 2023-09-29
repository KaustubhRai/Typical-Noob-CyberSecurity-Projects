import sys
sys.path.append("Text Encryption-Decryption using various Algorithms")
import encryptDecrypt

def main():
    print("\n Welcome to a shitty Cyber Knife, multiple tools in one made by your's truly \n")
    while True:
        print("\nWhat tool do you want to use \n 1] Encryption-Decryption \n 2] Password Analyzer \n 3] Keylogger \n 4] Packet Sniffer \n 5] Network Traffic Analyzer \n 6] Host-Based Intrusion Detection \n 7] Network-Based Intrusion Detection\n")
        tool_decision = int(input("\n Any number from 1-7 as your decision-"))
        match tool_decision:
            case 1:
                print("\nYou want to go ahead with Encryption-Decryption\n")
                spam = input("Enter some text for encryption or decryption \n")
                decision = int(input("\nWhat do you want to do?\n 1] Encrypt \n 2] Decrypt\n"))
                match decision:
                    case 1:
                        print("\n what algorithm do you want to encrypt in?\n a] Caesar Cipher\n b] Substitution Cipher \n c] Vigenère Cipher \n d] Transposition Cipher \n e] DES \n f] AES \n g] RSA \n h] Diffie-Hellman Key Exchange \n i] Elliptic Curve Cryptography \n")
                        encryption_decision = input()
                        match encryption_decision:
                            case "a":
                                print("\nChoose to go with Caesar Cipher\n")
                                text = encryptDecrypt.caesar_encrypt(spam)
                                print("Encrypted Text is -",text, "\n")
                            case "b":
                                print("\nChoose to go with Substitution Cipher\n")
                                text = encryptDecrypt.caesar_encrypt(spam)
                                print("Encrypted Text is -",text, "\n")
                            case "c":
                                print("\nChoose to go with Vigenère Cipher\n")
                                text = encryptDecrypt.vig_encrypt(spam)
                                print("Encrypted Text is -",text, "\n")
                            case "d":
                                print("\nChoose to go with Transposition Cipher\n")
                            case "e":
                                print("\nChoose to go with DES\n")
                            case "f":
                                print("\nChoose to go with AES\n")
                            case "g":
                                print("\nChoose to go with RSA\n")
                            case "h":
                                print("\nChoose to go with Diffie-Hellman Key Exchange\n")
                            case "i":
                                print("\nChoose to go with Elliptic Curve Cryptography\n")

                    case 2: 
                        print("\n what algorithm do you want to decrypt in?\n a] Caesar Cipher\n b] Substitution Cipher \n c] Vigenère Cipher \n d] Transposition Cipher \n e] DES \n f] AES \n g] RSA \n h] Diffie-Hellman Key Exchange \n i] Elliptic Curve Cryptography \n")
                        decryption_decision = input()
                        match decryption_decision:
                            case "a":
                                print("\nChoose to go with Caesar Cipher\n")
                                text = encryptDecrypt.caesar_decrypt(spam)
                                print("Decrypted Text is -",text, "\n")
                            case "b":
                                print("\nChoose to go with Substitution Cipher\n")
                                text = encryptDecrypt.caesar_decrypt(spam)
                                print("Decrypted Text is -",text, "\n")
                            case "c":
                                print("\nChoose to go with Vigenère Cipher\n")
                                text = encryptDecrypt.vig_decrypt(spam)
                                print("Decrypted Text is -",text, "\n")
                            case "d":
                                print("\nChoose to go with Transposition Cipher\n")
                            case "e":
                                print("\nChoose to go with DES\n")
                            case "f":
                                print("\nChoose to go with AES\n")
                            case "g":
                                print("\nChoose to go with RSA\n")
                            case "h":
                                print("\nChoose to go with Diffie-Hellman Key Exchange\n")
                            case "i":
                                print("\nChoose to go with Elliptic Curve Cryptography\n")
        continue_or_exit = input("\n Do you want to continue (y/n)? ")
        if continue_or_exit != "y":
            break

if __name__ == "__main__":
    main()

