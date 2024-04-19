print(" _      _   _____ ____ ____  ____   ____") 
print("(_)_  _(_) | ____/ ___/ /\ \|  _ \ / ___|")
print("| \ \/ / | |  _|| |  / /  \ \ | | | |    ")
print("| |>  <| | | |__| |__\ \  / / |_| | |___ ")
print("|_/_/\_\_| |_____\____\_\/_/|____/ \____|")

message=input("What would you like to do?\n1. Encrypt\n2. Decrypt\n")
def Encryptmessage(str,key1):
    encstring=""
    for i in str:
        if(ord(i))>=65 and (ord(i)<=90):
            tempstr=(ord(i)+key1)
            if tempstr>90:
                tempstr=tempstr%90+64
            encstring=encstring+chr(tempstr)
        elif(ord(i))>97 and (ord(i)<=122):
            tempstr=(ord(i)+key1)
            if tempstr>122:
                tempstr=tempstr%122+96
            encstring=encstring+chr(tempstr)
        else:
            encstring=encstring+chr(ord(i)+key1)
    return encstring
if message=="1":
    print("Enter the string to Encrypt")
    str=input()
    print("Enter the key(Eg. 21):")
    keyp=int(input())
    keyp=keyp%26
    print("Encrypted string:", Encryptmessage(str, keyp))
elif message=="2":
    print("Enter the string to Decrypt")
    str=input()
    print("Enter the key(Eg. 21):")
    keyp=-int(input())
    keyp=keyp%26
    print("Decrypted String: ",Encryptmessage(str, keyp))

#ixi inkhat
