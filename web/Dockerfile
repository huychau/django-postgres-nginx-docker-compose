FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir /web

ARG ENV

ADD requirements.txt /web

RUN pip install -r /web/requirements.txt
RUN groupadd -r django \
    && useradd -r -g django django

ADD . /web

COPY ./bin /bin

RUN chown -R django /web
RUN chmod +x /bin/*.sh

WORKDIR /web

EXPOSE 8000
