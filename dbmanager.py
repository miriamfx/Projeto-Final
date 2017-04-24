#!/usr/bin/env python
#coding: utf-8

# @autor: Míriam Félix Lemes da Silva
# @contato: miriamfx2@gmail.com
# @data: 08 de Abril de 2017
from sqlalchemy import create_engine, Table, Column, MetaData,engine
from sqlalchemy import Table, Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.serializer import loads, dumps
from sqlalchemy.orm import sessionmaker
from sqlalchemy import delete, select
import csv
import subprocess
import get
import os.path

#conecta o banco de dados
base = declarative_base()
engine = create_engine('sqlite:///snmpdb.db')
base.metadata.bind = engine

#cria a tabela
class host(base):
    __tablename__ = 'hosts'
    id = Column(Integer,primary_key=True)
    ip = Column(String(15))
    comunidade = Column(String(8))
    contact = Column(String)
    desc = Column(String)
    uptime = Column(String)
    idObject = Column(String(100))
    location = Column(String(100))
    ipInDelivers = Column(String)
    ipOutRequests = Column(String)
    data = Column(String)


    def save(self):
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        session.add(self)
        session.commit()

    #realiza um dump na tabela do banco de dados e salva no arquivo csv (executado pelo botão gera rel)
    def to_dict(self):
        _t = {
            'id': self.id, 'ip': self.ip, 'comunidade': self.comunidade, 'contact': self.contact,
            'desc': self.desc, 'uptime': self.uptime, 'idObject': self.idObject, 'location': self.location,
            'ipInDelivers': self.ipInDelivers, 'ipOutRequests': self.ipOutRequests,
            'data': self.data,
        }
        return _t
    def rel_hosts(self):
        DBSession = sessionmaker(bind=engine)
        session = DBSession()

        with open('snmp_rel.csv', 'w') as csv_file:  # Just use 'w' mode in 3.x
            fieldnames = [
                'id', 'ip', 'comunidade', 'contact', 'desc', 'uptime', 'idObject', 'location',
                'ipInDelivers','ipOutRequests','data'
            ]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            #writer.writeheader()
            for row in session.query(host).order_by('id'):
                writer.writerow(row.to_dict())

    #Exclui toda a tabela (executado pelo botão Limpar)
    def drop(self):
        host.metadata.drop_all(engine) #drop da tabela
        base.metadata.create_all(engine) #cria a tabela vazia

base.metadata.create_all(engine)


