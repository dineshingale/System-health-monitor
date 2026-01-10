FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js 20
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs

WORKDIR /app

# Backend Setup
COPY requirements.txt .
RUN pip install -r requirements.txt

# Frontend Setup
COPY dashboard/package.json dashboard/package-lock.json ./dashboard/
RUN cd dashboard && npm install

# Copy entire repo
COPY . .

# Set permissions
RUN chmod +x entrypoint.sh

# Environment variables
ENV PYTHONUNBUFFERED=1
ENV VITE_API_URL=http://localhost:8000

ENTRYPOINT ["./entrypoint.sh"]
