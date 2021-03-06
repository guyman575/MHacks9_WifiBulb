import os
from time import sleep
from speed_color import speed_color
import threading
import net_mapping
from net_mapping import get_network_ip
import sys
import app
from weather_color import weather_to_color
import color_clock
import stock_check
RED = '56ff000000f0aa'
GREEN = '5600ff0000f0aa'
BLUE = '560000ff00f0aa'
WHITE = '56fffffffff0aa'
OFF = '5600000000f0aa'
threads = {}
active_macs = {'F8:32:E4:DE:27:11': 0, '64:9A:BE:D5:5F:6D': 0}
saved_macs = ['F8:32:E4:DE:27:11'] #'64:9A:BE:D5:5F:6D'
CONNECTED = True
MODE = ''
mutex = threading.Lock()

def add_mac(new_mac):
    print("API: ", new_mac)
    if new_mac not in active_macs:
        active_macs[new_mac] = 0
        saved_macs.append(new_mac)

def get_macs():
    return saved_macs

def change_color(color):
    result = 1
    mutex.acquire()
    while result != 0:
        if CONNECTED:
            result = os.system('sudo gatttool -b D2:39:79:10:18:87 --char-write-req --handle=0x0043 --value=' + color)
        else:
            print("off c")
            result = os.system('sudo gatttool -b D2:39:79:10:18:87 --char-write-req --handle=0x0043 --value=' + OFF)
    mutex.release()

def check_speed():
    color = speed_color()
    packet = '56' + color + '00f0aa'
    change_color(packet)


def check_weather():
    color = weather_to_color()
    print(color)
    packet = '56' + color + '00f0aa'
    change_color(packet)

def check_clock():
    color = color_clock.color_clock()
    print(color)
    packet = '56' + color + '00f0aa'
    change_color(packet)

def check_stock():
    color = stock_check.get_stock_color()
    print(color)
    packet = '56' + color + '00f0aa'
    change_color(packet)



def color_loop():

    while True:
        print("FUCK")
        if CONNECTED:
            print("getting color")
            if MODE == 'speed':
                check_speed()
            elif MODE == 'weather':
                check_weather()
                sleep(600)
            elif MODE == 'clock':
                sleep(1)
                check_clock()
            elif MODE == 'stock':
                check_stock()
        else:
            sleep(3)
            print("sleeping")


def loop_check():

    while True:
        sleep(1)
        print("CHECKING...")
        c = check_dict()
        global CONNECTED
        CONNECTED = c



def loop_map():
    ip = str(get_network_ip('wlp4s0'))
    while True:
        macs = net_mapping.get_macs(ip)
        for key in active_macs.iterkeys():
            active_macs[key] += 1
        for mac in macs:
            active_macs[mac] = 0
        print(macs)
        print(active_macs)

def check_dict():

    kill = True
    for mac in saved_macs:
        if active_macs[mac] < 5:
            kill = False
            break
    if kill:
        return False
    else:
        return True


def main(mode):
    global MODE
    MODE = mode
    t = threading.Thread(target=color_loop)
    t.start()
    threads['color'] = t
    t = threading.Thread(target=loop_map)
    t.start()
    threads['map'] = t
    t = threading.Thread(target=loop_check)
    t.start()
    threads['check'] = t

if __name__ == "__main__":
    mode = 'speed'
    if len(sys.argv) > 1:
        mode = sys.argv[1]
    main(mode)
