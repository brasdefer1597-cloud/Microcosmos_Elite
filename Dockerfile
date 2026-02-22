FROM python:3.9-slim
WORKDIR /app
RUN pip install --no-cache-dir qiskit qiskit-aer flask
COPY . .
CMD ["python", "shor_15.py"]
