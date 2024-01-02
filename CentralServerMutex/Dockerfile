# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install Pyro4==4.82

# Make port 50000 available to the world outside this container
EXPOSE 50000

# Run app.py when the container launches
CMD ["python", "./update_file.py"]