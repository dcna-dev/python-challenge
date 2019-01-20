FROM python:3.6-slim-jessie
COPY . /server
WORKDIR /server
RUN pip install -r requirements.txt
CMD python -u server.py
