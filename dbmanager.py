from sqlalchemy import create_engine, Table, Column, MetaData
from sqlalchemy import Table, Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import delete
import csv
import setthings
import subprocess


engine = create_engine('sqlite:///snmpdb.db')

base = declarative_base()


class Host(base):
    __tablename__ = 'hosts'
    ip = Column(String(15), primary_key=True)
    comunidade = Column(String(8))
    idObject = Column(String)
    contact = Column(String)
    desc = Column(String)
    uptime = Column(String)
    location = Column(String)
    data = Column(String)
    hora = Column(String)
    qtd_mem = Column(String)
    qtd_mem_proc = Column(String)
    ip_Errors = Column(String)

    def save(self):
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        session.add(self)
        session.commit()


    def create_db(self):
        base.metadata.create_all(engine)



    def gera_rel(self):

      pass