from pysnmp.hlapi import *
from kivy.properties import ObjectProperty
from os import *
import dbmanager
import os.path
import os


class SimpleSnmp():
    def __init__(self, ip, community):
        self.ip = ip
        self.community = community



    def GetSNMP(self):
        resultado = errorIndication, errorStatus, errorIndex, varBinds = next(
            getCmd(SnmpEngine(),
                   CommunityData(self.community),
                   UdpTransportTarget((self.ip, 161)),
                   ContextData(),

                       ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysContact', 0)),
                       ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)),
                       ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysObjectID', 0)),
                       ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysLocation', 0)),
                       ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysUpTime', 0)),


                      ),
        )
        host = dbmanager.host()
        if errorIndication:
            return str(errorIndication)
        elif errorStatus:
            return str('%s at %s' % (errorStatus.prettyPrint(),
                                     errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        else:
            host.ip = self.ip
            host.comunidade = self.community
            host.contact = str(resultado[0])
            host.desc = str(resultado[1])
            host.idObject = str(resultado[2])
            host.location = str(resultado[3])

            host.save()

        return str(resultado)