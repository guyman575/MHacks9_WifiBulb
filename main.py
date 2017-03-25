import os
from time import sleep

RED = '56ff000000f0aa'
GREEN = '5600ff0000f0aa'
BLUE = '560000ff00f0aa'
WHITE = '56fffffffff0aa'
OFF = '5600000000f0aa'

def change_color(color):
    os.system('sudo gatttool -b D2:39:79:10:18:87 --char-write-req --handle=0x0043 --value=' + color)

def main():
    print("HI")

    while True:
        sleep(.1)
        change_color(RED)
        sleep(.1)
        change_color(GREEN)
        sleep(.1)
        change_color(BLUE)

if __name__ == "__main__":
    main()
