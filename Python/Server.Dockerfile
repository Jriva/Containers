FROM python:3
WORKDIR /app
COPY server.py .
CMD ["python3", "server.py"]