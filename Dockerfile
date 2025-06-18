FROM python:3.10-slim

WORKDIR /app

# Copy requirements first to use Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Download Stanza models via Python script
RUN python -c "import stanza; stanza.download('fa')"

# Copy the rest of your project
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
