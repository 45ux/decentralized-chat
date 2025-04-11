from encryption.aes import AESCipher
from encryption.kyber import KyberCipher
from encryption.sphincs import SPHINCSPlus
from p2p.vpn import VPNClient
from p2p.tor_client import TorClient
import base64

def main():
    print("🌐 Vítejte v P2P chatovací aplikaci s VPN a Tor šifrováním!")
    
    # Inicializace
    vpn = VPNClient()
    tor = TorClient()
    kyber = KyberCipher()
    aes = AESCipher()
    sphincs = SPHINCSPlus()

    # Generování VPN klíčů
    private_key, public_key = vpn.generate_keys()
    print(f"VPN veřejný klíč: {public_key}")

    # Konfigurace VPN
    peer_public_key = input("Zadejte veřejný klíč peeru: ")
    peer_ip = input("Zadejte IP adresu peeru (např. 10.0.0.2): ")
    vpn.configure_vpn(private_key, peer_public_key, peer_ip)

    # Příprava šifrované zprávy
    message = input("Zadejte zprávu k odeslání: ")
    aes_key = aes.generate_key()
    encrypted_message = aes.encrypt(message, aes_key)
    encrypted_key = kyber.encrypt(base64.b64encode(aes_key).decode(), kyber.generate_keys()[0])
    signature = sphincs.sign(encrypted_message, sphincs.generate_keys()[1])

    # Přenos zprávy
    print("Zpráva bude odeslána přes VPN nebo Tor...")
    tor.send_message({
        "encrypted_message": encrypted_message,
        "encrypted_key": encrypted_key,
        "signature": signature,
    })

    # Přijímání
    received_data = tor.receive_message()
    print("Přijatá šifrovaná zpráva:", received_data)

if __name__ == "__main__":
    main()