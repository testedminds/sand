FROM testedminds/python:3.7.1
MAINTAINER Bobby Norton <bobby@testedminds.com>
LABEL Description="Run SAND in a Jupyter Notebook"

WORKDIR /opt/sand/
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install sand
