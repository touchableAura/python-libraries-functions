from scapy.all import *

#SNIFFING
result=sniff(count=5)
#result=sniff(filter='tcp', count=2) #Only show first 3 TCP packets sniffed

result.nsummary()
result.[0].show()
