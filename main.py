import os
from time import sleep
from speed_color import speed_color
import threading
from net_mapping import get_macs
from net_mapping import get_network_ip
import sys
RED = '56ff000000f0aa'
GREEN = '5600ff0000f0aa'
BLUE = '560000ff00f0aa'
WHITE = '56fffffffff0aa'
OFF = '5600000000f0aa'
threads = {}
active_macs = {'F8:32:E4:DE:27:11': 0, '64:9A:BE:D5:5F:6D': 0}
saved_macs = ['F8:32:E4:DE:27:11','64:9A:BE:D5:5F:6D']
CONNECTED = True




def change_color(color):
    result = 1
    while result != 0:
        if CONNECTED:
            result = os.system('sudo gatttool -b D2:39:79:10:18:87 --char-write-req --handle=0x0043 --value=' + color)
        else:
            result = os.system('sudo gatttool -b D2:39:79:10:18:87 --char-write-req --handle=0x0043 --value=' + OFF)


def check():
    color = speed_color()
    packet = '56' + color + '00f0aa'
    change_color(packet)

def color_loop():
    while True:
        if CONNECTED:
            print("getting color")
            check()
        else:
            sleep(1)
            print("sleeping")

def loop_check():

    while True:
        sleep(10)
        print("CHECKING...")
        c = check_dict()
        if CONNECTED == True:
            if c == False:

                change_color(OFF)
        global CONNECTED
        CONNECTED = c



def loop_map():
    ip = get_network_ip()
    while True:
        macs = get_macs(ip)
        for key in active_macs.iterkeys():
            active_macs[key] += 1
        for mac in macs:
            active_macs[mac] = 0
        print(macs)
        print(active_macs)

def check_dict():

    kill = True
    for mac in saved_macs:
        if active_macs[mac] < 3:
            kill = False
            break
    if kill:
        return False
    else:
        return True


def main():
    mode = ''
    if len(sys.argv) > 1:
        mode = sys.argv[1]

    t = threading.Thread(target=color_loop)
    t.start()
    threads['color'] = t
    if mode == 'mapping':
        t = threading.Thread(target=loop_map)
        t.start()
        threads['map'] = t
        t = threading.Thread(target=loop_check)
        t.start()
        threads['check'] = t

if __name__ == "__main__":
    main()
