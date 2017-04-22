import kivy
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

from threading import Thread, Timer

class SnmpToolApp(App):
    btn1 = 'Consultar'
    btn2 = 'Agendar'
    btn3 = 'Gerar Rel'
    btn4 = 'Limpar'




    def gerar_rel(self):
        dbmanager.host.rel_hosts(self)

    def clean(self):

        dbmanager.host.drop(self)

    def get_agendado(self, ip, community,time1, time2):
        tempo_cont = int(time2)
        tempo_final = int(time1)
        time.sleep(tempo_cont)
        tempo = 0


        if tempo < tempo_final:
            tempo = time.time()

            while tempo < tempo_final:
                a = self.get_values_form(ip, community)
                print(tempo)
                result = ' community ' + community
                Thread(target= self.get_agendado, kwargs={'self': self,
                                                              'ip': ip,
                                                              'community': community,
                                                              'time2': time2
                                                              }).start()




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
