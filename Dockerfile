# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Copy the dependencies file to the working directory
COPY requirements.txt /code/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Gunicorn
RUN pip install gunicorn

# Copy the rest of the application code to the working directory
COPY . /code/

# Collect static files
RUN python manage.py collectstatic --no-input

# Run the application using Gunicorn
CMD ["gunicorn", "blogms.wsgi:application", "--bind", "0.0.0.0:8000"]
