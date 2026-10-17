
from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda x: json.dumps(x).encode("utf-8")
)

readings = [
    {"sensor_id": "S101", "location": "Line-A", "temperature": 31.2},
    {"sensor_id": "S102", "location": "Line-B", "temperature": 38.5},
    {"sensor_id": "S103", "location": "Line-A", "temperature": 34.0},
    {"sensor_id": "S104", "location": "Line-C", "temperature": 42.0},
    {"sensor_id": "S105", "location": "Line-B", "temperature": 29.5},
    {"sensor_id": "S106", "location": "Line-A", "temperature": 36.0},
    {"sensor_id": "S107", "location": "Line-C", "temperature": 33.5},
    {"sensor_id": "S108", "location": "Line-B", "temperature": 40.0},
    {"sensor_id": "S109", "location": "Line-A", "temperature": 27.8},
    {"sensor_id": "S110", "location": "Line-C", "temperature": 35.0},
    {"sensor_id": "S111", "location": "Line-A", "temperature": "abc"},
    {'sensor_id': 'S112', 'location': 'Line-D', 'temperature': 'lisha'}

]

for reading in readings:
    producer.send("sensor-readings-lisha", reading)
    print("Sent:", reading)

producer.flush()
producer.close()

print("All messages sent successfully!")

