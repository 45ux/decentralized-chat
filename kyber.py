from pqcrypto.kem.kyber512 import generate_keypair, encrypt, decrypt

class KyberCipher:
    def generate_keys(self):
        public_key, private_key = generate_keypair()
        return public_key, private_key

    def encrypt(self, plaintext, public_key):
        ciphertext, _ = encrypt(public_key, plaintext.encode())
        return ciphertext

    def decrypt(self, ciphertext, private_key):
        plaintext = decrypt(private_key, ciphertext)
        return plaintext.decode()