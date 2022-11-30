from cryptography.fernet import Fernet

#--------------------------------key generation-----------------------------------------

key=Fernet.generate_key()
#print(key)


#----------------------------------------key storing-----------------------------------

fernet=Fernet(key) 
with open('key.key', 'wb') as filekey:
    filekey.write(key)
with open('key.key', 'rb') as filekey:
    key=filekey.read()


#-----------------------------Encryption of Audio------------------------------------------------

with open('sample.mp3', 'rb') as file:
    originalaudio=file.read()
encrypted=fernet.encrypt(originalaudio)

with open("encrypted.mp3",'wb') as encrypted_file:
    encrypted_file.write(encrypted)



#---------------------------Decryption of Audio--------------------------------

with open('encrypted.mp3', 'rb') as file:
    originalaudio=file.read()
decrypted=fernet.decrypt(originalaudio)

with open("decrypted audio.mp3",'wb') as dec_file:
    dec_file.write(decrypted)
