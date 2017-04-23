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

    #realiza um dump na tabela do banco de dados e salva no arquivo csv (executado pelo botão gera rel)
    def rel_hosts(self):
        DBSession = sessionmaker(bind=engine)
        session = DBSession()

        f = ('id', 'ip', 'comunidade', 'contato', 'desc', 'uptime', 'idObject')
        with open('mycsvfile.csv', 'wb') as csv_file:
            w = csv.DictWriter(csv_file,fieldnames=f)
            for user in session.query():

                w.writerow(f)

    #Exclui toda a tabela (executado pelo botão Limpar)
    def drop(self):
        host.metadata.drop_all(engine) #drop da tabela
        base.metadata.create_all(engine) #cria a tabela vazia


base.metadata.create_all(engine)


