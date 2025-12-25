

# جدول S-Box
S_BOX = [
    [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
    [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
    [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
    [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
    [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
    [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
    [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
    [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
    [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
    [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
    [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
    [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
    [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
    [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
    [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
    [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]
]

# جدول S-Box معکوس
INV_S_BOX = [
    [0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb],
    [0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb],
    [0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e],
    [0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25],
    [0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92],
    [0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84],
    [0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06],
    [0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b],
    [0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73],
    [0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e],
    [0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b],
    [0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4],
    [0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f],
    [0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef],
    [0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61],
    [0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d]
]

# ثابت‌های دور
ROUND_CONSTANTS = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36]


def text_to_matrix(text):
    # "تبدیل متن به ماتریس حالت AES (4x4) - column-major order
    # تبدیل به بایت‌ها
    bytes_list = [ord(c) for c in text]
    
    # اضافه کردن padding
    padding_len = 16 - (len(bytes_list) % 16)
    if padding_len == 16:
        padding_len = 0
    while len(bytes_list) % 16 != 0:
        bytes_list.append(padding_len)
    
    # تبدیل به ماتریس 4x4 (column-major: state[i][j] = byte[i + 4*j])
    matrix = []
    for i in range(0, len(bytes_list), 16):
        block = bytes_list[i:i+16]
        state = [[block[i + 4*j] for j in range(4)] for i in range(4)]
        matrix.append(state)
    
    return matrix


def matrix_to_text(matrix, remove_padding=True):
    #تبدیل ماتریس حالت به متن
    text = ''
    for state in matrix:
        for j in range(4):
            for i in range(4):
                text += chr(state[i][j])
    
    # حذف padding (PKCS7)
    if remove_padding and len(text) > 0:
        padding_len = ord(text[-1])
        if padding_len > 0 and padding_len <= 16:
            # بررسی صحت padding
            is_valid_padding = True
            for i in range(padding_len):
                if ord(text[-(i+1)]) != padding_len:
                    is_valid_padding = False
                    break
            if is_valid_padding:
                text = text[:-padding_len]
    
    return text


def key_to_matrix(key):
    # تبدیل کلید به ماتریس - column-major order
    key_bytes = [ord(c) for c in key[:16]]
    while len(key_bytes) < 16:
        key_bytes.append(0)
    key_bytes = key_bytes[:16]
    
    # column-major: key_matrix[i][j] = key_bytes[i + 4*j]
    key_matrix = [[key_bytes[i + 4*j] for j in range(4)] for i in range(4)]
    return key_matrix


def sub_bytes(state, inv=False):
    # تبدیل SubBytes
    sbox = INV_S_BOX if inv else S_BOX
    for i in range(4):
        for j in range(4):
            row = state[i][j] >> 4
            col = state[i][j] & 0x0f
            state[i][j] = sbox[row][col]
    return state


def shift_rows(state, inv=False):
    # تبدیل ShiftRows
    if inv:
        # ShiftRows معکوس
        state[1] = [state[1][3], state[1][0], state[1][1], state[1][2]]
        state[2] = [state[2][2], state[2][3], state[2][0], state[2][1]]
        state[3] = [state[3][1], state[3][2], state[3][3], state[3][0]]
    else:
        # ShiftRows عادی
        state[1] = [state[1][1], state[1][2], state[1][3], state[1][0]]
        state[2] = [state[2][2], state[2][3], state[2][0], state[2][1]]
        state[3] = [state[3][3], state[3][0], state[3][1], state[3][2]]
    return state


def gmul(a, b):
    # ضرب در میدان GF(2^8)
    p = 0
    for i in range(8):
        if b & 1:
            p ^= a
        hi_bit_set = a & 0x80
        a <<= 1
        if hi_bit_set:
            a ^= 0x1b
        b >>= 1
    return p & 0xff


def mix_columns(state, inv=False):
    #تبدیل MixColumns
    new_state = [[0 for _ in range(4)] for _ in range(4)]
    
    if inv:
        # MixColumns معکوس
        for c in range(4):
            new_state[0][c] = gmul(0x0e, state[0][c]) ^ gmul(0x0b, state[1][c]) ^ \
                             gmul(0x0d, state[2][c]) ^ gmul(0x09, state[3][c])
            new_state[1][c] = gmul(0x09, state[0][c]) ^ gmul(0x0e, state[1][c]) ^ \
                             gmul(0x0b, state[2][c]) ^ gmul(0x0d, state[3][c])
            new_state[2][c] = gmul(0x0d, state[0][c]) ^ gmul(0x09, state[1][c]) ^ \
                             gmul(0x0e, state[2][c]) ^ gmul(0x0b, state[3][c])
            new_state[3][c] = gmul(0x0b, state[0][c]) ^ gmul(0x0d, state[1][c]) ^ \
                             gmul(0x09, state[2][c]) ^ gmul(0x0e, state[3][c])
    else:
        # MixColumns عادی
        for c in range(4):
            new_state[0][c] = gmul(0x02, state[0][c]) ^ gmul(0x03, state[1][c]) ^ \
                             state[2][c] ^ state[3][c]
            new_state[1][c] = state[0][c] ^ gmul(0x02, state[1][c]) ^ \
                             gmul(0x03, state[2][c]) ^ state[3][c]
            new_state[2][c] = state[0][c] ^ state[1][c] ^ \
                             gmul(0x02, state[2][c]) ^ gmul(0x03, state[3][c])
            new_state[3][c] = gmul(0x03, state[0][c]) ^ state[1][c] ^ \
                             state[2][c] ^ gmul(0x02, state[3][c])
    
    return new_state


def add_round_key(state, round_key):
    # تبدیل AddRoundKey
    for i in range(4):
        for j in range(4):
            state[i][j] ^= round_key[i][j]
    return state


def rot_word(word):
    # چرخش کلمه
    return [word[1], word[2], word[3], word[0]]


def sub_word(word):
    # تبدیل SubBytes روی کلمه
    for i in range(4):
        row = word[i] >> 4
        col = word[i] & 0x0f
        word[i] = S_BOX[row][col]
    return word


def key_expansion(key):
    # توسعه کلید
    # تبدیل کلید به words (column-major: word j = [key[0][j], key[1][j], key[2][j], key[3][j]])
    w = [[key[i][j] for i in range(4)] for j in range(4)]
    
    for i in range(4, 44):
        temp = w[i-1][:]
        if i % 4 == 0:
            temp = sub_word(rot_word(temp))
            temp[0] ^= ROUND_CONSTANTS[i//4 - 1]
        w.append([w[i-4][j] ^ temp[j] for j in range(4)])
    
    return w


def get_round_key(expanded_key, round_num):
    # دریافت کلید دور - column-major order
    start = round_num * 4
    # expanded_key[i] یک word (4 بایت) است
    # باید به صورت column-major تبدیل شود
    key = [[expanded_key[start + j][i] for j in range(4)] for i in range(4)]
    return key


def encrypt_aes_block(state, expanded_key):
    # رمزنگاری یک بلاک 128 بیتی
    # AddRoundKey اولیه
    state = add_round_key(state, get_round_key(expanded_key, 0))
    
    # 9 دور کامل
    for round_num in range(1, 10):
        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, get_round_key(expanded_key, round_num))
    
    # دور نهایی (بدون MixColumns)
    state = sub_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state, get_round_key(expanded_key, 10))
    
    return state


def decrypt_aes_block(state, expanded_key):
    # رمزگشایی یک بلاک 128 بیتی
    # AddRoundKey اولیه
    state = add_round_key(state, get_round_key(expanded_key, 10))
    
    # 9 دور کامل
    for round_num in range(9, 0, -1):
        state = shift_rows(state, inv=True)
        state = sub_bytes(state, inv=True)
        state = add_round_key(state, get_round_key(expanded_key, round_num))
        state = mix_columns(state, inv=True)
    
    # دور نهایی
    state = shift_rows(state, inv=True)
    state = sub_bytes(state, inv=True)
    state = add_round_key(state, get_round_key(expanded_key, 0))
    
    return state


def encrypt_aes(plaintext, key):
    # رمزنگاری AES
    key_matrix = key_to_matrix(key)
    expanded_key = key_expansion(key_matrix)
    
    text_matrix = text_to_matrix(plaintext)
    
    encrypted_blocks = []
    for state in text_matrix:
        encrypted_state = encrypt_aes_block(state, expanded_key)
        encrypted_blocks.append(encrypted_state)
    
    return matrix_to_text(encrypted_blocks, remove_padding=False)


def decrypt_aes(ciphertext, key):
    # رمزگشایی AES
    key_matrix = key_to_matrix(key)
    expanded_key = key_expansion(key_matrix)
    
    # تبدیل متن به ماتریس بدون اضافه کردن padding (column-major)
    bytes_list = [ord(c) for c in ciphertext]
    while len(bytes_list) % 16 != 0:
        bytes_list.append(0)
    
    text_matrix = []
    for i in range(0, len(bytes_list), 16):
        block = bytes_list[i:i+16]
        state = [[block[i + 4*j] for j in range(4)] for i in range(4)]
        text_matrix.append(state)
    
    decrypted_blocks = []
    for state in text_matrix:
        decrypted_state = decrypt_aes_block(state, expanded_key)
        decrypted_blocks.append(decrypted_state)
    
    return matrix_to_text(decrypted_blocks, remove_padding=True)


if __name__ == "__main__":
    plaintext = "HELLO WORLD"
    key = "SECRETKEY123456"
    
    print(f"Plaintext: {plaintext}")
    print(f"Key: {key}")
    
    ciphertext = encrypt_aes(plaintext, key)
    print(f"Ciphertext: {ciphertext}")
    
    decrypted = decrypt_aes(ciphertext, key)
    print(f"Decrypted: {decrypted}")

