import os
# Porta padrao do protocolo SNMP. Padrao 161
DEFAULT_PORT = 161

# Comunidade utilizada no SNMP. Padrao public
DEFAULT_COMMUNITY = 'public'

# Campo padrao para localizacao de Hosts com SNMP ativo.
DEFAULT_FIELD = 'sysName'

# Versao do protocolo SNMP. Padrao SNMPv2-MIB
SNMP_VERSION = 'SNMPv2-MIB'

# Caminho do banco de dados.
DB = os.path.abspath(os.path.dirname('snmpdb.db'))

# Caminho do diretorio de logs local.
LOG_FOLDER = os.path.join(os.getcwd(), '/logs')

#Caminho arquivo CSV
CSV = os.path.join(os.getcwd(), '/rel')
