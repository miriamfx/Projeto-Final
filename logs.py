#!/usr/bin/env python
#coding: utf-8

# @autor: Míriam Félix Lemes da Silva
# @contato: miriamfx2@gmail.com
# @data: 08 de Abril de 2017

import get
import dbmanager
import os,sys
from os import path
from datetime import datetime
import time

def logGet(self):
    date = str(time.strftime("%Y-%m-%d"))  #
    now = str(datetime.now())
    logfile = open('%s-getlog.txt' % date,'w')  # Cria o arquivo de Log
    texto = []
    texto.append(now)
    texto.append(' - get REALIZADO')
    logfile.writelines(texto)
    logfile.close()

def logRel(self):
    date = str(time.strftime("%Y-%m-%d"))  #
    now = str(datetime.now())
    logfile = open('%s-relatoriolog.txt' % date, 'w')  # Cria o arquivo de Log
    texto = []
    texto.append(now)
    texto.append(' - relatorio criado')
    logfile.writelines(texto)
    logfile.close()

def logAgendGet(self):
    date = str(time.strftime("%Y-%m-%d"))  #
    now = str(datetime.now())
    logfile = open('%s-Agendamentolog.txt' % date,'w')  # Cria o arquivo de Log
    texto = []
    texto.append(now)
    texto.append(' - Agendamento REALIZADO')
    logfile.writelines(texto)
    logfile.close()

def logDrop(self):
    date = str(time.strftime("%Y-%m-%d"))  #
    now = str(datetime.now())
    logfile = open('%s-droplog.txt' % date,'w')  # Cria o arquivo de Log
    texto = []
    texto.append(now)
    texto.append(' - drop REALIZADO')
    logfile.writelines(texto)
    logfile.close()
