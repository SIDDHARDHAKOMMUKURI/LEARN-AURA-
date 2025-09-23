# Use official Python slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements file first (for caching)
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose port (optional, if you run a webserver; Telegram bots usually don't need this)
# EXPOSE 8443

# Set environment variable to prevent Python from buffering stdout/stderr
ENV PYTHONUNBUFFERED=1

# Command to run the bot
CMD ["python", "main.py"]
