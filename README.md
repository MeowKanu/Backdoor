# Backdoor (Reverse Shell) Tool

This project implements a Python-based reverse shell with command execution, file upload/download, and JSON-based data communication.

The project includes two scripts:

- **client.py** → The backdoor that connects to the server.
- **server.py** → The listener that controls the client.

## Features

- Reverse shell connection
- Persistent retry logic
- Execute system commands
- Change directory (cd)
- Upload files to the victim
- Download files from the victim
- JSON-based reliable communication
- Base64-encoded file transfer

## Project Structure

reverse-shell/
│── client.py
│── server.py
└── README.md

shell
Copy code

## Usage

### 1. Start the server (listener)
python server.py

shell
Copy code

### 2. Run the client (backdoor)
python client.py

pgsql
Copy code

### 3. Supported Commands

| Command | Description |
|--------|-------------|
| ls / dir | List files |
| cd PATH | Change directory |
| download FILE | Download file from client |
| upload FILE | Upload file to client |
| exit | Close connection |

## Notes

- Update the IP in client.py before running.
- Use in a legal, ethical environment only.
- Best tested on local network (127.0.0.1 or LAN IPs).

## License

MIT License
