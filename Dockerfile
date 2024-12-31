# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose any ports the app needs (e.g., for Flask, we might expose 5000)
EXPOSE 5000

# Define the command to run your app (if it's a Flask app)
CMD ["python", "run.py"]
