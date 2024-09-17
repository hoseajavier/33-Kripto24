import numpy as np

def char_to_index(char):
    return ord(char) - ord('A')

def index_to_char(index):
    return chr(index + ord('A'))

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def find_mod_inverse(a, m):
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        return None
    else:
        return x % m

def modular_inverse(matrix, mod):
    determinant = int(round(np.linalg.det(matrix)))
    det_inv = find_mod_inverse(determinant % mod, mod)
    if det_inv is None:
        return None
    matrix_inv = np.round(det_inv * np.linalg.inv(matrix) * determinant).astype(int) % mod
    return matrix_inv

def validate_key(matrix):
    determinant = int(round(np.linalg.det(matrix)))
    if determinant % 2 == 0 or determinant % 13 == 0:
        return False
    return True

def generate_key_matrix(size):
    key_data = list(map(int, input("Masukkan elemen matriks kunci (pisahkan dengan spasi): ").split()))
    if len(key_data) != size * size:
        print(f"Jumlah elemen tidak sesuai. Diperlukan {size*size} elemen.")
        return None
    key_matrix = np.array(key_data).reshape(size, size) % 26
    return key_matrix

def prepare_text(prompt):
    text = input(prompt + ": ").replace(" ", "").upper()
    return text

def adjust_block_size(text):
    length = len(text)
    if length >= 9:
        return 3 
    elif length >= 4:
        return 2 
    else:
        print("Jumlah karakter tidak cukup untuk membuat matriks 2x2 atau 3x3.")
        return None

def hill_cipher_process(operation, message, key_matrix, block_size):
    determinant = int(round(np.linalg.det(key_matrix)))  # Menghitung determinan

    if determinant % 2 == 0 or determinant % 13 == 0:
        print("Determinant tidak valid (harus ganjil dan tidak sama dengan 13).")
        return

    if len(message) % block_size != 0:
        message += message[-1] * (block_size - len(message) % block_size)

    message_indices = [char_to_index(char) for char in message]
    message_matrix = np.array(message_indices).reshape(-1, block_size)
    result_matrix = np.array([])

    if operation == 'decrypt':
        mod_inv_det = find_mod_inverse(determinant % 26, 26)
        if mod_inv_det is None:
            print("Tidak dapat menghitung invers determinan. Dekripsi gagal.")
            return
        inv_key_matrix = mod_inv_det * np.round(np.linalg.inv(key_matrix) * determinant).astype(int) % 26
        print("\nMatriks Kunci untuk Dekripsi (dihitung dari invers):")
        print(inv_key_matrix)
        key_matrix = inv_key_matrix

    else:
        print("\nMatriks Kunci untuk Enkripsi:")
        print(key_matrix)

    for row in message_matrix:
        result_vector = np.dot(key_matrix, row) % 26
        result_matrix = np.append(result_matrix, result_vector)

    result_message = ''.join([index_to_char(int(num)) for num in result_matrix])
    return result_message

def textMatrix(text, size):
    indices = [char_to_index(char) for char in text]
    return np.array(indices).reshape(size, size)

def findKey(pt, ct, key_length):
    if len(pt) != len(ct):
        print("Plaintext and Ciphertext doesn't have the same length!")
        return None
    check = True
    key = None
    while len(pt) >= 4 and check:
        pt_chunk = pt[:4]
        ct_chunk = ct[:4]
        pt = pt[2:]
        ct = ct[2:]
        pt_matrix = textMatrix(pt_chunk, 2).flatten()
        ct_matrix = textMatrix(ct_chunk, 2).flatten()
        pt_matrix2 = np.zeros((2, 2), dtype=int)
        ct_matrix2 = np.zeros((2, 2), dtype=int)
        index = 0
        for i in range(2):
            for j in range(2):
                pt_matrix2[j, i] = pt_matrix[index]
                ct_matrix2[j, i] = ct_matrix[index]
                index += 1
        if validate_key(pt_matrix2):
            pt_inv = modular_inverse(pt_matrix2, key_length)
            if pt_inv is not None:
                key = np.matmul(ct_matrix2, pt_inv) % 26
                check = False
    if check:
        print("Cannot find key: There is no combination of plaintext matrix that is invertible modulo 26")
    return key

def main_menu():
    while True:
        print("\n====== MENU UTAMA ======")
        print("1. Enkripsi\n2. Dekripsi\n3. Temukan Kunci\n4. Keluar")
        option = input("Pilih opsi: ")

        if option == '1' or option == '2':
            block_size = int(input("\nMasukkan ukuran matriks kunci (n x n): "))
            if block_size != 2:
                print("Hanya mendukung ukuran matriks 2x2.")
                continue

            key_matrix = generate_key_matrix(block_size)
            if key_matrix is None:
                continue

            text = ''
            while len(text) < block_size:
                text = prepare_text("Masukkan teks")
                if len(text) < block_size:
                    print("Jumlah karakter harus kelipatan dari ukuran matriks.")

            result = hill_cipher_process("encrypt" if option == '1' else "decrypt", text, key_matrix, block_size)
            if result is not None:
                if option == '1':
                    print("\nHasil Enkripsi:")
                else:
                    print("\nHasil Dekripsi:")
                print(result)

        elif option == '3':
            plain_text = prepare_text("Masukkan plaintext")
            cipher_text = prepare_text("Masukkan ciphertext")

            key_matrix = findKey(plain_text, cipher_text, 26)
            if key_matrix is not None:
                print("\nMatriks Kunci:")
                print(key_matrix)

        elif option == '4':
            break

        else:
            print("\nPilihan tidak valid.\n")

if __name__ == "__main__":
    main_menu()
