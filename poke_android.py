## .\adb devices
# %%
from time import sleep
import os
from ppadb.client import Client as AdbClient #pip install -U pure-python-adb
from PIL import Image #Pillow
from poke_friends import busca

# %%
def conecta_android():
    client = AdbClient(host="127.0.0.1", port=5037)
    print(client.version())
    os.system('adb kill-server')
    sleep(1)
    os.system('adb usb')
    sleep(1)
    os.system('adb devices')
    sleep(1)
    os.system('adb tcpip 5556')
    sleep(1)
    os.system('adb connect "192.168.0.11:5556"')
    sleep(1)
    device = client.device("192.168.0.11:5556")
    device.shell("echo hello world !")
    return device

# %%

def screencap(show=True):
    result = device.screencap()
    with open("screen.png", "wb") as fp:
        fp.write(result)
    if show:
        Image.open('screen.png').show()


# %%
def insert_qr_code():
    device.shell("input tap 503 503") # adicionar amigos
    sleep(3)
    device.shell("input tap 728 238") # codigoqr
    sleep(3)
    device.shell("input tap 520 1250") # ok
    sleep(3)

 # %%
def insert_number(number):
    device.shell("input tap 250 1400") # caixa de texto
    sleep(.2)
    device.shell(f"input text {number}") # insere o numero
    sleep(.2)
    device.shell("input tap 500 900") # ok
    sleep(1)
    device.shell("input tap 500 900") # ok
    sleep(3)
    device.shell("input tap 500 1250") # ok


#%%
lista,_ = busca(cidade='Niterói', paginas=10)
lista

# %%
device = conecta_android()
device
#%%
device.shell("input tap 131 1975")  # clica na cara
sleep(1.5)
device.shell("input tap 503 503") # adicionar amigos
sleep(.5)

#%%%
print('lista:',lista)
for number in lista:
    insert_number(number)

#%%
for i in range(1500):
    device.shell("input tap 540 1900")

# %%
