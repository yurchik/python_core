from struct import *

# Store as byte
packet_byte = pack('iif', 5, 7, 3.8)
print(packet_byte)

print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))

#  Get back normal data
print(unpack('iif', packet_byte))