FROM python:3.12.3-slim

# Set the working directory

WORKDIR /spreadAPI

# Copy the current directory contents into the container at /spreadAPI

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .

EXPOSE 4000

ENV FLASK_APP=app
CMD ["flask", "run", "--host=0.0.0.0", "--port=4000"]