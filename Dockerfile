FROM python:3.12.3-slim

WORKDIR /spreadAPI

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .

EXPOSE 4000

ENV FLASK_APP=app
CMD ["flask", "run", "--host=0.0.0.0", "--port=4000"]