# Projeto-Final
Programa de gerenciamento de rede atraves do protocolo SNMP

AUTOR: Míriam Félix Lemes da Silva
CONTATO: miriamfx2@gmail.com


RESUMO

	O programa utiliza o protocolo SNMP para pegar informacoes em determinado intervalo de tempos de Hosts na rede.
	Estas informacoes sao armazenadas em um banco de dados utilizando sqlite.
	Baseado no protocolo SNMP, foi desenvolvida uma aplicação capaz de enviar uma mensagem “GET” a um determinado dispositivo, 		recebendo como parâmetro o IP e a comunidade do objeto da rede a ser gerenciado e retornando os valores na sequência em que 		serão solicitados. Para tanto, serão utilizadas a linguagem de programação Python e suas bibliotecas Pysnmp e Kivy.

REQUISITOS 

	A aplicação  desenvolvida utilizando o sistema operacional Ubuntu 16.04.1, a maioria das distribuições linux já vem com Python  instalado, mas a versão nem sempre é atualizada, para instalar a versão mais atualizada do Python foi utilizado o pyenv. Para que nossa aplicação também utilizamos a biblioteca PySNMP que facilitou muito o desenvolvimento da aplicação. Necessário também ter ativo tanto no gerente quanto no agende o serviço SNMP.

CONFIGURAÇÕES NECESSÁRIAS NO AGENTE

	O SNMP deve estar ativo no agente. Após ativado o serviço SNMP configure a comunidade em que irá executar o gerente. Para configurar  o agente no Windows deve-se ir em serviços, e ativar o serviço SNMP, em seguida em propriedades do serviço configurar a comunidade em que o agente esta, para podermos realizar a leitura. Lembrando que o gerente não precisa estar na mesma comunidade, e pode gerenciar comunidades distintas ao mesmo tempo, mas precisa receber o dados da comunidade como parâmetro para execução e envio das mensagens. 


	A configuração no agente Linux, foi realizado no Ubuntu, a ativação do SNMP no Linux vale tanto para o agente como para o gerente, se o serviço não estiver ativo no servidor não realizará o envio das mensagens. No Linux instale o serviço SNMP através do comando, # apt-get install snmpd, apague o conteúdo do arquivo de configuração do serviço através do comando, # echo > /etc/snmp/snmpd.conf, edite o arquivo de configuração snmpd.conf utilizando o vi, # vi /etc/snmp/snmpd.conf.
	Segue abaixo um arquivo "snmpd.conf" totalmente funcional: 
	rocommunity rede123
	syslocation projeto_final
	sysContact projeto_final <projeto.final@gmail.com>
	Em nosso exemplo, foi utilizado o nome de comunidade rede123, a localização projeto_final e a pessoa de contato projeto_final.
	Reinicie o serviço SNMP através do comando abaixo: 
	# /etc/init.d/snmpd restart
	Instale e execute o utilitário rcconf, marque para que o serviço SNMP seja iniciado automaticamente durante o boot: 
	# apt-get install rcconf
	# rcconf
	O serviço SNMP foi instalado em seu sistema com sucesso.




MODULOS DO PROGRAMA
>main.py

     >SnmpToolApp: responsavel pelos botões de ação, encaminha os atributos de entrada para o manager
    btn1 = cadastro
    btn2 = consulta (get)
    btn3 = agendar
    btn4 = gerar relatorio
    btn5 = limpar
    btn6 = sair

    >ponto de entrada
        ip
        comunidade
        tempo

    se entrada recebe 1 = btn1, 2 = btn2, 3 = btn3, 4 = btn4, 5 = btn5, 6 = btn6

>main.kv
      formata a parte grafica, funciona como uma pagina de estilos.

> manager.py
	  esse modulo é o responsavel por delegar as funções aos outros modulos
	  ele recebe os atributos de entrada do main.py que são as chaves para executar os demais modulos e gerencia qual modulo deve
	  ser executado.
	  para isso existem funções dentro de uma classe gerente, que executam com um repetidor while, e são executados a partir da condição


> get.py
	  Programa que recolhe as informacoes dos hosts.
	  Para chamar diretamente, deve ser passado por parametro o IP e a COMUNIDADE. Para obter estas informacoes, executar o >dbquery.py

 > GetSNMP1: recebe informações da MIB system
    1.3.6.1.2.1.1.1 - sysDescr
    1.3.6.1.2.1.1.2 - sysObjectID
    1.3.6.1.2.1.1.3 - sysUpTime
    1.3.6.1.2.1.1.4 - sysContact
    1.3.6.1.2.1.1.6 - sysLocation

 >GetSNMP2: recebe informaçoes da MIB HOST-RESOURCES-MIB
    1.3.6.1.2.1.25.5.1.1.1 - hrSWRunPerfCPU
    "O número de centésimos-segundos da CPU do sistema total
    Recursos consumidos por este processo. Note que em um
    Sistema multi-processador, este valor pode
    Mais de um centi-segundo em um centi-segundo de real
    (Relógio de parede).

    1.3.6.1.2.1.25.5.1.1.2 - hrSWRunPerfMem'
    A quantidade total de memória do sistema real alocada para este processo.

 >GetSNMP3:


     1.3.6.1.2.1.4.4 -  ipInHdrErrors
     O número de datagramas de entrada descartados devido a
     Erros em seus cabeçalhos IP, incluindo
     Checksums, número de versão incompatível, outro formato
     Erros, tempo de vida excedido, erros descobertos
     No processamento de suas opções de IP, etc.


> dbmanager.py
	  Gerencia todas os cadastros, modificacoes e consultas no banco de dados.

	  variaveis: cursor: é um interador que permite navegar e manipular os registros do bd.
                 execute: lê e executa comandos SQL puro diretamente no bd.
                 close: método desconecta do banco.c.close/con.close
                 commit: É ele que grava de fato as alterações na tabela.
                 Lembrando que uma tabela é alterada com as instruções SQL ``INSERT, UPDATE`` e ``DELETE``.

      Funções:
      def del_hosts_db(db, hosts_list):
        Exclui hosts do Banco de Dados na tabela Hosts.
        O Banco de Dados utilizando e o definido no settings.py.
        hosts_list contem uma lista de tuplas com ips e nomes de host no formato [(ip, nomedohost),
        (ip, nomedohost), ...]. Pode ser passado uma lista, mas na chamada interna do programa manager
        e passado uma lista com uma tupla apenas.

      def create_tables_db(db):
         Inicia a criacao das tabelas no Banco de Dados

      def drop_tables_db(db):
        Exclui as tabelas do Banco de Dados.
        O Banco de Dados utilizando e o definido no settings.py.
	
      def reg_hosts_db(db, hosts_list):
        Insere informacoes no Banco de Dados na tabela Hosts.
        O Banco de Dados utilizando e o definido no settings.py.
        hosts_list contem uma lista de tuplas com ips e nomes de host no formato [(ip, nomedohost), (ip, nomedohost), ...]

      def del_hosts_db(db, hosts_list):
        Exclui hosts do Banco de Dados na tabela Hosts.
        O Banco de Dados utilizando e o definido no settings.py.
        hosts_list contem uma lista de tuplas com ips e nomes de host no formato [(ip, nomedohost),
        (ip, nomedohost), ...]. Pode ser passado uma lista, mas na chamada interna do programa manager e passado
        uma lista com uma tupla apenas.



> logs.py
	  Grava em arquivos de logs as operacoes dos programas.


	  
	  
	  
