FROM python

ENV PYTHONUNBUFFERED=1

WORKDIR /my_project/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt











