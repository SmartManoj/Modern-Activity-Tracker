
import json
import socket 

TARGET_IP = '192.168.31.55'
TARGET_PORT = 5600

def control_fan(power):
    command = {"power": power}
    message = json.dumps(command).encode('utf-8')
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message, (TARGET_IP, TARGET_PORT))
    print(f"Sent JSON command to {TARGET_IP}:{TARGET_PORT}")
    sock.close()

if __name__ == '__main__':
    control_fan(1)