FROM python:3.5
ENV PYTHONUNBUFFERED 1

RUN mkdir /web

ARG ENV

ADD requirements.txt /web

RUN pip install -r /web/requirements.txt
RUN groupadd -r django \
    && useradd -r -g django django

ADD . /web

COPY ./run.sh /run.sh

RUN chown -R django /web
RUN chmod 775 /run.sh

WORKDIR /web

EXPOSE 8000
