# Use Python base image
FROM python:3.9-slim

# Set the working directory
# WORKDIR /app

# Copy the application files
COPY app/ /app

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose the Flask port
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app/main.py
# ENV OPENAI_API_KEY=your-openai-api-key

# Start the application
CMD ["python", "app/main.py"]
