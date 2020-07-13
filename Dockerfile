FROM tiangolo/uwsgi-nginx-flask:python3.7

WORKDIR /app

COPY project/requirements.txt .
RUN pip install -r requirements.txt

COPY project/ .

EXPOSE 80