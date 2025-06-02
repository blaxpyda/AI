FROM python:3.13-alpine

# set up working directory
WORKDIR /app

# copy files into the container
COPY requirements.txt .
COPY loan-imeline.py .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# expose the port
EXPOSE 8501

# run the application
CMD ["streamlit", "run", "loan-imeline.py", "--server.port=8501"]