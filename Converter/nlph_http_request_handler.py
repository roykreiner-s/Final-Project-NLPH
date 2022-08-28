#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse
import time
from parser import run_text

hostName = "localhost"
serverPort = 3002


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(
            bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(
            bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

    def do_POST(self):
        parsed_url = urlparse(self.path)
        print(f"Handling POST request - {parsed_url.path}")

        post_body = self.rfile.read(int(self.headers.get('Content-Length')))
        post_body_json = json.loads(post_body.decode('utf-8'))
        line = run_text(post_body_json['text'])

        # response
        self.send_response(200)
        self.send_header("Content-type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(bytes(line, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
