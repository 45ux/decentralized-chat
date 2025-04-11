from pqcrypto.sign.sphincs import generate_keypair, sign, verify

class SPHINCSPlus:
    def generate_keys(self):
        public_key, private_key = generate_keypair()
        return public_key, private_key

    def sign(self, message, private_key):
        return sign(private_key, message.encode())

    def verify(self, message, signature, public_key):
        try:
            verify(public_key, signature, message.encode())
            return True
        except Exception:
            return False