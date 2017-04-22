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
        dbmanager.gera_rel()

    def clean(self):
        dbmanager.drop()

    def agendar(self, ip, community, time1, time2):
        Thread.__init__(self)
        self.stopped = time1

        while not self.stopped.wait(time2):

            a = SimpleSnmp(ip, community)
            result = a.GetSNMP()
            result = result + '\n IP ' + ip
            result = result + ' e Community ' + community


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
