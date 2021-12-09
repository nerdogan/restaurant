

import soco
from soco.snapshot import Snapshot
import time
from soco.music_services import MusicService


""" Prints the name of each discovered player in the network. """
zone = list(soco.discover(include_invisible=1,interface_addr="192.168.2.49"))
for speaker in zone:
        if speaker.player_name == "Kule 1":
            device = speaker

print(MusicService.get_subscribed_services_names())
print(device.group.coordinator.get_current_transport_info())
device.group.coordinator.snap=Snapshot(device.group.coordinator)
device.group.coordinator.snap.snapshot()
print(device.player_name)
print (device.group.coordinator)
device.volume += 10

device.group.coordinator.play_uri('x-file-cifs://Wdmycloud/namik/yeniyeni/HammAli%20%20Navai%20-%20Птичка.mp3')
time.sleep(10)
device.group.coordinator.snap.restore()