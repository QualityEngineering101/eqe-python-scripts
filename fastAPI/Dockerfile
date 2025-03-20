# Use Python 3.13.1 as the base image
FROM python:3.13.1

# Set the working directory inside the container
WORKDIR /app

# Copy the FastAPI project files
COPY fastAPI /app  

# Ensure tests are included
COPY fastAPI/tests /app/tests  

# Install dependencies
COPY fastAPI/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for FastAPI
EXPOSE 8000

# Run the FastAPI application with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
