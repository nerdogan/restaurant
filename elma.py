import requests
import nenraconfig
import subprocess
import time as ttim

token=nenraconfig._GetOption2('token')

#a=requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token),  data={'chat_id': 839088426, 'text': "getiryemek kapandı"}).json()

while True:
   # subprocess.Popen("python3 persatt.py", shell=True)

    subprocess.Popen('python3 yemeksepeti.py', shell=True)
    ttim.sleep(40)
   # subprocess.Popen('python3 getiryemek.py', shell=True)
   # ttim.sleep(50)
    subprocess.Popen('python3 getiryemek2.py', shell=True)
    ttim.sleep(50)
    #    subprocess.Popen('python3 siparisyazdir.py', shell=True)
    ttim.sleep(1)
    #    subprocess.Popen('python3 deneme.py', shell=True)
    ttim.sleep(1)
    print("_______________________________________________________________")

