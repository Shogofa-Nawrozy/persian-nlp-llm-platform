# Use a lightweight Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements first to use Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your project into the container
COPY . .

# Expose the port Flask runs on
EXPOSE 5000

# Set the entrypoint to run the Flask app
CMD ["python", "app.py"]
