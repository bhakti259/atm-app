#base image
FROM python:3.11-slim
#working directory
WORKDIR /app
#copy
COPY . /app
#run
RUN pip install --no-cache-dir -r requirements.txt
#port
EXPOSE 5000
#command
CMD ["python", "app.py"]