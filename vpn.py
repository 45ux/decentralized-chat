import os
import subprocess

class VPNClient:
    def __init__(self, interface="wg0"):
        self.interface = interface

    def generate_keys(self):
        private_key = subprocess.check_output("wg genkey", shell=True).decode().strip()
        public_key = subprocess.check_output(f"echo {private_key} | wg pubkey", shell=True).decode().strip()
        return private_key, public_key

    def configure_vpn(self, private_key, peer_public_key, peer_ip, listen_port=51820):
        config = f"""
        [Interface]
        PrivateKey = {private_key}
        Address = 10.0.0.1/24
        ListenPort = {listen_port}

        [Peer]
        PublicKey = {peer_public_key}
        AllowedIPs = {peer_ip}/32
        """
        config_path = f"/etc/wireguard/{self.interface}.conf"
        with open(config_path, "w") as f:
            f.write(config)

        subprocess.run(f"wg-quick up {self.interface}", shell=True, check=True)

    def stop_vpn(self):
        subprocess.run(f"wg-quick down {self.interface}", shell=True, check=True)