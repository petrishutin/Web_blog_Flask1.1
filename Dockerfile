FROM tiangolo/uwsgi-nginx-flask:python3.7

WORKDIR /app

COPY project/requirements.txt .
RUN pip install -r requirements.txt

# Move the container's entrypoint to reuse it
RUN mv /entrypoint.sh /uwsgi-nginx-flask-entrypoint.sh
# Copy our entrypoint
COPY project/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY project/ .

EXPOSE 80

ENTRYPOINT ["/entrypoint.sh"]
CMD ["/start.sh"]
