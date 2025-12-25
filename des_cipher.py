
# جداول جایگشت اولیه (IP)
IP_TABLE = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

# جدول جایگشت معکوس (IP^-1)
IP_INV_TABLE = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

# جدول جایگشت انتخاب کلید (PC1)
PC1_TABLE = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

# جدول جایگشت انتخاب کلید (PC2)
PC2_TABLE = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

# جدول جایگشت گسترش (E)
E_TABLE = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

# جدول جایگشت (P)
P_TABLE = [
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25
]

# جداول S-Box
S_BOXES = [
    # S1
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    # S2
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    # S3
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    # S4
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    # S5
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    # S6
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    # S7
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    # S8
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]

# تعداد بیت‌های جابجایی در هر دور
SHIFT_SCHEDULE = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


def text_to_binary(text):
    #تبدیل متن به باینری
    binary = ''
    for char in text:
        binary += format(ord(char), '08b')
    return binary


def binary_to_text(binary):
    #تبدیل باینری به متن
    text = ''
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        if len(byte) == 8:
            text += chr(int(byte, 2))
    return text


def permute(bits, table):
    #انجام جایگشت بر روی بیت‌ها
    return ''.join([bits[table[i] - 1] for i in range(len(table))])


def left_shift(bits, n):
    #جابجایی چرخشی به چپ
    return bits[n:] + bits[:n]


def generate_keys(key_binary):
    #تولید 16 کلید دور
    # جایگشت اولیه کلید
    key_permuted = permute(key_binary, PC1_TABLE)
    
    # تقسیم به دو نیمه
    left = key_permuted[:28]
    right = key_permuted[28:]
    
    keys = []
    for i in range(16):
        # جابجایی چرخشی
        left = left_shift(left, SHIFT_SCHEDULE[i])
        right = left_shift(right, SHIFT_SCHEDULE[i])
        
        # ترکیب و جایگشت
        combined = left + right
        key_round = permute(combined, PC2_TABLE)
        keys.append(key_round)
    
    return keys


def f_function(right, key):
    #تابع F در DES
    # گسترش
    expanded = permute(right, E_TABLE)
    
    # XOR با کلید
    
    xored = ''.join(['1' if expanded[i] != key[i] else '0' for i in range(48)])
    
    # عبور از S-Boxes
    s_output = ''
    for i in range(8):
        block = xored[i*6:(i+1)*6]
        row = int(block[0] + block[5], 2)
        col = int(block[1:5], 2)
        s_value = S_BOXES[i][row][col]
        s_output += format(s_value, '04b')
    
    # جایگشت نهایی
    return permute(s_output, P_TABLE)


def des_encrypt_block(block, keys):
    #رمزنگاری یک بلاک 64 بیتی
    # جایگشت اولیه
    block = permute(block, IP_TABLE)
    
    # تقسیم به دو نیمه
    left = block[:32]
    right = block[32:]
    
    # 16 دور
    for i in range(16):
        temp = right
        right = ''.join(['1' if left[j] != f_function(right, keys[i])[j] else '0' 
                        for j in range(32)])
        left = temp
    
    # ترکیب نهایی
    combined = right + left
    
    # جایگشت معکوس
    return permute(combined, IP_INV_TABLE)


def des_decrypt_block(block, keys):
    #رمزگشایی یک بلاک 64 بیتی
    # استفاده از کلیدها به ترتیب معکوس
    return des_encrypt_block(block, keys[::-1])


def pad_text(text, block_size=8):
    # اضافه کردن padding به متن
    padding_len = block_size - (len(text) % block_size)
    return text + chr(padding_len) * padding_len


def unpad_text(text):
    # حذف padding از متن
    padding_len = ord(text[-1])
    return text[:-padding_len]


def encrypt_des(plaintext, key):
    # "رمزنگاری DES
    # تبدیل کلید به باینری (64 بیت)
    key_binary = text_to_binary(key[:8])
    if len(key_binary) < 64:
        key_binary = key_binary.ljust(64, '0')
    else:
        key_binary = key_binary[:64]
    
    # تولید کلیدهای دور
    keys = generate_keys(key_binary)
    
    # اضافه کردن padding
    padded_text = pad_text(plaintext)
    
    # تبدیل به باینری
    text_binary = text_to_binary(padded_text)
    
    # رمزنگاری هر بلاک 64 بیتی
    cipher_blocks = []
    for i in range(0, len(text_binary), 64):
        block = text_binary[i:i+64]
        if len(block) < 64:
            block = block.ljust(64, '0')
        encrypted_block = des_encrypt_block(block, keys)
        cipher_blocks.append(encrypted_block)
    
    # تبدیل به متن
    cipher_binary = ''.join(cipher_blocks)
    return binary_to_text(cipher_binary)


def decrypt_des(ciphertext, key):
    # "رمزگشایی DES
    # تبدیل کلید به باینری
    key_binary = text_to_binary(key[:8])
    if len(key_binary) < 64:
        key_binary = key_binary.ljust(64, '0')
    else:
        key_binary = key_binary[:64]
    
    # تولید کلیدهای دور
    keys = generate_keys(key_binary)
    
    # تبدیل به باینری
    cipher_binary = text_to_binary(ciphertext)
    
    # رمزگشایی هر بلاک
    plain_blocks = []
    for i in range(0, len(cipher_binary), 64):
        block = cipher_binary[i:i+64]
        if len(block) < 64:
            block = block.ljust(64, '0')
        decrypted_block = des_decrypt_block(block, keys)
        plain_blocks.append(decrypted_block)
    
    # تبدیل به متن
    plain_binary = ''.join(plain_blocks)
    plaintext = binary_to_text(plain_binary)
    
    # حذف padding
    return unpad_text(plaintext)


if __name__ == "__main__":
    plaintext = "HELLO WORLD"
    key = "SECRETKY"
    
    print(f"Plaintext: {plaintext}")
    print(f"Key: {key}")
    
    ciphertext = encrypt_des(plaintext, key)
    print(f"Ciphertext: {ciphertext}")
    
    decrypted = decrypt_des(ciphertext, key)
    print(f"Decrypted: {decrypted}")

