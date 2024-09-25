from influxdb import InfluxDBClient

# InfluxDB setup
client = InfluxDBClient(host='localhost', port=8086)
client.switch_database('financial_data')

def store_in_influxdb(data):
    json_body = [{
        "measurement": "stock_prices",
        "tags": {
            "symbol": data['symbol'],
        },
        "fields": {
            "price": float(data['price'])
        },
        "time": int(data['timestamp']) * 1000000000  # Nanosecond precision
    }]
    client.write_points(json_body)

# Inside the callback of the Pub/Sub consumer
def callback(message):
    data = json.loads(message.data)
    print(f"Received: {data}")
    analyze_stock_data(data)
    store_in_influxdb(data)  # Store data in InfluxDB
    message.ack()
