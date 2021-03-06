#!python3
import paho.mqtt.client as mqtt #import the client1
import time
#time imported to be able to put in delays
def on_log(client, userdata, level, buf):
        print("log:  "+buf)
def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("Connected OK")
    else:
        print("Bad connection Returned code=",rc)
def on_disconnect(client, userdata, flags, rc=0):
        print(Disconnected result code " +str(rc))
#Start Add on_message callback part one  IMPORTANT line 17 is not complete            
def on_message(client, userdata, msg):
        topic=msg.topic
        m_decode=str(msg.payload.decode("utf-8", "ignore")
        print("message received", m_decode)                                
#End Add message callback part one IMPORTANT Line 17 is not complete              
#broker="test.mosquitto.org"
#broker="broker.heivemq.com"
#broker="iot.eclipse.org"

broker="192.168.1.206"
#ATTENTION IP address
#There is a publically accessible sandbox server for the Eclipse IoT projects available at iot.eclipse.org, port 1883
#https://eclipse.org/paho/
#iot.eclipse.org > 198.41.30.241

client = mqtt.Client("python1")  #create new instance
client.on_connect=on_connect #blind call back function
client.on_disconnect=on_disconnect            
client.on_log=on_log
#Start add on_message callback part two                     
client.on_message=on_message
#End add on message callback part two                     
print("Connecting to broker ", broker)
client.connect(broker) #connect to broker
client.loop_start() #Start loop
client.subscribe("house/sensor1")
client.publish("house/sensor1","my first message")           
time.sleep(4)
client.loop_stop() #Stop loop
client.disconnect() #disconnect
