# Classical Cryptography Algorithms Implementation

## 📋 Table of Contents
- [Introduction](#introduction)
- [Implemented Algorithms](#implemented-algorithms)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Examples](#examples)
- [Implementation Features](#implementation-features)
- [Limitations](#limitations)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction

This project implements three classical cryptography algorithms as part of a Numerical Linear Algebra course project. The project includes implementations of Hill Cipher, DES (Data Encryption Standard), and AES (Advanced Encryption Standard), each implemented using linear algebra and cryptography concepts.

---

## Implemented Algorithms

### 1. Hill Cipher
Hill Cipher is a polygraphic substitution cipher that uses linear algebra and matrix multiplication. This algorithm:
- Uses a key matrix for encryption
- Divides text into blocks of n characters
- Multiplies each block by the key matrix
- Uses matrix inverse calculation modulo 26 for decryption

### 2. DES (Data Encryption Standard)
DES is a symmetric block cipher algorithm that:
- Uses a 64-bit key
- Divides text into 64-bit blocks
- Includes 16 rounds of encryption
- Uses permutation tables and S-Boxes

### 3. AES (Advanced Encryption Standard)
AES is an advanced block cipher algorithm that:
- Uses a 128-bit key (AES-128)
- Divides text into 128-bit blocks (16 bytes)
- Includes 10 rounds of encryption
- Uses SubBytes, ShiftRows, MixColumns, and AddRoundKey transformations
- Uses the finite field GF(2^8) for mathematical operations

---

## Installation

### Prerequisites
- Python 3.6 or higher

### Setup
```bash
# Clone the repository
git clone https://github.com/yourusername/cryptography-ciphers.git

# Navigate to project directory
cd cryptography-ciphers
```

No additional libraries are required! This project uses only Python standard library.

---

## Usage

### Hill Cipher

```python
from hill_cipher import encrypt_hill, decrypt_hill

# Define key matrix (2x2)
key_matrix = [[3, 3], [2, 5]]

# Plaintext
plaintext = "HELLO WORLD"

# Encryption
ciphertext = encrypt_hill(plaintext, key_matrix)
print(f"Ciphertext: {ciphertext}")

# Decryption
decrypted = decrypt_hill(ciphertext, key_matrix)
print(f"Decrypted: {decrypted}")
```

### DES Cipher

```python
from des_cipher import encrypt_des, decrypt_des

# Key (8 characters)
key = "SECRETKY"

# Plaintext
plaintext = "HELLO WORLD"

# Encryption
ciphertext = encrypt_des(plaintext, key)
print(f"Ciphertext: {ciphertext}")

# Decryption
decrypted = decrypt_des(ciphertext, key)
print(f"Decrypted: {decrypted}")
```

### AES Cipher

```python
from aes_cipher import encrypt_aes, decrypt_aes

# Key (16 characters)
key = "SECRETKEY123456"

# Plaintext
plaintext = "HELLO WORLD"

# Encryption
ciphertext = encrypt_aes(plaintext, key)
print(f"Ciphertext: {ciphertext}")

# Decryption
decrypted = decrypt_aes(ciphertext, key)
print(f"Decrypted: {decrypted}")
```

---

## Project Structure

```
project/
│
├── hill_cipher.py      # Hill Cipher implementation
├── des_cipher.py       # DES Cipher implementation
├── aes_cipher.py       # AES Cipher implementation
├── test.py            # Comprehensive test file for all algorithms
└── README.md          # This file
```

---

## Testing

To run comprehensive tests:

```bash
python test.py
```

This test file includes:
- Comprehensive tests for all three algorithms
- Tests with various characters
- Edge case testing
- Complete results report

### Running Individual Tests

```bash
# Test Hill Cipher
python hill_cipher.py

# Test DES Cipher
python des_cipher.py

# Test AES Cipher
python aes_cipher.py
```

---

## Examples

### Example 1: Simple Encryption with Hill Cipher

```python
from hill_cipher import encrypt_hill, decrypt_hill

key = [[3, 3], [2, 5]]
plaintext = "CRYPTOGRAPHY"

ciphertext = encrypt_hill(plaintext, key)
print(f"Encrypted: {ciphertext}")

decrypted = decrypt_hill(ciphertext, key)
print(f"Decrypted: {decrypted}")
```

### Example 2: Encryption with DES

```python
from des_cipher import encrypt_des, decrypt_des

key = "MYKEY123"
message = "Secret message"

encrypted = encrypt_des(message, key)
decrypted = decrypt_des(encrypted, key)

print(f"Original: {message}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
```

### Example 3: Encryption with AES

```python
from aes_cipher import encrypt_aes, decrypt_aes

key = "SECRETKEY123456"
data = "Important data"

encrypted = encrypt_aes(data, key)
decrypted = decrypt_aes(encrypted, key)

print(f"Original: {data}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
```

---

## Implementation Features

### Hill Cipher
- ✅ Support for 2x2 and 3x3 key matrices
- ✅ Matrix inverse calculation modulo 26
- ✅ Automatic padding management
- ✅ Automatic padding removal during decryption

### DES
- ✅ Complete 16-round DES implementation
- ✅ Round key generation
- ✅ Standard permutation tables
- ✅ 8 S-Boxes implementation
- ✅ PKCS7 padding management

### AES
- ✅ AES-128 implementation (10 rounds)
- ✅ Key expansion
- ✅ SubBytes, ShiftRows, MixColumns transformations
- ✅ Operations in GF(2^8) field
- ✅ PKCS7 padding management

---

## Limitations

- **Hill Cipher**: Only supports English letters (A-Z)
- **DES**: Key must be at least 8 characters (64 bits)
- **AES**: Key must be at least 16 characters (128 bits)
- These implementations are for educational purposes and should not be used for encrypting sensitive data in production environments

---

## Contributing

Contributions, suggestions, and bug reports are welcome! Please:

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## License

This project is created for educational purposes. Free to use.

---

## Project Information

- **Course**: Numerical Linear Algebra
- **University**: Amirkabir University of Technology
- **Programming Language**: Python 3

---

## References

- [Hill Cipher - Wikipedia](https://en.wikipedia.org/wiki/Hill_cipher)
- [DES - Wikipedia](https://en.wikipedia.org/wiki/Data_Encryption_Standard)
- [AES - Wikipedia](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)
- [NIST FIPS 197 - AES Standard](https://csrc.nist.gov/publications/fips/fips197/fips-197.pdf)

---

## Contact

For questions and suggestions, please open an Issue on GitHub.

---

**Note**: These implementations are designed for educational purposes and learning cryptography and linear algebra concepts. For production use, please use standard and tested cryptography libraries.
