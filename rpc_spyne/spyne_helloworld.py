from spyne.application import Application
from spyne.decorator import srpc
from spyne.service import ServiceBase
from spyne.model.complex import Iterable
from spyne.model.primitive import Integer
from spyne.model.primitive import String
from spyne.server.wsgi import WsgiApplication
from spyne.protocol.http import HttpRpc
from spyne.protocol.json import JsonDocument
import logging

class HelloWorldService(ServiceBase):
    @srpc(String, Integer, _returns=Iterable(String))

    def say_hello(name, times):
        for i in xrange(times):
            yield "hello, %s"%name
        

if __name__ == '__main__':
         # Python daemon boilerplate
    from wsgiref.simple_server import make_server
            
    logging.basicConfig(level=logging.DEBUG)        
    application = Application([HelloWorldService], 'spyne.examples.hello.http',
                                      in_protocol=HttpRpc(), out_protocol=JsonDocument())
    
    wsgi_application = WsgiApplication(application)

        # More daemon boilerplate
    server = make_server('127.0.0.1', 8000, wsgi_application)

    logging.info("listening to http://127.0.0.1:8000")
    logging.info("wsdl is at: http://localhost:8000/?wsdl")

    server.serve_forever()    

