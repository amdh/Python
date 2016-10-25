import json
from flask import Flask
test= {
    "titile" : "streets",
    "street1" :
        [
            {
                "type":"shoot",
                "date":"2/4/16"
            },
            {
                "type":"robbary",
                "date":"4/4/16"
            }
        ],
    "pruneridge eve santa clara" :
        [
            {
                "type":"murder",
                "date":"2/4/16"
            },
            {
                "type":"loot",
                "date":"4/4/16"
            }
        ],
    "101 E street 2" :
        [{
                "type":"kill",
                "date":"2/4/16"
        }
    ]

}
app = Flask(__name__)

@app.route("/")
def getNestedJson():
    print test["titile"]
    print test["street1"][0]["type"]
    for k in test["street1"]:
        print k["type"]
        print k["date"]
    print test.has_key("street1")
    print test.has_key("101 E street 2")
    test["101 E street 2"].append({"type ": "alarm"})
    return test


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')