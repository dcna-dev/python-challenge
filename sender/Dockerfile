FROM python:3.6-slim-jessie
COPY . /sender
WORKDIR /sender
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python -u sender.py
