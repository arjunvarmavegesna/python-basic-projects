print("Created By Arjun Varma")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

user = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

def encrypt(new_text, new_shift):
    cipher_text = ""
    for letter in new_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + new_shift) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    print(f"YOUR ENCRYPTED TEXT: {cipher_text}")

def decrypt(org_text, org_shift):
    plain_text = ""
    for letter in org_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position - org_shift) % 26
            plain_text += alphabet[new_position]
        else:
            plain_text += letter
    print(f"YOUR DECRYPTED TEXT: {plain_text}")

if user == "encode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26
    encrypt(new_text=text, new_shift=shift)

elif user == "decode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26
    decrypt(org_text=text, org_shift=shift)

else:
    print("INVALID CHOICE! Please type 'encode' or 'decode'.")
