import paho.mqtt.client as mqtt

import json
from pymongo import MongoClient

def on_message(client, userdata, msg):
    message = json.loads(str(msg.payload.decode("UTF-8")))
    message_type = message.get("type", None)
    if message_type == "healt_update":
        sensors = message.get("data", None)
        mongoClient = MongoClient('mongodb://localhost:27017/')
        db = mongoClient['sfera']
        configdb = db.config
        result = configdb.update_one({'key': 'sfera_healt'}, {'$set': {'value.sensors': sensors}})
        mongoClient.close()
        client.publish('local/system', 'manager:healt_update')


def on_connect(client, userdata, flags, rc):
    client.subscribe("local/manager")

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection."+now)

client = mqtt.Client(client_id="manager")
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect
client.connect("localhost", 1883, 60)

client.loop_forever()
