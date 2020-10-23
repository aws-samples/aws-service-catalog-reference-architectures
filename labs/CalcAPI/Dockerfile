FROM centos:latest
MAINTAINER chpmanc@amazon.com 

RUN yum install -y python3-pip

RUN mkdir -p /flask-app
WORKDIR /flask-app
	
COPY flask/requirements.txt /flask-app/
COPY flask/application.py /flask-app/
COPY flask/gu.conf /flask-app/gu.py
COPY pytest.py /flask-app/
COPY start.sh /flask-app/
ADD  pycalc/ /flask-app/pycalc/
ADD  bin/ /flask-app/bin/
RUN pip3 install -r requirements.txt
RUN chmod +x start.sh

EXPOSE 80
ENTRYPOINT ["./start.sh"]


