# Use a slim Python base image for efficiency
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the app.py file into the container
COPY app.py .

# Install Python dependencies
RUN pip install --no-cache-dir dash==2.17.1 plotly==5.22.0 numpy==1.26.4 pandas==2.2.2 matplotlib==3.9.0

# Expose the port the app runs on
EXPOSE 8888

# Run the Dash app (note: you'll need to update the host to '0.0.0.0' in app.py for external access)
CMD ["python", "app.py"]