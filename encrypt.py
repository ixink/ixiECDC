def Encryptmessage(str, key1):
    encstring = ""
    for i in str:
        if 65 <= ord(i) <= 90:
            tempstr = (ord(i) + key1)
            if tempstr > 90:
                tempstr = tempstr % 90 + 64
            encstring = encstring + chr(tempstr)
        elif 97 <= ord(i) <= 122:
            tempstr = (ord(i) + key1)
            if tempstr > 122:
                tempstr = tempstr % 122 + 96
            encstring = encstring + chr(tempstr)
        else:
            encstring = encstring + chr(ord(i) + key1)
    return encstring

message = raw_input("What would you like to do?\n1. Encrypt\n2. Decrypt\n")
if message == "1":
    print("Enter the string to Encrypt:")
    str_input = raw_input()
    print("Enter the key (Eg. 21):")
    keyp = int(raw_input())
    keyp = keyp % 26
    print("Encrypted string:", Encryptmessage(str_input, keyp))
elif message == "2":
    print("Enter the string to Decrypt:")
    str_input = raw_input()
    print("Enter the key (Eg. 21):")
    keyp = -int(raw_input())
    keyp = keyp % 26
    print("Decrypted String:", Encryptmessage(str_input, keyp))
#ixi inkhat
