# Sensor Temperature Monitoring

## About the Project

This project uses Apache Kafka and Python to monitor temperature readings from factory sensors. The producer sends sensor data to Kafka, and the consumer reads the data and classifies each temperature.

## Technologies Used

- Python
- Apache Kafka
- kafka-python
- JSON

## How It Works

- Temperatures below 35°C are classified as NORMAL.
- Temperatures of 35°C or above are classified as HIGH.
- Missing or invalid temperatures are displayed as INVALID.
- The consumer displays the counts of normal, high, and invalid readings.

The Kafka topic is `sensor-readings-lisha`, with two partitions. Both consumers use the same consumer group, `sensor-group-lisha`.

## How to Run

Start the Kafka container:

```bash
docker start delivery-kafka
```

Activate the virtual environment:

```bash
cd ~/sensor-temperature-monitoring
source venv/bin/activate
```

Run the consumer:

```bash
python consumer.py
```

Run the producer in another terminal:

```bash
cd ~/sensor-temperature-monitoring
source venv/bin/activate
python producer.py
```

To test two consumers, run `consumer.py` in two separate terminals before starting the producer.

## Files

- `producer.py` – Sends sensor readings to Kafka.
- `consumer.py` – Reads and classifies sensor readings.
- `assessment 3 Sensor Temperature Monitoring.docx` – Project report.
