def encrypt(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''

    for char in message.lower():
        if char == ' ':
            result += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            result += alphabet[new_index]

    return result

def decrypt(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''

    for char in message.lower():
        if char == ' ':
            result += char
        else:
            index = alphabet.find(char)
            new_index = (index - offset) % len(alphabet)
            result += alphabet[new_index]

    return result

def menu():
    running = True
    
    while running:
        print("\nShift Cipher")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Keluar")

        choice = int(input("Masukkan opsi: "))

        if choice == 1:
            text = input("Masukkan kalimat yang ingin di enkripsi: ")
            shift = int(input("Masukkan kunci: "))
            encrypted_text = encrypt(text, shift)
            print('Plain text:', text)
            print('Encrypted text:', encrypted_text)

        elif choice == 2:
            text = input("Masukkan kalimat yang ingin di dekripsi: ")
            shift = int(input("Masukkan kunci: "))
            decrypted_text = decrypt(text, shift)
            print('Cipher text:', text)
            print('Decrypted text:', decrypted_text)

        elif choice == 3:
            print("Terima kasih telah menggunakan program ini.")
            running = False

        else:
            print("Salah masukkan opsi menu. Silahkan coba ulang.")

menu()
