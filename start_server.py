import http.server
import socketserver
import os
import webbrowser
import sys
from pathlib import Path

# Get the current directory
CURRENT_DIR = Path(__file__).parent.absolute()

# Set the port
PORT = 8000

# Change to the nimrahbuildcare.com directory
os.chdir(os.path.join(CURRENT_DIR, 'nimrahbuildcare.com'))

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        http.server.SimpleHTTPRequestHandler.end_headers(self)

# Create the server
handler = MyHttpRequestHandler

# Allow address reuse to avoid WinError 10048
socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"\n✅ Server started at http://localhost:{PORT}")
    print(f"📂 Serving files from: {os.getcwd()}")
    print("🌐 Open your browser to view the website")
    print("⚠️ Press Ctrl+C to stop the server\n")
    
    # Open the browser automatically
    webbrowser.open(f'http://localhost:{PORT}')
    
    # Keep the server running
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped")
        sys.exit(0)