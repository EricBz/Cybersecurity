import time

# 1. Definimos las reglas de seguridad (Lista Negra)
IP_BLOCKLIST = ["192.168.1.50", "10.0.0.7"]
PUERTOS_PROHIBIDOS = [21, 22, 23] # FTP, SSH, Telnet (Puertos inseguros)

def firewall_check(ip_origen, puerto_destino):
    print(f"\n[FIREWALL] Analizando paquete: {ip_origen}:{puerto_destino}...")
    time.sleep(1) # Simula el tiempo de procesamiento
    
    # REGLA 1: Filtrado por IP
    if ip_origen in IP_BLOCKLIST:
        return " BLOQUEADO: IP en lista negra (Posible atacante)"
    
    # REGLA 2: Filtrado por Puerto
    if puerto_destino in PUERTOS_PROHIBIDOS:
        return f" BLOQUEADO: Intento de conexión a puerto crítico ({puerto_destino})"
    
    # REGLA 3: Permitir todo lo demás
    return " PERMITIDO: El paquete cumple las políticas de seguridad"

# --- SIMULACIÓN DE TRÁFICO ENTRANTE ---
trafico = [
    {"ip": "192.168.1.10", "puerto": 80},   # Tráfico web normal
    {"ip": "192.168.1.50", "puerto": 443},  # IP sospechosa
    {"ip": "172.16.0.5", "puerto": 22},     # Intento de acceso SSH
    {"ip": "8.8.8.8", "puerto": 443}        # DNS de Google (seguro)
]

for paquete in trafico:
    resultado = firewall_check(paquete["ip"], paquete["puerto"])
    print(f"RESULTADO: {resultado}")
