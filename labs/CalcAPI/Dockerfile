FROM centos:latest
MAINTAINER chpmanc@amazon.com 

RUN yum -y install epel-release && yum clean all
RUN yum install -y python2-pip

RUN mkdir -p /flask-app
WORKDIR /flask-app
	
COPY flask/requirements.txt /flask-app/
COPY flask/application.py /flask-app/
COPY flask/gu.conf /flask-app/
COPY pytest.py /flask-app/
COPY start.sh /flask-app/
ADD  pycalc/ /flask-app/pycalc/
ADD  bin/ /flask-app/bin/
RUN pip2 install --upgrade pip
RUN pip2 install -r requirements.txt
RUN chmod +x start.sh

EXPOSE 80
ENTRYPOINT ["./start.sh"]


