FROM python:3.13-alpine

# set up working directory
WORKDIR /app

# copy requirements file into the container
COPY requirements.txt .
COPY data_profiler.py .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

#Expose default streamlit port
EXPOSE 8501

# run the application
CMD ["streamlit", "run", "data_profiler.py", "--server.port=8501", "--server.enableCORS=false", "--server.headless=true"]