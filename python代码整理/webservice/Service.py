import soaplib
from soaplib.core.service import rpc, DefinitionBase, soap
from soaplib.core.model.primitive import String, Integer,Any
from soaplib.core.server import wsgi
from soaplib.core.model.clazz import Array



class HelloWorldService(DefinitionBase):
    @soap(String, Integer, _returns=Array(String))
    def say_hello(self, name, times):
        results = []
        for i in range(0, times):
            results.append('Hello, %s' % name)
        return results

    @soap(String, _returns=Array(String))
    def helloWorld(self,hello):
        print hello
        return hello





if __name__ == '__main__':
    try:
        from wsgiref.simple_server import make_server

        soap_application = soaplib.core.Application([HelloWorldService], 'tns')
        wsgi_application = wsgi.Application(soap_application)
        server = make_server('localhost', 8080, wsgi_application)
        print 'soap server starting......'
        server.serve_forever()
    except ImportError:
        print "Error: example server code requires Python >= 2.5"