import time

class FirewallInteligente:
    def __init__(self):
        self.blocklist = set()       # IPs baneadas permanentemente
        self.intentos_fallidos = {}  # Contador: {ip: numero_de_intentos}
        self.MAX_INTENTOS = 3        # Umbral para banear
        self.puertos_criticos = [21, 22, 23, 3389] # FTP, SSH, Telnet, RDP

    def analizar_paquete(self, ip, puerto):
        print(f"\n[Filtro] Analizando tráfico de {ip} al puerto {puerto}...")

        # 1. Verificar si ya está baneado
        if ip in self.blocklist:
            return f"RECHAZADO: La IP {ip} está en la lista negra definitiva."

        # 2. Verificar si intenta tocar puertos prohibidos
        if puerto in self.puertos_criticos:
            # Incrementar contador de sospecha
            self.intentos_fallidos[ip] = self.intentos_fallidos.get(ip, 0) + 1
            intentos = self.intentos_fallidos[ip]
            
            print(f"ALERTA: Intento de acceso a puerto crítico ({intentos}/{self.MAX_INTENTOS})")

            # 3. Regla de Baneo Automático (IPS)
            if intentos >= self.MAX_INTENTOS:
                self.blocklist.add(ip)
                return f" BANEO AUTOMÁTICO: IP {ip} bloqueada por comportamiento malicioso."
            
            return f" BLOQUEADO: Acceso denegado al puerto {puerto}."

        return " PERMITIDO: Tráfico legítimo."

# --- SIMULACIÓN DE UN ATAQUE DE ESCANEO DE PUERTOS ---
ips = FirewallInteligente()
ataque_simulado = [
    {"ip": "192.168.1.10", "p": 80},   # Normal
    {"ip": "10.0.0.5", "p": 22},       # Intento 1 (Sospechoso)
    {"ip": "10.0.0.5", "p": 21},       # Intento 2 (Sospechoso)
    {"ip": "192.168.1.10", "p": 443},  # Normal
    {"ip": "10.0.0.5", "p": 23},       # Intento 3 -> ¡Baneo!
    {"ip": "10.0.0.5", "p": 80}        # Intento después del baneo
]

for pqt in ataque_simulado:
    time.sleep(0.5)
    resultado = ips.analizar_paquete(pqt["ip"], pqt["p"])
    print(resultado)
