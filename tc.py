from math import ceil

def menuu():
    print("""
Welcome to ColumnarTranspositionCipher EncryptorDecryptorrBreaker

What do you want to do?
1.Encrypt with CTC
2.Decrypt with CTC
3.Cracking CTC

4.Encrypt with Transposition Chiper
5.Decrypt with Transposition Chiper
6.Cracking Transposition Chiper

7.Encrypt with Rail Fence Chiper
8.Decrypt with Rail Fence Chiper
9.Cracking Rail Fence Chiper

10.Encrypt with Route Chiper

0.Exit

Note : In tranposition chiper a way to encrypt, decrypt even crack it is the same way but to make it
       user friendly, I will also attach the decryptor and the cracker in the menu
               """)
    menu = input()
    if menu == "1":
        encrypt_ctc()
        go_to_menu()
    elif menu == "2":
        decrypt_ctc()
        go_to_menu()
    elif menu == "3":
        cracking_ctc()
        go_to_menu()
    elif menu == "4":
        encrypt_transposition("en")
        go_to_menu()
    elif menu == "5":
        encrypt_transposition("de")
        go_to_menu()
    elif menu == "6":
        encrypt_transposition("cr")
        go_to_menu()
    elif menu == "7":
        railfence()
        go_to_menu()
    elif menu == "8":
        railfence_decrypt()
        go_to_menu()
    elif menu == "9":
        railfence_crack()
        go_to_menu()
    elif menu == "10":
        rt_chiper_encrypt()
        go_to_menu()
    elif menu == "0":
        exit(0)
    else:
        print("Please enter a valid input from the menu \n")
        menuu()

def go_to_menu():
    cc_text = input("Do you want to go to the main menu 1)Yes 2)No ?  ")
    cc_text.lower()
    if cc_text == "1" or cc_text == "yes":
        menuu()
    elif cc_text == "2" or cc_text == "no":
        print("Thanks for using this program! See ya later")
    else:
        print("Please input a valid number")

def encrypt_ctc():
    to_encrypt = []
    encrypted = []
    text = input("What text do you want to encrypt? ")
    text.strip()
    key = int(input("What key do you want to use? "))
    to_encrypt = list(text)
    for column in range(0,8):
        for index in range(column,len(text),key):
            encrypted.append(to_encrypt[index])
    encrypted = "".join(encrypted)
    print(f"This is the text after encrypted by Columnar Transposition Cipher : {encrypted}")

def decrypt_ctc():
    to_decrypt = []
    decrypted = []
    text = input("What text do you want to decrypt? ")
    key = int(input("What is the key that this encrypted text used? "))
    to_decrypt = list(text)
    for i in range(len(to_decrypt) % key, key):
        to_decrypt.insert((ceil(len(to_decrypt) / key) - 1) + ceil(len(to_decrypt) / key) * i, None)
    for row in range(0, ceil(len(to_decrypt) / key)):
        for index in range(row, len(to_decrypt), ceil(len(to_decrypt) / key)):
            decrypted.append(to_decrypt[index])
    while None in decrypted:
        decrypted.remove(None)
    decrypted = "".join(decrypted)
    print(f"This is the text after decrypted by Columnar Transposition Cipher : {decrypted}")

def cracking_ctc():
    to_crack = []
    crack = []
    text = input("What encrypted text do you want to crack by this method? ")
    to_crack = list(text)
    for key in range(1, len(text)):
        to_crack = []
        crack = []
        to_crack = list(text)
        for i in range(len(to_crack) % key, key):
            to_crack.insert((ceil(len(to_crack) / key) - 1) + ceil(len(to_crack) / key) * i, None)
        for row in range(0, ceil(len(to_crack) / key)):
            for index in range(row, len(to_crack), ceil(len(to_crack) / key)):
                crack.append(to_crack[index])
        while None in crack:
            crack.remove(None)
        crack = "".join(crack)
        print(f"Trial {key} : {crack}")
    print("\nBrute force finished!")

def encrypt_transposition(mode):
    to_crack = []
    cracked = []
    if mode == "en":
        text = input("What text do you want to encrypt with this transposition cipher method? ")
    elif mode == "de":
        text = input("What text do you want to decrypt with this transposition cipher method? ")
    elif mode == "cr":
        text = input("What text do you want to crack with this transposition cipher method? ")
    to_crack = list(text)
    while len(to_crack) != 0:
        try:
            space = to_crack.index(" ")
        except:
            space = len(to_crack)
        for i in range (space -1, -1, -1):
            cracked.insert(len(cracked), to_crack[i])
            to_crack.pop(i)
        try:
            cracked.insert(len(cracked), to_crack[0])
            to_crack.pop(0)
        except:
            pass
    cracked = "".join(cracked)
    if mode == "en":
        print(f"This is the text after encrypted by Transposition Cipher : {cracked}")
    elif mode == "de":
        print(f"This is the text after decrypted by Transposition Cipher : {cracked}")
    elif mode == "cr":
        print(f"This is the text after cracked by Transposition Cipher : {cracked}")

def railfence():
    encrypted = []
    text = input("What text do you want to encrypt with this Rail fence cipher method? ")
    key = int(input("What is the key that you want this plaintext uses? "))
    key_list = []
    to_encrypt = list(text)
    count = 0
    for x in range((key * 2) - 2, 0, -2):
        key_list.append(x)
    key_list.append((key * 2) - 2)
    for start in range(0, key):
        temp_start = start
        while start < len(text):
            encrypted.append(to_encrypt[start])
            start += key_list[temp_start]
            key_list.reverse()
            count += 1

        if count % 2 != 0:
            key_list.reverse()
            count += 1
            
    encrypted = "".join(encrypted)
    print(f"This is the text after cracked by Rail fence Cipher : {encrypted}")

def railfence_crack():
    text = input("What text do you want to crack with this Rail fence cipher method? ")
    for key in range(2,len(text) // 2):
        decrypted = []
        to_decrypt = list(text)
        index = 0
        key_list = []
        count = 0
        for x in range((key * 2) - 2, 0, -2):
            key_list.append(x)
        key_list.append((key * 2) - 2)
        for i in text:
            decrypted.append(None)
        for start in range(0, key):
            temp_start = start
            while start < len(text):
                decrypted.insert(start,to_decrypt[index])
                decrypted.pop(start + 1)
                start += key_list[temp_start]
                key_list.reverse()
                count += 1
                index += 1

            if count % 2 != 0:
                key_list.reverse()
                count += 1
        key -= 1
        decrypted = "".join(decrypted)
        print(f"Trial {key} : {decrypted}")
    print("Brute force finished!\n")

def choose_route():
    route = int(input("""
Which route do you want to choose?
1.Up
2.Down
3.Left
4.Right
5.Spiral down right
6.Spiral right down
7.Spiral up right
8.Spiral right up
9.Spiral down left
10.Spiral left down
11.Spiral up left
12.Spiral left up
\n"""))
    if route not in range(1,13):
        print("Please enter a valid input from menu")
        choose_route()
    else:
        return route

def rt_chiper_encrypt():
    decrypted = []
    text = input("What text do you want to encrypt with this route chiper? ")
    key = int(input("How many row or column do you want to have? "))
    key_type = input("""
Which type of formatting do you want?
1.Row
2.Column
\n""")
    key_type.lower()
    key_type.strip()
    route = choose_route()
    text = list(text)
    index = 0
    if route == 1:
        if key_type == "1":
            while len(text) % key != 0:
                text.append("X")
            for n in range(0,len(text), key):
                for i in range(n + key - 1,n - 1, -1):
                    decrypted.insert(index, text[i])
                    index += 1
            decrypted = "".join(decrypted)
            return print(f"This is the text after encrypted with route chiper : {decrypted}")
        elif key_type == "2": #Something gets wrong from here
            while len(text) % key != 0:
                text.append("X")
            for n in range(0, key):
                for i in range(((len(text) // key) - 1) * key + n, n, key):
                    print(decrypted)
                    decrypted.append(text[i])
            decrypted = "".join(decrypted)
            return print(f"This is the text after encrypted with route chiper : {decrypted}")
    elif route == 2:
        pass
    elif route == 3:
        pass
    elif route == 4:
        pass
    elif route == 5:
        pass
    elif route == 6:
        pass
    elif route == 7:
        pass
    elif route == 8:
        pass
    elif route == 9:
        pass
    elif route == 10:
        pass
    elif route == 11:
        pass
    elif route == 12:
        pass

menuu()
