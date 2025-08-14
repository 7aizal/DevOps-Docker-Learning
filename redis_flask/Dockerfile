# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY . .

# Install dependencies
RUN pip install flask redis

# Expose port 5000
EXPOSE 5000

# Run the app
CMD ["python", "count.py"]
