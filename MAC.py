import hmac
import hashlib

def generate_mac(message, key):
    if isinstance(message, str):
        message = message.encode('utf-8')

    if isinstance(key, str):
        key = key.encode('utf-8')

    h = hmac.new(key, message, hashlib.sha256)
    return h.hexdigest()


def verify_mac(message, key, mac):
    generated_mac = generate_mac(message, key)
    return generated_mac == mac

message = input("Enter the message whose HMAC is to be generated: ")
key = input("Enter random secret key to create HMAC: ")

mac = generate_mac(message, key)
print("Generated MAC: ",mac)

option = input("Do you want to verify it (y/n): ")
if option =='y':
    is_valid = verify_mac(message, key, mac)
    print("MAC is valid: ", is_valid)
