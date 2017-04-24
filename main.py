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

from threading import Thread, Timer
#O main é responsável pela delegação das funções
#Cada botão executa uma requisição a um modulo do aplicativo
#Classe principal SnmpTool
class SnmpToolApp(App):
    btn1 = 'Consultar'#executa a função get_values_form()
    btn2 = 'Agendar' #executa a função agendar()
    btn3 = 'Gerar Rel' #executa a função gera_rel()
    btn4 = 'Limpar' #executa a função clean


    def gerar_rel(self): # Esta função é chamada no main.kv no Button btn3
        dbmanager.host.rel_hosts(self)#executa a função host.rel_hosts no dbmanager.py
        result = 'Relatório gerado com sucesso.' #result recebe uma mensagem de sucesso
        self.set_result_form(result) #exibe a mensagem na função set_result_for()

    def clean(self):# Realiza o Drop na tabela do banco de dados
        dbmanager.host.drop(self) #executa a função host.drop() no dbmanage.py
        result = 'Drop table realizado com sucesso.' #result recebe uma mensagem de sucesso
        self.set_result_form(result) #exibe a mensagem na função set_result_for()

    def agendar(self, ip, community, time1, time2):
        Thread(target=self.get_agendado, kwargs={

            'ip': ip,
            'community': community,
            'time1': time1,
            'time2': time2
        }).start()

    def get_agendado(self, ip, community, time1, time2):
        # Variavel para a contagem de tmepo decorrido
        time_delay = int(time1)
        time_final = int(time2)
        tempo_inicial = time.time()

        while True:
            # Executa o primeiro get
            self.get_values_form(ip, community)
            # Pausa no itervalo especificado
            time.sleep(time_delay)
            # se o tempo atual for maior que o tempo esperado o loop sera encerrado
            if time.time() > tempo_inicial + time_final:
                break

        self.set_result_form(self.result)

        tempo = 0 #Contador

        while tempo < tempo_final: #enquanto tempo for menor que o tempo total de agendamento
            cont = time.time() #cont recebe o tempo em segundos desde inicio da execução
            tempo = cont+tempo
            time.sleep(tempo_cont) #realiza o tempo de espera para execução do programa

             #executa o get


            Thread(target= self.get_values_form(ip, community), kwargs={'self': self,
                                                              'ip': ip,
                                                              'community': community,
                                                              'time2': time2
                                                              }).start() #retorna a thread

        self.set_result_form(self.result)



    def build(self):#responsável pela montagem do layout
        Window.size = (1000, 750) #tamanho da janela
        self.load_kv('main.kv') #caminho do arquivo main.kv onde estão as configurações de botão etc.

    def set_result_form(self, resultado): #responsável por mostrar as mensagens na tela
        self.root.ids.textinput_resultado.text = resultado

        print (resultado)



    def get_values_form(self, ip, community): #executa o get.py
        a = SimpleSnmp(ip, community)
        result = a.GetSNMP()
        result = result + '\n IP ' + ip
        result = result + ' e Community ' + community
        self.set_result_form(result)




if __name__ == "__main__":
    SnmpToolApp().run()
