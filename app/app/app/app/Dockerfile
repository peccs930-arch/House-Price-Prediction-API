# -----------------------------
# Base Image
# -----------------------------
FROM python:3.11-slim

# -----------------------------
# Set Working Directory
# -----------------------------
WORKDIR /app

# -----------------------------
# Copy Requirements
# -----------------------------
COPY requirements.txt .

# -----------------------------
# Install Dependencies
# -----------------------------
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# -----------------------------
# Copy Project Files
# -----------------------------
COPY app ./app
COPY model ./model

# -----------------------------
# Set Working Directory to app
# -----------------------------
WORKDIR /app/app

# -----------------------------
# Expose FastAPI Port
# -----------------------------
EXPOSE 8000

# -----------------------------
# Start FastAPI Server
# -----------------------------
CMD [
    "uvicorn",
    "main:app",
    "--host",
    "0.0.0.0",
    "--port",
    "8000"
]
