import constants
import xmlrpc.client

server = xmlrpc.client.ServerProxy(
    "http://localhost:{}".format(constants.PORT_NUMBER))
print("Available methods:")
print(server.system.listMethods())

print("\nComplexities for various words:")
words = [
    "the",
    "thence",
    "provided",
    "parodying",
    "are",
    "animosity",
]
for word in words:
    print("{}\t\t{}".format(word, server.predict(word)))
