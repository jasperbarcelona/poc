FROM python:3.6

COPY requirements.txt ./mock_data/requirements.txt

COPY pldt_xls/ /pldt_xls/

RUN ls -la /pldt_xls/*

WORKDIR ./mock_data

RUN apt-get update && apt-get install -y python3-dev libmysqlclient-dev

RUN pip install -r requirements.txt