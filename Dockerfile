# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies (assuming requirements.txt exists)
RUN pip install --no-cache-dir -r requirements.txt

# Expose any necessary ports (this might vary depending on how the app works)
# EXPOSE <port_number>

# Command to run the application
# If there is a script to run (e.g., bombcheck.py), use the following command:
CMD ["python", "bombcheck.py"]
