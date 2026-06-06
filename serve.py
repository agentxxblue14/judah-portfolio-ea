import http.server, os, socketserver, sys
d = os.path.dirname(os.path.abspath(__file__))
print(f"Serving from {d}", flush=True)
os.chdir(d)
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", 8080), http.server.SimpleHTTPRequestHandler) as s:
    s.serve_forever()
