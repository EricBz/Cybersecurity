from cryptography.fernet import Fernet

# 1. Generación de la Clave (Simulando el intercambio de llaves seguro)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def vpn_tunnel_send(message):
    print(f"\n[CLIENTE] Mensaje original: {message}")
    
    # CIFRADO: Protegemos el contenido
    payload_cifrado = cipher_suite.encrypt(message.encode())
    
    # ENCAPSULAMIENTO: Creamos el "paquete" que viajará por la red
    packet = {
        "header": {"src": "192.168.1.5", "dst": "10.0.0.1", "proto": "UDP/443"},
        "payload": payload_cifrado
    }
    print(f"[RED] Transmitiendo paquete cifrado: {packet['payload'][:20]}...")
    return packet

def vpn_tunnel_receive(packet):
    print(f"[SERVIDOR] Paquete recibido de: {packet['header']['src']}")
    
    # DESENCAPSULAMIENTO Y DESCIFRADO
    try:
        mensaje_descifrado = cipher_suite.decrypt(packet['payload']).decode()
        print(f"[SERVIDOR] Mensaje final descifrado: {mensaje_descifrado}")
    except Exception as e:
        print("[ALERTA] Error de integridad: No se pudo descifrar el paquete.")

# --- SIMULACIÓN ---
mensaje_privado = "Esta es la clase de ciberseguridad..."
paquete_en_transito = vpn_tunnel_send(mensaje_privado)
vpn_tunnel_receive(paquete_en_transito)
