from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

# scrypt is a key derivation function 
# designed for password storage
# can slow down an attack by tuning memory

# salt can be made by individuals and stored in plain text but not shared publicly
salt = b"!long*rand0m%salt$string@"

# DERIVING THE HASH 
s_enc = Scrypt(
                 salt=salt,
                 length=64,   # length of key
                 n=2048,      # CPU memory cost 
                 r=8,         # block size 
                 p=1,         # parilization 
            )
enc_pword = s_enc.derive(b"Password_2_be_kept_secret!")
print("Derived Key: " + str(enc_pword))

# VERIFYING THE HASH
s_enc = Scrypt(
    salt=salt,
    length=64,
    n=2048,
    r=8,
    p=1
)

print("Password Exception: ")
# print(s_enc.verify(b"Password_2_be_kept_secret!", enc_pword))
print(s_enc.verify(b"Password_2_be_kept_secret", enc_pword))
# expect: None (if passwords match) 