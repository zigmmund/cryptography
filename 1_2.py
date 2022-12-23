import numpy as np
import random
import copy
import re

def encrypt_polybius_square(text, dict_alphabets):
    hor_coordinates = ''
    ver_coordinates = ''
    for char in text:
        hor_coordinates += dict_alphabets[char][0]
        ver_coordinates += dict_alphabets[char][1]
    list_encrypted_text = re.findall('..', hor_coordinates+ver_coordinates)
    return ' '.join(list_encrypted_text)

def decrypt_polybius_square(encrypted_text, dict_alphabets):
    hor_coordinates = encrypted_text[:len(encrypted_text)//2].replace(' ', '')
    ver_coordinates = encrypted_text[len(encrypted_text)//2:].replace(' ', '')
    dict_swap = {value: key for key, value in dict_alphabets.items()}
    text = ''
    for i in range(0, len(hor_coordinates)):
        text += dict_swap[hor_coordinates[i]+ver_coordinates[i]]
    return text

dict_alphabets = {
    'а':'11', 'б':'12', 'в':'13', 'г':'14', 'д':'15', 'е':'16',
    'є':'21', 'ж':'22', 'з':'23', 'и':'24', 'і':'24', 'й':'25',
    'к':'31', 'л':'32', 'м':'33', 'н':'34', 'о':'35', 'п':'36',
    'р':'41', 'с':'42', 'т':'43', 'у':'44', 'ф':'45', 'х':'46',
    'ц':'51', 'ч':'52', 'ш':'53', 'ь':'54', 'ю':'55', 'я':'56'
}

dict_numbers = {v: k for k, v in dict_alphabets.items()}

text = input("Text message in Ukrainian:\n").lower()

print('Encrypt...')

try:
    encrypted_text =encrypt_polybius_square(text, dict_alphabets)
    cipher_text = ''.join([dict_numbers.get(n, n) for n in encrypted_text.split(' ')])

    print('Cipher text:', encrypted_text)
    print('Cipher text:', cipher_text)

    print('Decrypt...')
    text = decrypt_polybius_square(encrypted_text, dict_alphabets)
    print('Plain text:', text)
except KeyError:
    print('Something went wrong, please enter text in Ukrainian next time!')
