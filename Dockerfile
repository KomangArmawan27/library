# Use an official Python runtime as a parent image
FROM python:3.9.6

# Set the working directory inside the container
WORKDIR /library

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container (excluding unnecessary files via .dockerignore)
COPY . .

# Expose the port Django runs on
EXPOSE 8000

# Run migrations and start the Django server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
