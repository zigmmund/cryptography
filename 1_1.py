import numpy as np
import random
import copy
import re

def encode_decode(arr, key_hor, key_ver, encode):
    list_hor = list(key_hor)
    list_ver = list(key_ver)
    if encode:
        random.shuffle(list_hor)
        random.shuffle(list_ver)
    arr_local = np.transpose(copy.deepcopy(arr))
    temp = copy.deepcopy(arr_local)
    for i in range(0, len(list_hor)):
        arr_local[i+1] = temp[np.where(arr[0]==list_hor[i])[0]][0]
    array_copy = copy.deepcopy(arr_local)
    arr_local = np.transpose(arr_local)
    temp = copy.deepcopy(arr_local)
    for i in range(0, len(list_ver)):
        arr_local[i+1] = temp[np.where(array_copy[0]==list_ver[i])[0]][0]
    arr_local_for_return = copy.deepcopy(arr_local)
    if encode:
        arr_local = np.transpose(arr_local)
    arr_local = np.delete(arr_local, 0,0)
    arr_local = np.delete(arr_local, 0,1)
    text_crypto = ''
    for row in arr_local:
        text_row = ''.join(row)
        if text_row != ' ':
            text_crypto = text_crypto + text_row
    text_encrypted = text_crypto.strip()
    return arr_local_for_return, text_encrypted

key_hor = "crypto"
key_ver = "sifr"

text = input("Enter your message:\n")[:24]
arr = np.array(list(text))
arr_empty = np.empty(24-len(text), np.str)
arr = np.concatenate((arr, arr_empty), axis=0).reshape((len(key_ver),len(key_hor)))

arr = np.insert(arr, 0, list(key_hor), axis=0)
arr = np.insert(arr, 0, list(' '+key_ver), axis=1)

print(' ')
print('Encrypting...')
arr_encrypt, encrypted_text = encode_decode(arr, key_hor, key_ver, True)
print('Encrypted matrix:\n', arr_encrypt)
print('Cipher text:', encrypted_text)


print(' ')
print('Decrypting...')
arr_decrypt, text = encode_decode(arr, key_hor, key_ver, False)
print('Decrypted matrix:\n', arr_decrypt)
print('Plain text:', text)
