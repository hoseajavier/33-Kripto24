def vigenere_encrypt(plaintext, key):
    key = key.upper()
    ciphertext = ''
    key_index = 0
    
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            if char.isupper():
                ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            elif char.islower():
                ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            key_index = (key_index + 1) % len(key)
        else:
            ciphertext += char

    return ciphertext

def vigenere_decrypt(ciphertext, key):
    key = key.upper()
    plaintext = ''
    key_index = 0
    
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            if char.isupper():
                plaintext += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            elif char.islower():
                plaintext += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            key_index = (key_index + 1) % len(key)
        else:
            plaintext += char

    return plaintext

def menu():
    while True:
        print("\n=== Vigenère Cipher ===")
        print("1. Enkripsi (Encrypt)")
        print("2. Dekripsi (Decrypt)")
        print("3. Keluar (Exit)")

        choice = input("Pilih opsi (1/2/3): ")

        if choice == '1':
            plaintext = input("Masukkan plaintext: ")
            key = input("Masukkan key: ")
            ciphertext = vigenere_encrypt(plaintext, key)
            print("Hasil enkripsi:", ciphertext)

        elif choice == '2':
            ciphertext = input("Masukkan ciphertext: ")
            key = input("Masukkan key: ")
            plaintext = vigenere_decrypt(ciphertext, key)
            print("Hasil dekripsi:", plaintext)

        elif choice == '3':
            print("Keluar dari program.")
            break

        else:
            print("Opsi tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    menu()
