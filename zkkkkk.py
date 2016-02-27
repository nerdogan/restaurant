from ZKK import Zkem
zk = Zkem()

if zk.connect('192.168.2.224'):
    if zk.disable():
        if zk.get_attendance_log():
            log = zk.unpack_attendance_log()
            print log


    zk.enable()
    zk.disconnect()