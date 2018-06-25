def caesar_cipher_encode():
    """Function to encrypt using the Caesar"""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key = int(input('Enter key: '))
    word = str(input('Enter the word, which you want to encrypt: '))
    result = ''
    for index_word in word:
        result += alphabet[(alphabet.index(index_word) + key) % len(alphabet)]
    return result


print(caesar_cipher_encode())


def caesar_cipher_decode():
    """Function to decrypt using the Caesar"""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key = int(input('Enter key: '))
    word = str(input('Enter the word, which you want to encrypt: '))
    result = ''
    for index_word in word:
        result += alphabet[(alphabet.index(index_word) - key) % len(alphabet)]
    return result


print(caesar_cipher_decode())
