import paho.mqtt.client as mqtt
from smart.models import Device, Channel,ChannelType



def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT with result code "+str(rc))
    for device in Device.objects.all():
        client.subscribe("/"+device.name+"/status")
    for channel in Channel.objects.all():
        client.subscribe("/"+channel.device.name+"/"+channel.name+"/status")

def on_message(client, userdata, msg):
    msg.payload = msg.payload.decode("utf-8")
    print(msg.topic+" ->  "+str(msg.payload))
    device = msg.topic.split("/")[1]
    channel = msg.topic.split("/")[2]
    print(device)



def on_disconnect(client, userdata, rc):
    client.loop_stop(force=True)
    if rc != 0:
        print("Unexpected disconnection.")
    else:
        print("Disconnected")

# client = mqtt.Client()
# client.on_connect = on_connect
# client.on_message = on_message
# client.on_disconnect = on_disconnect
#
# client.connect("192.168.1.200", 1883, 60)