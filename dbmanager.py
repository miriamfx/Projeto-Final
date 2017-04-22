from sqlalchemy import create_engine, Table, Column, MetaData
from sqlalchemy import Table, Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import delete, select
import csv
import setthings
import subprocess
import get
import os.path





base = declarative_base()

engine = create_engine('sqlite:///snmpdb.db')
base.metadata.bind = engine

class host(base):

    __tablename__ = 'hosts'
    ip = Column(String(15), primary_key=True)
    comunidade = Column(String(8))
    contact = Column(String)
    desc = Column(String)
    uptime = Column(String)
    idObject = Column(String(100))
    location = Column(String(100))
    data = Column(String)
    hora = Column(String)
    qtd_mem = Column(String)
    qtd_mem_proc = Column(String)
    ip_Errors = Column(String)


    def save(self):
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        session.add(self)
        resultado = get.SimpleSnmp.resultado

        session.commit()

    def rel_hosts(self):
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        return session.query(host).order_by(host.ip)
        snmp_db = host
        with open(r'snmp.csv', 'a') as data:
            writer = csv.writer(data)
            writer.writerow(snmp_db)

    def drop(self):
        host.metadata.drop_all(engine)


base.metadata.create_all(engine)


