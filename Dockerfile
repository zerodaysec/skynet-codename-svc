FROM python:3.11

WORKDIR /app

# TODO: Need to enable pipenv
# COPY requirements.txt /app/
COPY app.py /app/

ENV FLASK_APP=app.py

ENTRYPOINT ["flask", "run"]