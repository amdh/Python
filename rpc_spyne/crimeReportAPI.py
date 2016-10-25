from suds.client import Client
import requests
import json
#hello_client = Client('http://localhost:7789/?wsdl')
#print hello_client.service.say_hello("Dave", 5)
hello_client = Client('http://127.0.0.1:8000/?')
print hello_client.service.checkcrime(37.33,121.88,0.02)

#https://api.spotcrime.com/crimes.json?lat=37.334164&lon=-121.884301&radius=0.02&key=.

base_url = "https://api.spotcrime.com/crimes.json"
get_url = "%s?lat=%s&lon=%s&radius=%s&key=." % (base_url, lan, lon, rad)
get_response = requests.get(get_url)
json_response = json.loads(get_response.content)
if get_response.status_code == 200:
    user_log['get_returns_200'] = points['get_returns_200']
    for key in object_to_post.keys():
        if key not in json_response.keys():
            print "Key %s not found in response " % key
            user_log['get_returns_all_keys_and_values'] = 0
            submit_to_lambda()
            exit(1)
    user_log['get_returns_all_keys_and_values'] = points['get_returns_all_keys_and_values']
    user_log['get_response'] = json_response
else:
    user_log['get_returns_200'] = 0
    print "Get did not return 200 as expected."
    submit_to_lambda()
    exit(1)

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
import requests
from datetime import date

crime_type_count_dict = {}

event_time_count_dict = {
    "12:01am-3am": 0,
    "3:01am-6am": 0,
    "6:01am-9am": 0,
    "9:01am-12noon": 0,
    "12:01pm-3pm": 0,
    "3:01pm-6pm": 0,
    "6:01pm-9pm": 0,
    "9:01pm-12midnight": 0
}
the_most_dangerous_streets = []

json_output = {
    "total_crime": 0,
    "the_most_dangerous_streets": [],
    "crime_type_count": {
        "Assault": 0
    },
    "event_time_count": {
        "12:01am-3am": 0,
        "3:01am-6am": 0,
        "6:01am-9am": 0,
        "9:01am-12noon": 0,
        "12:01pm-3pm": 0,
        "3:01pm-6pm": 0,
        "6:01pm-9pm": 0,
        "9:01pm-12midnight": 0
    }
}


class CrimeReportService(ServiceBase):
    @rpc(Float, Float, Float, _returns=Unicode)
    def checkcrime(self, lat, lon, radius):
        ret_response = {}
        base_url = "https://api.spotcrime.com/crimes.json"
        get_url = "%s?lat=%s&lon=%s&radius=%s&key=." % (base_url, lat, lon, radius)
        print get_url
        # json_data = json.loads(urllib2.urlopen(get_url))

        get_response = requests.get(get_url)
        json_data = json.loads(get_response.content)
        if get_response.status_code == 200:
            print  len(json_data['crimes'])
            print  json_data.get("crimes")
        # if( len(json_data['crimes']) <= 3):
        for obj in json_data['crimes']:
            if (obj['address'].find(" & ") != -1):
                addr_str = obj['address'].split(' & ')
                print addr_str
                json_output["the_most_dangerous_streets"].append(addr_str[0])
                json_output["the_most_dangerous_streets"].append(addr_str[1])
            else:
                json_output["the_most_dangerous_streets"].append(obj['address'])
                crime_type_count_dict.update({obj['address']: 1})
            if (json_output["crime_type_count"].has_key(obj['type'])):
                val = json_output["crime_type_count"].get(obj['type'])
                val = val + 1;
                json_output["crime_type_count"].update({obj['type']: val})
            else:
                json_output["crime_type_count"].update({obj['type']: 1})

                # self.checkTimeSlot(obj['date'])
            obj_date = dparser.parse(obj['date'])
            obj_date.strftime('%m/%d/%y %H:%M:%S')
            print " object date time :%s" % obj_date.time()
            time_slot = obj_date.time()

            # self.settimeslot(obj['date'])
            if (time_slot >= datetime.time(0, 1) and time_slot <= datetime.time(3, 0)):
                val = json_output["event_time_count"].get("12:01am-3am")
                val = val + 1
                json_output["event_time_count"]["12:01am-3am"] = val
            if (time_slot >= datetime.time(3, 1) and time_slot <= datetime.time(6, 0)):
                val = json_output["event_time_count"].get("3:01am-6am")
                val = val + 1
                json_output["event_time_count"]["3:01am-6am"] = val
            if (time_slot >= datetime.time(6, 1) and time_slot <= datetime.time(9, 0)):
                val = json_output["event_time_count"].get("6:01am-9am")
                val = val + 1
                json_output["event_time_count"]["6:01am-9am"] = val
            if (time_slot >= datetime.time(9, 1) and time_slot <= datetime.time(12, 0)):
                val = json_output["event_time_count"].get("9:01am-12noon")
                val = val + 1
                json_output["event_time_count"]["9:01am-12noon"] = val
            if (time_slot >= datetime.time(12, 1) and time_slot <= datetime.time(15, 0)):
                val = json_output["event_time_count"].get("12:01pm-3pm")
                val = val + 1
                json_output["event_time_count"]["12:01pm-3pm"] = val
            if (time_slot >= datetime.time(15, 1) and time_slot <= datetime.time(18, 0)):
                val = json_output["event_time_count"].get("3:01pm-6pm")
                val = val + 1
                json_output["event_time_count"]["3:01pm-6pm"] = val
            if (time_slot >= datetime.time(18, 1) and time_slot <= datetime.time(21, 0)):
                val = json_output["event_time_count"].get("6:01pm-9pm")
                val = val + 1
                json_output["event_time_count"]["6:01pm-9pm"] = val
            if (time_slot >= datetime.time(21, 1) and time_slot <= datetime.time(23, 0)):
                val = json_output["event_time_count"].get("9:01pm-12midnight")
                val = val + 1
                json_output["event_time_count"]["9:01pm-12midnight"] = val

        # else:
        #    print " more than 3 records found"

        ret_response.update({"event_time_count": event_time_count_dict})
        ret_response.update({"crime_type_count": crime_type_count_dict})
        ret_response.update({"the_most_dangerous_streets": the_most_dangerous_streets})

        total_crime = json_output["event_time_count"]["12:01am-3am"] + json_output["event_time_count"]["3:01am-6am"] + \
                      json_output["event_time_count"]["6:01am-9am"] + json_output["event_time_count"]["9:01am-12noon"] + \
                      json_output["event_time_count"]['12:01pm-3pm'] + json_output["event_time_count"]["3:01pm-6pm"] + \
                      json_output["event_time_count"]['6:01pm-9pm'] + json_output["event_time_count"][
                          "9:01pm-12midnight"]
        json_output['total_crime'] = total_crime

        print crime_type_count_dict
        # res = Response(json.dumps(json_output), status=200)
        # return res
        return json.dumps(json_output)

    def settimeslot(self, obj_date):
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

