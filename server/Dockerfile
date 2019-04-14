FROM python:onbuild

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ONBUILD COPY requirements.txt /usr/src/app/
ONBUILD RUN pip install --no-cache-dir -r requirements.txt

ONBUILD COPY . /usr/src/app

CMD ["/usr/local/bin/gunicorn", "wsgi:app", "-w", "2", "-b", "0.0.0.0:5000"]
