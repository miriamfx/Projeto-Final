#!/usr/bin/env python
#coding: utf-8

# @autor: Míriam Félix Lemes da Silva
# @contato: miriamfx2@gmail.com
# @data: 08 de Abril de 2017

from pysnmp.hlapi import *
from kivy.properties import ObjectProperty
from os import *
import dbmanager
import os.path
import os
from datetime import datetime

class SimpleSnmp():
    def __init__(self, ip, community):#recebe os atributos de entrada do main
        self.ip = ip
        self.community = community


    def GetSNMP(self): #realiza o get snmp
        data = (
            ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysLocation', 0)),
            ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)),
            ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysObjectID', 0)),
            ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysUpTime', 0)),
            ObjectType(ObjectIdentity('IP-MIB', 'ipInDelivers', 0)),
            ObjectType(ObjectIdentity('IP-MIB', 'ipOutRequests', 0))

        )

        g = getCmd(SnmpEngine()
                   , CommunityData(self.community, mpModel=1)
                   , UdpTransportTarget((self.ip, 161))
                   , ContextData()
                   , *data)

        errorIndication, errorStatus, errorIndex, varBinds = next(g)

        if errorIndication:
            print(errorIndication)
        elif errorStatus:
            print('%s at %s' % (
                errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'
            )

                  )
        else:
            lista = []
            cont = 0
            for varBind in varBinds:
                if cont < 7:
                    lista.append((' = '.join([x.prettyPrint() for x in varBind])))
                    cont = cont + 1


        host = dbmanager.host()
        #salva a requisição no banco de dados
        host.ip = self.ip
        host.comunidade = self.community
        host.contact = str(lista[0])
        host.desc = str(lista[1])
        host.idObject = str(lista[2])
        host.location = str(lista[3])
        host.uptime = str(lista[4])
        host.ipInDelivers = str(lista[5])
        host.ipOutRequests = str(lista[-1])
        host.data = str(datetime.now)

        host.save()

        return str(lista)
