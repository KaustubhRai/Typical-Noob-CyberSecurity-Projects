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
                        print("\n what algorithm do you want to encrypt in?\n a] caesar\n")
                        encryption_decision = input()
                        match encryption_decision:
                            case "a":
                                text = encryptDecrypt.caesar_encrypt(spam)
                                print(text, "\n")
                    case 2: 
                        print("\n what algorithm do you want to decrypt in?\n a] caesar\n")
                        decryption_decision = input()
                        match decryption_decision:
                            case "a":
                                text = encryptDecrypt.caesar_decrypt(spam)
                                print(text, "\n")
        continue_or_exit = input("\n Do you want to continue (y/n)? ")
        if continue_or_exit != "y":
            break

if __name__ == "__main__":
    main()

