# Use Python 3.12.11 image
FROM python:3.12.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies (for pandas, torch, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    git \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libatlas-base-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy files
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip \
 && pip install -r requirements.txt

# Run the app
CMD ["python", "web.py"]
