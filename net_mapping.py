import nmap
import socket
import fcntl
import struct





def get_network_ip(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])
    # return '10.0.0.196'

    
def get_macs(ip_address):
    nm = nmap.PortScanner()
    hosts = ip_address + '/24'
    nm.scan(hosts=hosts,arguments='--host-timeout 2')

    macs = []
    for h in nm.all_hosts():
        if 'mac' in nm[h]['addresses']:
            macs.append(nm[h]['addresses']['mac'])

    return macs
