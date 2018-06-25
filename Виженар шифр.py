def vigenere_cipher_encode():

    """Function to encrypt using the Vigenere"""

    key = input('Enter key: ')

    word = str(input('Enter the word, which you want to encrypt: '))

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    new_word_range = []

result = ''

    for index_word in word:

        if index_word not in alphabet:

             new_word_range.append(index_word)

        else:

            new_word_range.append(alphabet[(alphabet.index(index_word) + len(key)) % len(alphabet)])

    for index_word in range(len(new_word_range)):

        result += new_word_range[index_word]

    return result





print(vigenere_cipher_encode())

