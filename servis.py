# -*- coding:utf8 -*-
import sys
import socket
reload(sys)
from pushetta import Pushetta

sys.setdefaultencoding('utf8')
API_KEY = "58fee02c2e20ed7511b179af994fc34850f84656"
CHANNEL_NAME = "garson1"
p = Pushetta(API_KEY)
appnot="mutfak please !"

def garson():
    p.pushMessage(CHANNEL_NAME, appnot, expire="2017-03-30")


HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print 'Serving HTTP on port %s ...' % PORT
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print request

    http_response = """\
HTTP/1.1 200 OK

Hello, World!
"""
    client_connection.sendall(http_response)
    p.pushMessage(CHANNEL_NAME, appnot, expire="2017-02-28")
    client_connection.close()