from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.popup import Popup
from get import SimpleSnmp
import dbmanager
import time
import re
import sys
from threading import Thread

from threading import Thread, Timer

class SnmpToolApp(App):
    btn1 = 'Consultar'
    btn2 = 'Agendar'
    btn3 = 'Gerar Rel'
    btn4 = 'Limpar'




    def gerar_rel(self):
        dbmanager.host.rel_hosts(self)
        result = 'Relatório gerado com sucesso.'
        self.set_result_form(result)

    def clean(self):

        dbmanager.host.drop(self)
        result = 'Drop table realizado com sucesso.'
        self.set_result_form(result)



    def get_agendado(self, ip, community,time1, time2):
        Thread.__init__(self)
        tempo_cont = (time2)
        tempo_final = (time1)

        tempo = 0

        while tempo < tempo_final:
            cont = time.time()
            tempo = cont+tempo
            time.sleep(tempo_cont)

            self.get_values_form(ip, community)


            Thread(target= self.get_agendado, kwargs={'self': self,
                                                              'ip': ip,
                                                              'community': community,
                                                              'time2': time2
                                                              }).start()

        self.set_result_form(self.result)



    def build(self):
        Window.size = (1000, 750)
        self.load_kv('main.kv')

    def set_result_form(self, resultado):
        self.root.ids.textinput_resultado.text = resultado
        print (resultado)



    def get_values_form(self, ip, community):
        a = SimpleSnmp(ip, community)
        result = a.GetSNMP()
        result = result + '\n IP ' + ip
        result = result + ' e Community ' + community
        self.set_result_form(result)




if __name__ == "__main__":
    SnmpToolApp().run()
