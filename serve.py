#!/usr/bin/env python3
"""
Simple HTTP server to serve the Chicken Butt timer on local network.
Run this script and access from your phone using the displayed IP address.
"""

import http.server
import socketserver
import socket

def get_local_ip():
    """Get the local IP address of this machine."""
    try:
        # Create a socket to find the local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Connect to an external address (doesn't actually send data)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        return "localhost"

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler to serve files from current directory."""
    
    def end_headers(self):
        # Add CORS headers to allow audio playback
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

def main():
    PORT = 8000
    local_ip = get_local_ip()
    
    with socketserver.TCPServer(("0.0.0.0", PORT), MyHTTPRequestHandler) as httpd:
        print("=" * 60)
        print("🐔 Hurry Up Chicken Butt Timer Server 🐔")
        print("=" * 60)
        print(f"\nServer running on port {PORT}")
        print(f"\n📱 Access from your phone at:")
        print(f"   http://{local_ip}:{PORT}")
        print(f"\n💻 Access locally at:")
        print(f"   http://localhost:{PORT}")
        print(f"\nPress Ctrl+C to stop the server")
        print("=" * 60)
        print()
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n🛑 Server stopped")
            print("=" * 60)

if __name__ == "__main__":
    main()
