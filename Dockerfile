FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app
ADD docker-entrypoint.sh /app/
RUN chmod +x /app/docker-entrypoint.sh
ADD requirements.txt /app
RUN pip install --upgrade pip \
    && pip install uwsgi \
    && pip install -r /app/requirements.txt
ADD my_web_app /app/

EXPOSE 8000

CMD ["/app/docker-entrypoint.sh"]
