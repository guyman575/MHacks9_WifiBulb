import nmap

def get_network_ip():
    return '172.20.10.3'


def get_macs(ip_address):
    nm = nmap.PortScanner()
    hosts = ip_address + '/24'
    nm.scan(hosts=hosts,arguments='--host-timeout 2')

    macs = []
    for h in nm.all_hosts():
        if 'mac' in nm[h]['addresses']:
            macs.append(nm[h]['addresses']['mac'])

    return macs
