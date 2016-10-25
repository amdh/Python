from __future__ import print_function

from twisted.internet import reactor
from twisted.web.client import Agent
from twisted.web.http_headers import Headers

agent = Agent(reactor)

d = agent.request(
    'GET',
    'http://example.com/',
    Headers({'User-Agent': ['Twisted Web Client Example']}),
    None)

def cbResponse(contents):
    print('Response received')
    print (contents)
d.addCallback(cbResponse)

def cbShutdown(ignored):
    reactor.stop()
d.addBoth(cbShutdown)

def errorHandler(error):
    print ("error hence stopping")
    reactor.stop()

d.addErrback(errorHandler)

reactor.run()