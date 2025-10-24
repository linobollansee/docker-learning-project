# Stage 1: Build stage
# Use a slim Python 3.11 image as the builder
FROM python:3.11-slim AS builder

# Set the working directory inside the container
WORKDIR /app

# Copy only the requirements file to leverage Docker cache
COPY app/requirements.txt .

# Install Python dependencies for the user (not system-wide)
RUN pip install --user -r requirements.txt


# Stage 2: Runtime stage
# Use a fresh slim Python 3.11 image for the final container
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy installed dependencies from the builder stage
COPY --from=builder /root/.local /root/.local

# Copy the application code into the container
COPY app/ .

# Add local Python binaries to PATH
ENV PATH=/root/.local/bin:$PATH

# Expose port 5000 for the application
EXPOSE 5000

# Define a healthcheck to verify the app is running
HEALTHCHECK --interval=10s --timeout=3s CMD curl -f http://localhost:5000/ || exit 1

# Command to run the application
CMD ["python", "main.py"]
