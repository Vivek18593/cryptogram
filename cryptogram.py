from numerizer import numerize
from termcolor import colored
import os
os.system('color')

#----ENCRYPTION----#
def encrypt(word):
    word.replace(' ','*')
    key = len(word)
    word_sum = ''
    res = ''
    for letter in word:
        en_let = ord(letter)*key
        en_let = hex(en_let).replace('0x','o')
        word_sum = str(word_sum) + str(en_let)
        res = word_sum[1:]
    return res

#----DECRYPTION----#
def decrypt(content,key):
    code_sp = content.split('o')
    nord = []
    for n in code_sp:
        nord.append(n)
    re_cd = ''
    for b in nord:
        re = int(b,16)//key
        re_wd = chr(re)
        re_st = str(re_cd) + str(re_wd)
        re_cd = re_st.replace('*',' ')
    return re_cd
#-----------------------------------------------------------#

#----RUN----#
#--KEY IS THE LENGTH OF THE DATA INCLUDING SPACE IN TEXT FORMAT--#
status = True
while status:
    data = input('Enter data to encrypt: ')
    pwd = len(data)
    en_content = encrypt(data)
    print('encrypted data: ',colored(en_content,'cyan'),'\n')
    ky = True
    while ky:
        key_text = input('Enter the key to decrypt: ')
        try:
            if key_text.isdigit():
                print(colored('Key Mismatched!! Decryption Failed!!','red'))
                ky = True
                status = False
            else:
                key = int(numerize(key_text))
                if key == pwd:  
                    de_content = decrypt(en_content,key)
                    print('data decrypted: ',colored(de_content,'yellow'),'\n')
                    print(colored('Decryption Completed!!','green'),'\n')
                    ky = False
                    status = False
                else:
                    print(colored('Key Mismatched!! Decryption Failed!!','red'))
                    ky = True
                    status = False
        except:
            print(colored('Key Mismatched!! Decryption Failed!!','red'))
            ky = True
            status = False    





