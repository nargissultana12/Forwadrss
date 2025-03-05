# Use Python base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose ports if needed (optional)
EXPOSE 80

# Run bot
CMD ["python", "main.py"]
