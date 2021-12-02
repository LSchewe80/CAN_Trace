# from can import interface
# import cantools
# import can
# from can import Message
# # from pprint import pprint
# import time
# #from bitarray import bitarray

# #db = cantools.database.load_file('')
# #can_bus = can.interface.Bus('vcan0', bustype='socketcan')

# bus = can.Bus(  interface='socketcan',
#                 channel='can0',
#                 receive_own_messages=True   )

# beginn = True

# while beginn == True:

#     for msg in bus:
#         print("Zeitstempel:{} ; Arbit_ID:{} ; Daten:{}".format(msg.timestamp, msg.arbitration_id, msg.data))

import platform

print(platform.python_version())
print(platform.platform())
