import scapy.all as scapy
import optparse
def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--ipadress",dest="ip_adress",help="Enter Ip Adress")
    (user_input,arguments) = parse_object.parse_args()
    if not user_input.ip_adress:
        print("Enter IP Adress")
    return user_input
def scan_network(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combine = arp_request/broadcast
    (answer,unanswer)=scapy.srp(combine,timeout=1)
    answer.summary()
user_ip_adress = get_user_input()
scan_network(user_ip_adress.ip_adress)
