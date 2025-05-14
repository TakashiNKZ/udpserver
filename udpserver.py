import socket
from datetime import datetime, timezone, timedelta

# Параметры сервера
UDP_IP = "0.0.0.0"      # слушать на всех интерфейсах
UDP_PORT = 5005         # порт, тот же, что на ESP32
LOG_FILE = "logs.txt"   # файл для записи
TIMEZONE = timezone(timedelta(hours=3))  # Украина: GMT+3

def main():
    # Создаём UDP-сокет
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    sock.settimeout(5.0)  # чтобы не блокировался навечно

    print(f"Listening on UDP {UDP_IP}:{UDP_PORT}…", flush=True)

    try:
        while True:
            try:
                # Принимаем данные с таймаутом
                data, addr = sock.recvfrom(1024)
                now = datetime.now(TIMEZONE)
                text = data.decode('utf-8', errors='replace').strip()
                print(f"Received from {addr} at {now.strftime('%d/%m/%Y %H:%M:%S')}: {text}", flush=True)

                # Записываем в лог
                with open(LOG_FILE, 'a', encoding='utf-8') as f:
                    f.write(f"{text} {now.strftime('%d/%m/%Y %H:%M:%S')}\n")

            except socket.timeout:
                # Ничего не пришло — просто ждём дальше
                continue

    except KeyboardInterrupt:
        print("\nShutting down server.")
    finally:
        sock.close()

if __name__ == "__main__":
    main()
