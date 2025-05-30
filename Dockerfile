# FROM python:3.13-alpine

# ADD requirements.txt .

# ADD main.py .

# ADD .env .

# RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install streamlit

# CMD [ "python", "main.py" ]

# Use an official Python runtime as a parent image
FROM python:3.13-alpine

# Set working directory in the container
WORKDIR /app

# Copy requirements and app code
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# # Expose the Streamlit default port
# EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

