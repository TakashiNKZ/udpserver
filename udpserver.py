import socket
from datetime import datetime

# Параметры сервера
UDP_IP = "0.0.0.0"      # слушать на всех интерфейсах
UDP_PORT = 5005         # порт, тот же, что на ESP32
LOG_FILE = "logs.txt"   # файл для записи

def main():
    # Создаём UDP-сокет
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    print(f"Listening on UDP {UDP_IP}:{UDP_PORT}…")

    try:
        while True:
            # Принимаем данные
            now = datetime.now()
            data, addr = sock.recvfrom(1024)
            text = data.decode('utf-8', errors='replace').strip()
            print(f"Received from {addr}: {text}")

            # Записываем в файл
            with open(LOG_FILE, 'a', encoding='utf-8') as f:
                f.write(text + ' ' + now.strftime("%d/%m/%Y %H:%M:%S") +'\n')
    except KeyboardInterrupt:
        print("\nShutting down server.")
    finally:
        sock.close()
if __name__ == "__main__":
    main()
