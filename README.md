Project Overview:
Goal: Build a real-time data pipeline that can:
Ingest financial data streams.
Process the streams in real-time.
Analyze the data and display results on a dashboard.
Alert based on specific conditions (e.g., stock price thresholds).
Tech Stack:
Data Ingestion: Apache Kafka, AWS Kinesis, or Google Pub/Sub.
Stream Processing: Apache Flink or Python-based consumers.
Data Analysis: Python (Pandas, NumPy).
Orchestration: Kubernetes.
Visualization: Grafana (for dashboards).
Step-by-Step Implementation:
Ingest Data: Use Apache Kafka or Google Pub/Sub to ingest financial data in real time.
Process Data: Use Apache Flink or a simple Python consumer to process and analyze the streams.
Visualize Data: Integrate Grafana for real-time visualization.
Alerting: Use Python to trigger alerts based on real-time analysis.
