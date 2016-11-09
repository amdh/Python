from __future__ import print_function

from twisted.internet import reactor
from twisted.web.client import Agent
from twisted.web.http_headers import Headers
import time
import datetime
from  dateutil import tz
import dateutil.parser as dparser
import pytz

agent = Agent(reactor)
now_time = datetime.datetime.now()
d = agent.request(
    'GET',
    'http://twistedmatrix.com/documents/8.2.0/core/howto/async.html',
    Headers({'User-Agent': ['Twisted Web Client Example'],'content-type' : [ 'text/html'], 'date' :[ '%s' %now_time]}),
    None)


start_time = int(round(time.time() * 1000))
print (start_time)


def millis():
   dt = datetime.datetime.now() - start_time
   ms = (dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0
   return ms


def cbResponse(contents):
    end_time = int(round(time.time() * 1000))
    print(end_time)
    print (datetime.datetime.now())
    print("total time taken in sec:%d" % (end_time - start_time))
    print (contents.code)
    print('Response received')
    Headers = contents.headers
    print(Headers)
    for k,v in Headers.getAllRawHeaders():
        print (k)
        if( k == "Date"):
            req_time = v[0]
            print (req_time)
            break

    utc_zone = tz.gettz('UTC')
    gmt_zone = tz.gettz('GMT')
    obj_date = dparser.parse(req_time)
    print ("return time :%s"% obj_date.time())
    gmt_now_time = now_time +  datetime.timedelta(hours=7)
    print ("request time: %s" %gmt_now_time.time())
    end = int(round(obj_date.time().second))
    start = int(round(gmt_now_time.time().second))
    print (" difference between the two : %d "% (end - start))
    #obj_date = obj_date.astimezone(pytz._UTC())
    #print (obj_date)
    #obj_date.replace(tzinfo=utc_zone) + obj_date.utcoffset()
    #obj_date.strftime('%a, %d %b %Y %H:%M:%S GMT')
    #print (" object date time :%s" % obj_date.time())

    #hour = obj_date.time().hour - datetime.time(7,0,0).hour
    #new_ret_time = datetime.time(hour,obj_date.time().minute,obj_date.time().second)
    #print (new_ret_time)






d.addCallback(cbResponse)

def cbShutdown(ignored):
    reactor.stop()
d.addBoth(cbShutdown)


def errorHandler(error):
    print ("error hence stopping")
    reactor.stop()
d.addErrback(errorHandler)

reactor.run()