def encrypt(text,s):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)

        else:
            result += chr((ord(char) + s - 97) % 26 +97)

    return result



def decrypt(text,s):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)

        else:
            result += chr((ord(char) + s - 97) % 26 +97)

    return result

while True:
    
    print("\n1.Encryption")
    print("2.Decryption")
    print("3.Exit")
    choice = int(input("Enter the choice: "))

    if choice == 1:
        text = input("Enter the text to encrypt: ")
        s = 3
        print("Text: " + text)
        str(s)
        print("Cipher: " + encrypt(text,s))

    elif choice == 2:
        text = input("Enter the text to Decrypt: ")
        s = -3
        print("Text: " + text)
        str(s)
        print("Cipher: " + decrypt(text,s))

    elif choice == 3:
        print("Exit")
        break
    

