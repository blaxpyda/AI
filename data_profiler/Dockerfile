FROM python:3.13-alpine

# set working directory
WORKDIR /app

#copy files to container
COPY requirements.txt .
COPY data_profiler.py .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# expose port
EXPOSE 8501

# run the application
CMD ["streamlit", "run", "data_profiler.py", "--server.port=8501"]