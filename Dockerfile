FROM python:3.12

WORKDIR /app

# TODO: Need to enable pipenv
COPY Pipfile /app/
COPY Pipfile.lock /app/
RUN python -m pip install pipenv \
    && pipenv sync
COPY /app/ /app/

ENV FLASK_APP=app.py

ENTRYPOINT ["pipenv","run","streamlit", "run", "app.py"]