# Caesar Cipher implementation in Python

def encrypt(text, shift):
    result = ""
    
    # Loop through each character in the text
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Leave non-alphabetic characters as is
            result += char
    
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


if __name__ == "__main__":
    choice = input("Type 'encrypt' to encrypt, 'decrypt' to decrypt: ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))
    
    if choice == 'encrypt':
        encrypted_message = encrypt(message, shift)
        print(f"Encrypted Message: {encrypted_message}")
    elif choice == 'decrypt':
        decrypted_message = decrypt(message, shift)
        print(f"Decrypted Message: {decrypted_message}")
    else:
        print("Invalid choice! Please type 'encrypt' or 'decrypt'.")
