FROM python:3.7.9-alpine3.12

ADD ./requirements.txt /app/requirements.txt

RUN set -ex \
    && apk add --no-cache --virtual .build-deps python3-dev postgresql-dev build-base \
    && python -m venv /env \
    && /env/bin/pip install --upgrade pip \
    && /env/bin/pip install --upgrade setuptools \
    && /env/bin/pip install wheel \
    && /env/bin/pip install --no-cache-dir -r /app/requirements.txt \
    && runDeps="$(scanelf --needed --nobanner --recursive /env \
        | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
        | sort -u \
        | xargs -r apk info --installed \
        | sort -u)" \
    && apk add --virtual rundeps $runDeps \
    && apk del .build-deps

ADD . /app
WORKDIR /app

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH
ENV DJANGO_SETTINGS_MODULE base.settings.prod

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "--threads", "6", "--worker-class", "gthread", "--timeout", "90", "--worker-tmp-dir", "/dev/shm", "base.wsgi:application"]