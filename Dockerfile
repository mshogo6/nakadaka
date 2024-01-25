FROM python:3

WORKDIR /app

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE jp_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get install -y vim less
RUN apt-get install -y apache2
RUN apt-get install -y apache2-dev

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install --upgrade Flask
RUN pip install --upgrade mod_wsgi

CMD ["apachectl", "-D", "FOREGROUND"]
