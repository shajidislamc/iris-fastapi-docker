# Python Base Image 
FROM python:3.11-slim
# Set working directory
WORKDIR /app
# Copy requirements file and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY ./app ./app
COPY ./model ./model

# Run FastAPI app
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","7860"]
