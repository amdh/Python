from twisted.web.client import getPage

from twisted.internet import reactor

def lowerCaseContents(contents):
    '''
    This is a 'callback' function, added to the Deferred and called by
    it when the promised data is available. It converts all the data to
    lower case
    '''
    print ("data received in lower case")
    return contents.lower()

def printContents(contents):
    '''
    This a 'callback' function, added to the Deferred after lowerCaseContents
    and called by it with the results of lowerCaseContents
    '''
    print ("data received")
    print contents
    reactor.stop()

deferred = getPage('http://twistedmatrix.com/documents/8.2.0/core/howto/async.html')

# add two callbacks to the deferred -- request that it run lowerCaseContents
# when the page content has been downloaded, and then run printContents with
# the result of lowerCaseContents
deferred.addCallback(lowerCaseContents)
deferred.addCallback(printContents)

reactor.run()