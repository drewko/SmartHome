import paho.mqtt.client as mqtt
from smart.models import Device, Channel, ChannelType
import time


def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT with result code " + str(rc))
    for device in Device.objects.all():
        client.subscribe("/" + device.name + "/status")
        client.subscribe('/' + device.name + '/request')
    for channel in Channel.objects.all():
        client.subscribe("/" + channel.device.name + "/" + channel.name + "/status")


def on_message(client, userdata, msg):
    msg.payload = msg.payload.decode("utf-8")
    print(msg.topic + " ->  " + str(msg.payload))
    if 'request' not in msg.topic:
        device = msg.topic.split("/")[1]
        channel = msg.topic.split("/")[2]
        object = Channel.objects.get(device__name=device, name=channel)
        object.status = msg.payload
        object.save()
    else:
        device = msg.topic.split('/')[1]
        channel = msg.payload
        object = Channel.objects.get(device__name=device, name=channel)
        client.publish('/'+device+'/'+channel,object.status)






def on_disconnect(client, userdata, rc):
    client.loop_stop(force=True)
    if rc != 0:
        print("Unexpected disconnection.")
    else:
        print("Disconnected")



client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect
client.connect("192.168.1.118", 1883, 60)

for channel in Channel.objects.all():
    client.subscribe('/'+channel.device.name+'/'+channel.name+'/status')



