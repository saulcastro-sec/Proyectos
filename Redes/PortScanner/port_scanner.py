import socket
from datetime import datetime

# Función para escanear puertos
def scan_ports(target, start_port, end_port):
    # Convertir la IP objetivo a una dirección IP válida
    ip = socket.gethostbyname(target)
    print(f"Escaneando la dirección IP {ip} en el rango de puertos {start_port}-{end_port}")

    # Guardar la fecha y hora de inicio
    start_time = datetime.now()

    # Iterar sobre el rango de puertos
    for port in range(start_port, end_port + 1):
        # Crear un socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Tiempo de espera de 1 segundo para cada puerto

        # Intentar conectar al puerto
        result = sock.connect_ex((ip, port))

        if result == 0:
            print(f"Puerto {port} está abierto.")
        else:
            print(f"Puerto {port} está cerrado o filtrado.")
        
        # Cerrar el socket
        sock.close()

    # Tiempo de ejecución total
    end_time = datetime.now()
    total_time = end_time - start_time
    print(f"\nEscaneo completado en {total_time}")

if __name__ == "__main__":
    # Solicitar al usuario la IP y los puertos a escanear
    target_ip = input("Introduce la dirección IP a escanear: ")
    port_range = input("Introduce el rango de puertos (ejemplo: 20-80): ")
    
    # Separar el rango de puertos
    start_port, end_port = map(int, port_range.split('-'))

    # Llamar a la función de escaneo
    scan_ports(target_ip, start_port, end_port)
