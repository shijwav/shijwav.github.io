import http.server
import socketserver
import webbrowser

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Server running at http://localhost:8000")
    webbrowser.open("http://localhost:8000/index.html")
    httpd.serve_forever()