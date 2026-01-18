import time
import random

def monitor_system():
    nodes = ["Servidor-Pagos", "API-Suiche7B", "Base-Datos-Oracle"]
    print("--- INICIANDO MONITOREO DE ALTA DISPONIBILIDAD ---")
    
    while True:
        for node in nodes:
            # Simulamos que hay un 20% de probabilidad de que falle
            if random.random() < 0.2:
                print(f"[{time.ctime()}] ⚠️ ALERTA: {node} está CAÍDO ❌")
            else:
                print(f"[{time.ctime()}] {node} está OPERATIVO ✅")
        
        print("-" * 30)
        time.sleep(5) # Espera 5 segundos para la próxima revisión

if __name__ == "__main__":
    monitor_system()
