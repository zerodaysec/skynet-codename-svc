FROM python:3.12

WORKDIR /app

# NOTE: Using pip over pipenv
COPY requirements.txt /app/
RUN python -m pip install --no-cache-dir --requirement requirements.txt
COPY /app/ /app/

ENV FLASK_APP=app.py

ENTRYPOINT ["streamlit", "run", "app.py"]