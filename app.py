import time

def monitor_system():
    # Simulación de lo que haces en Bancaribe
    nodes = ["Servidor-Pagos", "API-Suiche7B", "Base-Datos-Oracle"]
    print("Iniciando sistema de monitoreo v1.0...")
    
    for node in nodes:
        print(f"Revisando estado de: {node}...")
        time.sleep(1)
        print(f"Resultado: {node} está OPERATIVO ✅")

if __name__ == "__main__":
    monitor_system()
