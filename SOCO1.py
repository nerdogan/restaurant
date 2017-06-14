

import soco
from soco.snapshot import Snapshot
import time

""" Prints the name of each discovered player in the network. """
zone = list(soco.discover(include_invisible=1,interface_addr="192.168.2.83"))
for speaker in zone:
        if speaker.player_name == "Kat 2":
            device = speaker



#device.volume += 10

device.group.coordinator.snap=Snapshot(device.group.coordinator)
device.group.coordinator.snap.snapshot()
print device.player_name
print device.group.coordinator.player_name
device.group.coordinator.play_uri('x-file-cifs://Wdmycloud/namik/Mutlu%20Y%c4%b1llar%20Sana%20-%203%20Do%c4%9fum%20G%c3%bcn%c3%bc%20%c5%9eark%c4%b1s%c4%b1%20Bir%20Arada.mp4')
time.sleep(5)
device.group.coordinator.snap.restore()