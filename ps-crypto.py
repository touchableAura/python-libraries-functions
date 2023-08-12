from cryptography.fernet import Fernet 

f_key = Fernet.generate_key()
print("KEY: " + str(f_key))
f_enc = Fernet(f_key)

enc_string = f_enc.encrypt(b"Password_2_be_kept_secret!")

print("ECRYPTED: " + str(enc_string))
print("DECRYPTEDl " + str(f_enc.decrypt(enc_string)))

# expect:
# C:\Users\19023\Documents\python-libraries-functions>py ps-crypto.py
# KEY: b'rgT5sw4v1nwtmmjBv0MfyHAN_KObbVAivFa1jl6_U0c='
# ECRYPTED: b'gAAAAABkz9DDveV-_WlwXHA9vyIm7yWFGVvvykWrzeFH5ZwVjpY4E5esFoxKoEMkLKqqyydWfvS1rQokTBg9aeSnfWQHRDUkf1EaSMJJaSSERcFRZJ-5hc4='
# DECRYPTEDl b'Password_2_be_kept_secret!'