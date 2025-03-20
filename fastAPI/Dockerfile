# Use Python 3.13.1 as the base image
FROM python:3.13.1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI app code
COPY app /app

# Ensure tests directory is explicitly copied (just to be safe)
COPY tests /app/tests

# Expose port 8000 for FastAPI
EXPOSE 8000

# Run the FastAPI application with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
