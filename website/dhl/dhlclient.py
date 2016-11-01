from ZSI import *
from zeep import Client
from socket import *
import logging
from SOAPpy import SOAPProxy
import urllib2
import xml

class DhlClient():
    WSDL = 'https://dhl24.com.pl/webapi'
    namespace = 'https://dhl24.com.pl/webapi/provider/service.html?ws=1'
    client = Client(WSDL)
    msg = client.service.getVersion()
    print 'Version: ' + msg
    logging.basicConfig(filename='dhlclient.log', level=logging.DEBUG)
    def call(self):
        try:
            a = socket.connect(self.WSDL)
            print a
        except Exception as e:
            logging.debug(str(e))
        try:
            a2 = socket.bind(self.WSDL)
            print a2
        except Exception as e:
            logging.debug(str(e))
        try:
            a3 = socket.connect_ex(self.WSDL)
            print a3
        except Exception as e:
            logging.debug(str(e))

    def establish(self):
        msg = ''
        # x = urllib2.urlopen('https://dhl24.com.pl/webapi/provider/service.html?ws=1"')
        # print xml.load(x)
        try:
            client = Client(self.WSDL)
            msg = client.service.getVersion()
            # server = SOAPProxy(self.WSDL,self.namespace)
            # msg = server.getVersion()
            print msg
            logging.info(str(msg))

        except Exception as e:
            logging.info(str(e))
            return str(msg)
        return msg