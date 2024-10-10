# Use the official Python image as a base image
FROM python:3.11-slim

# Set environment variables to avoid issues with Python writing bytecode
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory inside the container
WORKDIR /app

# Copy requirements.txt to the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code to the container
COPY . /app/


# Expose the port the app runs on
EXPOSE 8000

# Run Django's development server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
