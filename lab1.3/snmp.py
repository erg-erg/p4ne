# импорт pysnmp, только High-level API
from pysnmp.hlapi import *

#задаем MIB: 1 по имени, 2 по значению
snmp_object1 = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)
snmp_object2 = ObjectIdentity('1.3.6.1.2.1.2.2.1.2')

#указываем хост
target = ('10.31.70.107', 161)

result = getCmd(SnmpEngine(),
            CommunityData('public', mpModel=0),
            UdpTransportTarget(target), #указываем цель
            ContextData(),
            ObjectType(snmp_object1)) #MIB

for r in result:
    for r2 in r[3]:
        print(r2)

result2 = nextCmd(SnmpEngine(),
            CommunityData('public', mpModel=0),
            UdpTransportTarget(target), #указываем цель
            ContextData(),
            ObjectType(snmp_object2), #MIB
            lexicographicMode=False) #ограничение по глубине

for r in result2:
    for r2 in r[3]:
        print(r2)
