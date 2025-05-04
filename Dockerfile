FROM python:3.11-slim
LABEL authors="kautz"

# Set the timezone to UTC
# Download the latest installer
WORKDIR /app

COPY ./src /app/src

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/app/src
EXPOSE 8000
CMD ["uvicorn", "tasy_o.api.app:fastapi_app", "--host", "0.0.0.0", "--port", "8088"]

