from predictor import WordComplexityPredictor
from xmlrpc.server import SimpleXMLRPCRequestHandler, SimpleXMLRPCServer

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

server = SimpleXMLRPCServer(("localhost", constants.PORT_NUMBER),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

server.register_instance(WordComplexityPredictor(debug=True))
server.serve_forever()
