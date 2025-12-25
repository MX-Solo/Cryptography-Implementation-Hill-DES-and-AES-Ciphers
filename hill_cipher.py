
def text_to_matrix(text, n):
    
    #تبدیل متن به ماتریس
    
    # حذف فاصله‌ها و تبدیل به حروف بزرگ
    text = text.replace(' ', '').upper()
    
    # اضافه کردن حروف اضافی برای کامل کردن ماتریس
    while len(text) % n != 0:
        text += 'X'
    
    # تبدیل حروف به اعداد (A=0, B=1, ..., Z=25)
    numbers = [ord(char) - ord('A') for char in text]
    
    # تبدیل به ماتریس
    matrix = []
    for i in range(0, len(numbers), n):
        matrix.append(numbers[i:i+n])
    
    return matrix


def matrix_to_text(matrix):
    
    #تبدیل ماتریس به متن

    text = ''
    for row in matrix:
        for num in row:
            text += chr(num + ord('A'))
    return text


def matrix_multiply(A, B):
    
   # ضرب ماتریس A در B
    
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            sum_val = 0
            for k in range(len(B)):
                sum_val += A[i][k] * B[k][j]
            row.append(sum_val % 26)  # مدول 26 برای الفبای انگلیسی
        result.append(row)
    return result


def matrix_inverse_mod26(matrix):
    
   # محاسبه معکوس ماتریس در مدول 26
    
    n = len(matrix)
    
    # محاسبه دترمینان
    det = determinant_mod26(matrix)
    
    # محاسبه معکوس دترمینان در مدول 26
    det_inv = mod_inverse(det, 26)
    if det_inv is None:
        raise ValueError("ماتریس معکوس‌پذیر نیست (دترمینان و 26 نسبت به هم اول نیستند)")
    
    # محاسبه ماتریس الحاقی
    adj = adjoint_matrix(matrix)
    
    # ضرب در معکوس دترمینان
    inverse = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append((adj[i][j] * det_inv) % 26)
        inverse.append(row)
    
    return inverse


def determinant_mod26(matrix):
    
   # محاسبه دترمینان ماتریس در مدول 26
    
    n = len(matrix)
    if n == 1:
        return matrix[0][0] % 26
    elif n == 2:
        det = (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % 26
        return det if det >= 0 else det + 26
    else:
        det = 0
        for j in range(n):
            minor = [[matrix[i][k] for k in range(n) if k != j] 
                     for i in range(1, n)]
            cofactor = ((-1) ** j) * matrix[0][j] * determinant_mod26(minor)
            det += cofactor
        det = det % 26
        return det if det >= 0 else det + 26


def adjoint_matrix(matrix):
    
  #  محاسبه ماتریس الحاقی
    
    n = len(matrix)
    adj = []
    for i in range(n):
        row = []
        for j in range(n):
            # محاسبه کوفکتور
            minor = [[matrix[x][y] for y in range(n) if y != j] 
                     for x in range(n) if x != i]
            cofactor = ((-1) ** (i + j)) * determinant_mod26(minor)
            cofactor = cofactor % 26
            row.append(cofactor if cofactor >= 0 else cofactor + 26)
        adj.append(row)
    
    # ترانهاده ماتریس الحاقی
    adj_transpose = [[adj[j][i] for j in range(n)] for i in range(n)]
    return adj_transpose


def mod_inverse(a, m):
    
   # محاسبه معکوس a در مدول m با استفاده از الگوریتم اقلیدس توسعه‌یافته
    
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y
    
    gcd, x, _ = extended_gcd(a % m, m)
    if gcd != 1:
        return None
    return (x % m + m) % m


def encrypt_hill(plaintext, key_matrix):
    
   # رمزنگاری Hill
    
    n = len(key_matrix)
    # ذخیره طول متن اصلی (بدون فاصله)
    original_length = len(plaintext.replace(' ', ''))
    
    text_matrix = text_to_matrix(plaintext, n)
    
    cipher_matrix = []
    for row in text_matrix:
        # تبدیل هر سطر به ماتریس ستونی
        col_matrix = [[row[i]] for i in range(n)]
        # ضرب در ماتریس کلید
        encrypted_col = matrix_multiply(key_matrix, col_matrix)
        # تبدیل به لیست
        cipher_matrix.append([encrypted_col[i][0] for i in range(n)])
    
    ciphertext = matrix_to_text(cipher_matrix)
    
    # ذخیره طول اصلی در دیکشنری global برای استفاده در decrypt
    global _hill_length_map
    _hill_length_map[ciphertext] = original_length
    
    return ciphertext


# دیکشنری global برای نگاشت ciphertext به طول متن اصلی
_hill_length_map = {}

def decrypt_hill(ciphertext, key_matrix, original_length=None):
    
   # رمزگشایی Hill
    
    global _hill_length_map
    
    # محاسبه معکوس ماتریس کلید
    key_inverse = matrix_inverse_mod26(key_matrix)
    
    n = len(key_inverse)
    text_matrix = text_to_matrix(ciphertext, n)
    
    plain_matrix = []
    for row in text_matrix:
        # تبدیل هر سطر به ماتریس ستونی
        col_matrix = [[row[i]] for i in range(n)]
        # ضرب در معکوس ماتریس کلید
        decrypted_col = matrix_multiply(key_inverse, col_matrix)
        # تبدیل به لیست
        plain_matrix.append([decrypted_col[i][0] for i in range(n)])
    
    decrypted_text = matrix_to_text(plain_matrix)
    
    # اگر original_length داده شده، فقط همان تعداد کاراکتر را برگردان
    if original_length is not None:
        if len(decrypted_text) >= original_length:
            return decrypted_text[:original_length]
    
    # سعی کن طول اصلی را از دیکشنری بگیر
    if ciphertext in _hill_length_map:
        original_len = _hill_length_map[ciphertext]
        if len(decrypted_text) >= original_len:
            return decrypted_text[:original_len]
    
    # در غیر این صورت، متن کامل را برگردان (با padding)
    return decrypted_text


# مثال استفاده
if __name__ == "__main__":
    # ماتریس کلید 2x2
    key = [[3, 3], [2, 5]]
    
    plaintext = "HELLO WORLD"
    print(f"Plaintext: {plaintext}")
    
    ciphertext = encrypt_hill(plaintext, key)
    print(f"Ciphertext: {ciphertext}")
    
    decrypted = decrypt_hill(ciphertext, key)
    print(f"Decrypted: {decrypted}")

