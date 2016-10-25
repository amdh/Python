from twisted.web.client import getPage

from twisted.internet import reactor

def errorHandler(error):
    '''
    This is an 'errback' function, added to the Deferred which will call
    it in the event of an error
    '''

    # this isn't a very effective handling of the error, we just print it out:
    print "An error has occurred: <%s>" % str(error)
    # and then we stop the entire process:
    reactor.stop()

def printContents(contents):
    '''
    This a 'callback' function, added to the Deferred and called by it with
    the page content
    '''

    print contents
    reactor.stop()

# We request a page which doesn't exist in order to demonstrate the
# error chain
deferred = getPage('http://twistedmatrix.com/does-not-exist')

# add the callback to the Deferred to handle the page content
deferred.addCallback(printContents)

# add the errback to the Deferred to handle any errors
deferred.addErrback(errorHandler)

reactor.run()