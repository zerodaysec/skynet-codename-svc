FROM python:3.12

EXPOSE 8501

WORKDIR /app

COPY Pipfile* /app/

RUN pip install pipenv && pipenv sync

COPY app.py /app/

ENTRYPOINT [ "pipenv", "run", "streamlit", "run", "app.py" ]