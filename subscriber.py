import paho.mqtt.client as mqtt
import serial

# Replace with your correct COM port
ser = serial.Serial('COM5', 9600)

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("light/control")

def on_message(client, userdata, msg):
    command = msg.payload.decode().strip()
    print(f"Received: {command}")
    
    if command in ["ON", "OFF"]:
        ser.write((command + '\n').encode())

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

print("Connecting to MQTT broker...")
client.connect("localhost", 1883)

client.loop_forever()
