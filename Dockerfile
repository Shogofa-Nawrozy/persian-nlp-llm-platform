FROM python:3.10-slim

WORKDIR /app

# Copy requirements first to use Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your project (including static and templates)
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]