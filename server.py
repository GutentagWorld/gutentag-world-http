#!/usr/bin/env python3
"""Raw HTTP server using socket module only.

Run: python3 server.py
Fetch: curl http://localhost:8080/
"""
import socket

HOST = ''
PORT = 8080
BODY = b'Gutentag, World!'
RESPONSE = (
    b'HTTP/1.1 200 OK\r\n'
    b'Content-Type: text/plain; charset=utf-8\r\n'
    b'Content-Length: ' + str(len(BODY)).encode() + b'\r\n'
    b'Connection: close\r\n'
    b'\r\n'
) + BODY

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f'Listening on http://localhost:{PORT}')
    while True:
        conn, addr = server.accept()
        with conn:
            conn.recv(4096)  # read and discard the request
            conn.sendall(RESPONSE)
