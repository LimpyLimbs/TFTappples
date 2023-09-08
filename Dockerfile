# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 80 for Gunicorn
EXPOSE 80

# Define the command to run Gunicorn with your Flask app
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:80", "app:app"]