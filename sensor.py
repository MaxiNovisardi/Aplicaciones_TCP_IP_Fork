import json
import time
import paho.mqtt.client as mqtt

# Configuración del broker MQTT
broker = "localhost"  # o la IP donde esté EMQX (cambiá si no es localhost)
port = 1883

# Datos de prueba para cada tópico
datos_sonoff = {
    "ENERGY": {
        "Voltage": 230,
        "Current": 0.3,
        "Power": 70
    }
}

datos_dht11 = {
    "DHT11": {
        "Temperature": 25.0,
        "Humidity": 60
    }
}

datos_raspy = {
    "RASPY": {
        "CPU_temp": 55.0,
        "RAM_usage": 512
    }
}

# Crear cliente y conectar para cada usuario
def publicar_datos(topic, payload, username, password):
    client = mqtt.Client()
    client.username_pw_set(username, password)
    client.connect(broker, port)
    client.loop_start()
    client.publish(topic, json.dumps(payload), qos=2)
    client.loop_stop()
    client.disconnect()

# Publicar en los tres tópicos
while True:
    publicar_datos("sensor/sonoff/data", datos_sonoff, "sonoff", "labiot2024")
    publicar_datos("sensor/dht11/data", datos_dht11, "dht11", "sebacrack")
    publicar_datos("sensor/raspy/data", datos_raspy, "raspy", "tcpip2024")
    print("Mensajes publicados")
    time.sleep(1)  # Cada 10 segundos