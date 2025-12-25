

from hill_cipher import encrypt_hill, decrypt_hill
from des_cipher import encrypt_des, decrypt_des
from aes_cipher import encrypt_aes, decrypt_aes

def test_hill_comprehensive():
    """Comprehensive tests for Hill Cipher"""
    print("=" * 70)
    print("COMPREHENSIVE HILL CIPHER TESTS")
    print("=" * 70)
    
    test_cases = [
        # (plaintext, key_matrix, description)
        ("HELLO", [[3, 3], [2, 5]], "Simple 5-letter word"),
        ("HELLO WORLD", [[3, 3], [2, 5]], "Text with space"),
        ("CRYPTOGRAPHY", [[3, 3], [2, 5]], "Long word"),
        ("A", [[3, 3], [2, 5]], "Single character"),
        ("ABCDEFGH", [[3, 3], [2, 5]], "Alphabet sequence"),
        ("THE QUICK BROWN FOX", [[3, 3], [2, 5]], "Multiple words"),
        ("HELLO", [[7, 8], [11, 11]], "Different key matrix"),
        ("TESTING", [[5, 1], [3, 2]], "Another key matrix"),
    ]
    
    # Test 3x3 matrix
    test_cases_3x3 = [
        ("HELLO WORLD", [[17, 17, 5], [21, 18, 21], [2, 2, 19]], "3x3 key matrix"),
        ("CRYPTOGRAPHY", [[17, 17, 5], [21, 18, 21], [2, 2, 19]], "3x3 key with long text"),
    ]
    
    passed = 0
    failed = 0
    
    # Test 2x2 matrices
    for plaintext, key, description in test_cases:
        try:
            print(f"\nTest: {description}")
            print(f"  Plaintext: '{plaintext}'")
            print(f"  Key: {key}")
            
            ciphertext = encrypt_hill(plaintext, key)
            print(f"  Ciphertext: '{ciphertext}'")
            
            decrypted = decrypt_hill(ciphertext, key)
            print(f"  Decrypted: '{decrypted}'")
            
            # Compare without spaces and case
            plain_clean = plaintext.replace(' ', '').upper()
            decrypted_clean = decrypted.replace(' ', '').upper()
            
            # The decrypt function should automatically remove padding
            # So we can compare directly
            if plain_clean == decrypted_clean:
                print(f"  ✓ PASSED")
                passed += 1
            else:
                print(f"  ✗ FAILED")
                print(f"    Expected: '{plain_clean}' (length: {len(plain_clean)})")
                print(f"    Got: '{decrypted_clean}' (length: {len(decrypted_clean)})")
                print(f"    Full decrypted: '{decrypted}' (length: {len(decrypted)})")
                # Show character-by-character comparison
                if len(plain_clean) == len(decrypted_clean):
                    diff = [i for i, (p, d) in enumerate(zip(plain_clean, decrypted_clean)) if p != d]
                    if diff:
                        print(f"    Differences at positions: {diff}")
                failed += 1
        except Exception as e:
            print(f"  ✗ ERROR: {e}")
            failed += 1
    
    # Test 3x3 matrices
    for plaintext, key, description in test_cases_3x3:
        try:
            print(f"\nTest: {description}")
            print(f"  Plaintext: '{plaintext}'")
            print(f"  Key: {key}")
            
            ciphertext = encrypt_hill(plaintext, key)
            print(f"  Ciphertext: '{ciphertext}'")
            
            decrypted = decrypt_hill(ciphertext, key)
            print(f"  Decrypted: '{decrypted}'")
            
            plain_clean = plaintext.replace(' ', '').upper()
            decrypted_clean = decrypted.replace(' ', '').upper()
            
            # The decrypt function should automatically remove padding
            if plain_clean == decrypted_clean:
                print(f"  ✓ PASSED")
                passed += 1
            else:
                print(f"  ✗ FAILED")
                print(f"    Expected: '{plain_clean}' (length: {len(plain_clean)})")
                print(f"    Got: '{decrypted_clean}' (length: {len(decrypted_clean)})")
                print(f"    Full decrypted: '{decrypted}'")
                failed += 1
        except Exception as e:
            print(f"  ✗ ERROR: {e}")
            failed += 1
    
    print(f"\n{'='*70}")
    print(f"Hill Cipher Results: {passed} passed, {failed} failed")
    print(f"{'='*70}\n")
    
    return passed, failed


def test_des_comprehensive():
    """Comprehensive tests for DES Cipher"""
    print("=" * 70)
    print("COMPREHENSIVE DES CIPHER TESTS")
    print("=" * 70)
    
    test_cases = [
        # (plaintext, key, description)
        ("HELLO", "SECRETKY", "Simple 5-letter word"),
        ("HELLO WORLD", "SECRETKY", "Text with space"),
        ("CRYPTOGRAPHY", "SECRETKY", "Long word"),
        ("A", "SECRETKY", "Single character"),
        ("ABCDEFGH", "SECRETKY", "Alphabet sequence"),
        ("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG", "SECRETKY", "Long sentence"),
        ("HELLO", "KEY12345", "Different key"),
        ("TESTING", "MYKEY123", "Another key"),
        ("12345678", "SECRETKY", "Numbers as text"),
        ("!@#$%^&*", "SECRETKY", "Special characters"),
        ("HELLO", "A", "Short key"),
        ("HELLO", "VERYLONGKEY123456789", "Long key"),
    ]
    
    passed = 0
    failed = 0
    
    for plaintext, key, description in test_cases:
        try:
            print(f"\nTest: {description}")
            print(f"  Plaintext: '{plaintext}'")
            print(f"  Key: '{key}'")
            
            ciphertext = encrypt_des(plaintext, key)
            print(f"  Ciphertext length: {len(ciphertext)} characters")
            print(f"  Ciphertext (first 50): '{ciphertext[:50]}...'")
            
            decrypted = decrypt_des(ciphertext, key)
            print(f"  Decrypted: '{decrypted}'")
            
            if plaintext == decrypted:
                print(f"  ✓ PASSED")
                passed += 1
            else:
                print(f"  ✗ FAILED")
                print(f"    Expected: '{plaintext}'")
                print(f"    Got: '{decrypted}'")
                print(f"    Expected length: {len(plaintext)}, Got length: {len(decrypted)}")
                failed += 1
        except Exception as e:
            print(f"  ✗ ERROR: {e}")
            failed += 1
    
    print(f"\n{'='*70}")
    print(f"DES Cipher Results: {passed} passed, {failed} failed")
    print(f"{'='*70}\n")
    
    return passed, failed


def test_aes_comprehensive():
    """Comprehensive tests for AES Cipher"""
    print("=" * 70)
    print("COMPREHENSIVE AES CIPHER TESTS")
    print("=" * 70)
    
    test_cases = [
        # (plaintext, key, description)
        ("HELLO", "SECRETKEY123456", "Simple 5-letter word"),
        ("HELLO WORLD", "SECRETKEY123456", "Text with space"),
        ("CRYPTOGRAPHY", "SECRETKEY123456", "Long word"),
        ("A", "SECRETKEY123456", "Single character"),
        ("ABCDEFGH", "SECRETKEY123456", "Alphabet sequence"),
        ("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG", "SECRETKEY123456", "Long sentence"),
        ("HELLO", "MYKEY1234567890", "Different key"),
        ("TESTING", "ANOTHERKEY1234", "Another key"),
        ("12345678", "SECRETKEY123456", "Numbers as text"),
        ("!@#$%^&*", "SECRETKEY123456", "Special characters"),
        ("HELLO", "A", "Short key"),
        ("HELLO", "VERYLONGKEY12345678901234567890", "Long key"),
        ("", "SECRETKEY123456", "Empty string"),
    ]
    
    passed = 0
    failed = 0
    
    for plaintext, key, description in test_cases:
        try:
            print(f"\nTest: {description}")
            print(f"  Plaintext: '{plaintext}'")
            print(f"  Key: '{key}'")
            
            ciphertext = encrypt_aes(plaintext, key)
            print(f"  Ciphertext length: {len(ciphertext)} characters")
            print(f"  Ciphertext (first 50): '{ciphertext[:50]}...'")
            
            decrypted = decrypt_aes(ciphertext, key)
            print(f"  Decrypted: '{decrypted}'")
            
            if plaintext == decrypted:
                print(f"  ✓ PASSED")
                passed += 1
            else:
                print(f"  ✗ FAILED")
                print(f"    Expected: '{plaintext}'")
                print(f"    Got: '{decrypted}'")
                print(f"    Expected length: {len(plaintext)}, Got length: {len(decrypted)}")
                # Show character differences
                if len(plaintext) == len(decrypted):
                    diff_positions = [i for i, (p, d) in enumerate(zip(plaintext, decrypted)) if p != d]
                    if diff_positions:
                        print(f"    Differences at positions: {diff_positions[:10]}")
                failed += 1
        except Exception as e:
            print(f"  ✗ ERROR: {e}")
            import traceback
            traceback.print_exc()
            failed += 1
    
    print(f"\n{'='*70}")
    print(f"AES Cipher Results: {passed} passed, {failed} failed")
    print(f"{'='*70}\n")
    
    return passed, failed


def test_all_characters():
    """Test with all ASCII printable characters"""
    print("=" * 70)
    print("TESTING WITH ALL PRINTABLE ASCII CHARACTERS")
    print("=" * 70)
    
    # All printable ASCII characters
    all_chars = ''.join([chr(i) for i in range(32, 127)])
    
    print(f"\nTesting with string containing all printable ASCII characters")
    print(f"Length: {len(all_chars)} characters")
    print(f"First 50 chars: '{all_chars[:50]}...'")
    
    results = {}
    
    # Test DES
    try:
        print(f"\n--- DES Test ---")
        key = "SECRETKY"
        ciphertext = encrypt_des(all_chars, key)
        decrypted = decrypt_des(ciphertext, key)
        if all_chars == decrypted:
            print("✓ DES: PASSED")
            results['DES'] = True
        else:
            print("✗ DES: FAILED")
            results['DES'] = False
    except Exception as e:
        print(f"✗ DES: ERROR - {e}")
        results['DES'] = False
    
    # Test AES
    try:
        print(f"\n--- AES Test ---")
        key = "SECRETKEY123456"
        ciphertext = encrypt_aes(all_chars, key)
        decrypted = decrypt_aes(ciphertext, key)
        if all_chars == decrypted:
            print("✓ AES: PASSED")
            results['AES'] = True
        else:
            print("✗ AES: FAILED")
            results['AES'] = False
    except Exception as e:
        print(f"✗ AES: ERROR - {e}")
        results['AES'] = False
    
    # Test Hill (only letters)
    try:
        print(f"\n--- Hill Test (letters only) ---")
        letters_only = ''.join([c for c in all_chars if c.isalpha()])
        key = [[3, 3], [2, 5]]
        ciphertext = encrypt_hill(letters_only, key)
        decrypted = decrypt_hill(ciphertext, key)
        # The decrypt function should automatically remove padding
        if letters_only.upper() == decrypted:
            print("✓ Hill: PASSED")
            results['Hill'] = True
        else:
            print("✗ Hill: FAILED")
            results['Hill'] = False
    except Exception as e:
        print(f"✗ Hill: ERROR - {e}")
        results['Hill'] = False
    
    print(f"\n{'='*70}\n")
    return results


def test_edge_cases():
    """Test edge cases for all ciphers"""
    print("=" * 70)
    print("EDGE CASE TESTS")
    print("=" * 70)
    
    edge_cases = [
        ("", "Empty string"),
        ("A" * 1, "Single character repeated"),
        ("A" * 16, "Exactly one block (AES/DES)"),
        ("A" * 32, "Exactly two blocks"),
        ("A" * 100, "Multiple blocks"),
        (" " * 10, "Only spaces"),
        ("\n" * 10, "Only newlines"),
        ("A" + " " * 10 + "B", "Text with many spaces"),
    ]
    
    print("\n--- DES Edge Cases ---")
    for text, description in edge_cases:
        try:
            key = "SECRETKY"
            ciphertext = encrypt_des(text, key)
            decrypted = decrypt_des(ciphertext, key)
            if text == decrypted:
                print(f"✓ {description}: PASSED")
            else:
                print(f"✗ {description}: FAILED")
        except Exception as e:
            print(f"✗ {description}: ERROR - {e}")
    
    print("\n--- AES Edge Cases ---")
    for text, description in edge_cases:
        try:
            key = "SECRETKEY123456"
            ciphertext = encrypt_aes(text, key)
            decrypted = decrypt_aes(ciphertext, key)
            if text == decrypted:
                print(f"✓ {description}: PASSED")
            else:
                print(f"✗ {description}: FAILED")
        except Exception as e:
            print(f"✗ {description}: ERROR - {e}")
    
    print("\n--- Hill Edge Cases (letters only) ---")
    for text, description in edge_cases:
        try:
            # Filter to letters only for Hill
            letters = ''.join([c for c in text if c.isalpha()])
            if not letters:
                letters = "A"  # At least one letter needed
            key = [[3, 3], [2, 5]]
            ciphertext = encrypt_hill(letters, key)
            decrypted = decrypt_hill(ciphertext, key)
            # The decrypt function should automatically remove padding
            if letters.upper() == decrypted:
                print(f"✓ {description}: PASSED")
            else:
                print(f"✗ {description}: FAILED")
        except Exception as e:
            print(f"✗ {description}: ERROR - {e}")
    
    print(f"\n{'='*70}\n")


def main():
    """Run all comprehensive tests"""
    print("\n" + "=" * 70)
    print("COMPREHENSIVE CIPHER TEST SUITE")
    print("=" * 70 + "\n")
    
    total_passed = 0
    total_failed = 0
    
    # Run comprehensive tests for each cipher
    hill_passed, hill_failed = test_hill_comprehensive()
    total_passed += hill_passed
    total_failed += hill_failed
    
    des_passed, des_failed = test_des_comprehensive()
    total_passed += des_passed
    total_failed += des_failed
    
    aes_passed, aes_failed = test_aes_comprehensive()
    total_passed += aes_passed
    total_failed += aes_failed
    
    # Test with all characters
    all_chars_results = test_all_characters()
    
    # Test edge cases
    test_edge_cases()
    
    # Final summary
    print("=" * 70)
    print("FINAL SUMMARY")
    print("=" * 70)
    print(f"Total tests passed: {total_passed}")
    print(f"Total tests failed: {total_failed}")
    print(f"Success rate: {(total_passed / (total_passed + total_failed) * 100):.2f}%")
    print("\nAll Characters Test Results:")
    for cipher, result in all_chars_results.items():
        status = "PASSED" if result else "FAILED"
        print(f"  {cipher}: {status}")
    print("=" * 70)


if __name__ == "__main__":
    main()

