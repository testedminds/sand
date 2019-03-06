FROM testedminds/python:3.7.1
MAINTAINER Bobby Norton <bobby@testedminds.com>
LABEL Description="Run SAND in a Jupyter Notebook"

RUN apt-get -y update && apt-get -y install pandoc

WORKDIR /opt/sand/
COPY . /opt/sand/

RUN pip install -r requirements.txt
RUN pip uninstall -y sand && pip install sand
