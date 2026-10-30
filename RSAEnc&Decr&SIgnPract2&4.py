import rsa

public_key, private_key = rsa.newkeys(1024)
print(public_key)
print("\n", private_key)

with open ("public.pem", "wb") as f:
    f.write(public_key.save_pkcs1("PEM"))

with open ("private.pem", "wb") as f:
    f.write(private_key.save_pkcs1("PEM"))

with open ("public.pem", "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

with open ("private.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

message = input("\nEnter the secrete message you want to share = ")

print("Select operation")
print("1: Confidentiality - Encryption ")
print("2: Confidentiality - Decryption ")
print("3: Digital signature ")
print("4: Exit ")

while True:
    ch = int(input("Enter choice for operation = "))
    if ch == 1:
        encrypted_message = rsa.encrypt(message.encode(), public_key)
        print("Encrypted message is = ", encrypted_message)

    elif ch == 2:
        encrypted_message = rsa.encrypt(message.encode(), public_key)
        decrypted_message = rsa.decrypt(encrypted_message, private_key)
        print("Decrypted message is = ", decrypted_message.decode())

    elif ch == 3:
        digi_sign = rsa.sign(message.encode(), private_key, "SHA-256")
        print("Digital signature is = ", digi_sign)
        option = input("Do you want to verify it (y/n): ")
        if option == 'y':
            print(rsa.verify(message.encode(), digi_sign, public_key))

    else:
        break
        
