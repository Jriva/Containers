FROM python:3
WORKDIR /app
COPY client.py .
CMD ["python3", "client.py"]