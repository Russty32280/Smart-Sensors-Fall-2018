import paho.mqtt.publish as publish

MQTT_SERVER = "m14.cloudmqtt.com:19969"
MQTT_PATH = "test_channel"

publish.single(MQTT_PATH, "HELLO, WORLD!", hostname=MQTT_SERVER)
