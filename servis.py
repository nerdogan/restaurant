# -*- coding:utf8 -*-
import sys
import socket
reload(sys)
import time
import soco
from soco.snapshot import Snapshot
import urllib

kontrol=1

"""from pushetta import Pushetta

sys.setdefaultencoding('utf8')
API_KEY = "58fee02c2e20ed7511b179af994fc34850f84656"
CHANNEL_NAME = "garson1"
p = Pushetta(API_KEY)
appnot="mutfak please !"
"""
def garson(sonoss,kontrol):
    zone = list(soco.discover(include_invisible=1, interface_addr="192.168.2.83"))
    for speaker in zone:
        if speaker.player_name == sonoss:
            device = speaker
            kontrol=0
    if kontrol!=0:
        return
    device.group.coordinator.snap = Snapshot(device.group.coordinator)
    device.group.coordinator.snap.snapshot()
    print device.player_name
    print device.group.coordinator.player_name
    device.volume = 40
    device.group.coordinator.play_uri(
        'x-file-cifs://Wdmycloud/namik/Mutlu%20Y%c4%b1llar%20Sana%20-%203%20Do%c4%9fum%20G%c3%bcn%c3%bc%20%c5%9eark%c4%b1s%c4%b1%20Bir%20Arada.mp4')
    time.sleep(10)
    device.group.coordinator.snap.restore()


    #device.volume += 10


HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print 'Serving HTTP on port %s ...' % PORT
while True:
    device = u"""<!DOCTYPE html> <html><head>
      <meta charset="UTF-8">
    </head>
     <body> """

    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print request.decode('utf-8')
    elma=request.split(" ")
    armut=" "
    if len(elma)>2:
        armut= urllib.unquote(elma[1])

    zone = list(soco.discover(include_invisible=1, interface_addr="192.168.2.83"))
    for speaker in zone:
        device = device+'<br><br><br><a href="http://192.168.2.83:8888/'+speaker.player_name+'"> <button style="font-size : 80px;width:500px;height:100px;" >'+speaker.player_name+'</button></a>'

    http_response = """\
HTTP/1.1 200 OK \n Content-Type: text/html \n \n
 """+device.encode("utf-8")
    client_connection.sendall(http_response)
    client_connection.close()

    kontrol=1
    if len(armut)>1:
        garson(armut[1:].decode("utf-8"),kontrol)



