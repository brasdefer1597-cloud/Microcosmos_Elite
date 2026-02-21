FROM python:3.11-slim
RUN pip install fastapi uvicorn
WORKDIR /app
COPY main.py .
CMD ["uvicorn", "main.py", "--host", "0.0.0.0", "--port", "8000"]
