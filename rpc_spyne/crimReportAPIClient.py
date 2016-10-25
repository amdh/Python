import logging
logging.basicConfig(level=logging.DEBUG)

from spyne import Application, rpc, ServiceBase, \
    Integer, Unicode, Float

from spyne import Iterable

from spyne.protocol.http import HttpRpc
from spyne.protocol.json import JsonDocument

from spyne.server.wsgi import WsgiApplication
import time
import json
import urllib2
import datetime
from time import mktime
import dateutil.parser as dparser

from datetime import date

crime_type_count_dict = {}
event_time_count_dict = {
        "12:01am-3am" : 0,
        "3:01am-6am" : 0,
        "6:01am-9am" : 0,
        "9:01am-12noon" : 0,
        "12:01pm-3pm" : 0,
        "3:01pm-6pm" : 0,
        "6:01pm-9pm" : 0,
        "9:01pm-12midnight" : 0
    }
the_most_dangerous_streets = []
json_output ={
    "total_crime" : 0,
    "the_most_dangerous_streets" : [ ],
    "crime_type_count" : {
        "Assault" : 0
    },
    "event_time_count" : {
        "12:01am-3am" : 0,
        "3:01am-6am" : 0,
        "6:01am-9am" : 0,
        "9:01am-12noon" : 0,
        "12:01pm-3pm" : 0,
        "3:01pm-6pm" : 0,
        "6:01pm-9pm" : 0,
        "9:01pm-12midnight" : 0
    }
}

class CrimeReportService(ServiceBase):

    def checkTimeSlot(self,obj_date):
        time_slot = time.strptime(obj_date, '%I%p')
        print "timeslot: %s" %time_slot
        event_time_count_dict.update()
        datetime.time(0, 12)
        strut_time_ = datetime.datetime.strptime(obj_date, '%m/%d/%y %H:%M %p')
        time_slot = strut_time_.time()
        ts = datetime.datetime.fromtimestamp(mktime(strut_time_.timetuple()))
        if (time_slot in range(datetime.time(12, 0, 1), datetime.time(3, 0, 0), ts)):
            if (event_time_count_dict.has_key("12:01am-3:00am")):
                val = event_time_count_dict.get("12:01am-3:00am")
                val = val + 1
                event_time_count_dict.update({"12:01am-3:00am": val})
            else:
                event_time_count_dict.update({"12:01am-3:00am": 1})
        elif (time_slot in range(datetime.time(3, 0, 1), datetime.time(6, 0, 0), ts)):
            if (event_time_count_dict.has_key("03:01am-6:00am")):
                val = event_time_count_dict.get("03:01am-6:00am")
                val = val + 1
                event_time_count_dict.update({"03:01am-6:00am": val})
            else:
                event_time_count_dict.update({"03:01am-6:00am": 1})
        elif (time_slot in range(datetime.time(6, 0, 1), datetime.time(9, 0, 0), ts)):
            if (event_time_count_dict.has_key("12:01am-3:00am")):
                val = event_time_count_dict.get("12:01am-3:00am")
                val = val + 1
                event_time_count_dict.update({"12:01am-3:00am": val})
            else:
                event_time_count_dict.update({"12:01am-3:00am": 1})
        elif (time_slot in range(datetime.time(18, 0, 1), datetime.time(21, 0, 0), ts)):
            if (event_time_count_dict.has_key("6:01pm-9:00pm")):
                val = event_time_count_dict.get("6:01pm-9:00pm")
                val = val + 1
                event_time_count_dict.update({"6:01pm-9:00pm": val})
            else:
                event_time_count_dict.update({"6:01pm-9:00pm": 1})

    @rpc(Float, Float, Float, _returns=Iterable(Unicode))
    def checkcrime(self, lat, lon, radius):
        ret_response = {}
        base_url = "https://api.spotcrime.com/crimes.json"
        get_url = "%s?lat=%s&lon=%s&radius=%s&key=." % (base_url, lat, lon, radius)
        print get_url
        json_data = json.load(urllib2.urlopen(get_url))
        print  len(json_data['crimes'])
        #if( len(json_data['crimes']) <= 3):
        for obj in json_data['crimes']:
            if(obj['address'].find('&')):
                addr_str = obj['address'].split('&')
                json_output["the_most_dangerous_streets"].append(addr_str)
            else:
                json_output["the_most_dangerous_streets"].append(obj['address'])
            if(json_output["crime_type_count"].has_key(obj['type'])):
                val = json_output["crime_type_count"].get(obj['type'])
                val = val +1;
                json_output["crime_type_count"].update({obj['type']:val})
            else:
                json_output["crime_type_count"].update({obj['type']: 0})

                #self.checkTimeSlot(obj['date'])
            obj_date = dparser.parse(obj['date'])
            obj_date.strftime('%m/%d/%y %H:%M:%S')
            print " object date time :%s"%obj_date.time()
            strut_time_ = datetime.datetime.strptime(obj['date'], '%m/%d/%y %H:%M %p' )
            time_slot = strut_time_.time()
            #datetime.time(0, 12)
            ts = datetime.datetime.fromtimestamp(mktime(strut_time_.timetuple()))
            print "timeslot: %s" %  time_slot
            print datetime.time(13,5)
            self.settimeslot(obj['date'])
            if( time_slot >= datetime.time(6,1) and time_slot < datetime.time(9,0)):
                    json_output["event_time_count"]["6:01pm-9pm"] = 1

        #else:
        #    print " more than 3 records found"

        ret_response.update({"event_time_count" :event_time_count_dict})
        ret_response.update({"crime_type_count" :crime_type_count_dict})
        ret_response.update({"the_most_dangerous_streets" : the_most_dangerous_streets})

        #res = Response(json.dumps(json_output), status=200)
        #return res
        return json.dumps(json_output)

    def settimeslot(self,obj_date):
        print "into set time slot"




application = Application([CrimeReportService],
    tns='spyne.examples.crimereport',
    in_protocol=HttpRpc(validator='soft'),
    out_protocol=JsonDocument()
)

if __name__ == '__main__':
    # You can use any Wsgi server. Here, we chose
    # Python's built-in wsgi server but you're not
    # supposed to use it in production.
    from wsgiref.simple_server import make_server

    wsgi_app = WsgiApplication(application)
    server = make_server('127.0.0.1', 8000, wsgi_app)
    server.serve_forever()