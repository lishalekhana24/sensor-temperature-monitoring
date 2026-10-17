
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "sensor-readings-lisha",
    bootstrap_servers="localhost:9092",
    group_id="sensor-group-lisha",
    auto_offset_reset="latest",
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    consumer_timeout_ms=30000
)

normal = 0
high = 0
invalid = 0
total = 0

print("\n--- SENSOR READINGS ---")

try:
    for message in consumer:
        reading = message.value
        sensor_id = reading.get("sensor_id", "Unknown")

        try:
            temperature = float(reading["temperature"])

            if temperature < 35:
                print(f"{sensor_id} | {temperature} C | NORMAL | P{message.partition}")
                normal += 1
            else:
                print(f"{sensor_id} | {temperature} C | HIGH | P{message.partition}")
                high += 1

        except (KeyError, ValueError, TypeError):
            print(f"{sensor_id} | INVALID | P{message.partition}")
            invalid += 1

        total += 1

except KeyboardInterrupt:
    print("\nConsumer stopped.")

finally:
    consumer.close()

print("\n--- SUMMARY ---")
print(f"NORMAL: {normal} | HIGH: {high} | INVALID: {invalid}")
print(f"TOTAL: {total}")

