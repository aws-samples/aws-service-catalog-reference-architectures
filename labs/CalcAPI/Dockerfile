FROM public.ecr.aws/amazonlinux/amazonlinux:latest
MAINTAINER chpmanc@amazon.com 

RUN yum install -y python3-pip
#RUN yum update -y

RUN mkdir -p /flask-app
WORKDIR /flask-app
	
COPY flaskapp /flask-app
WORKDIR /flask-app
COPY flask/gu.conf /flask-app/gu.py
COPY pytest.py /flask-app/
COPY start.sh /flask-app/
RUN pip3 install -r requirements.txt
RUN chmod +x start.sh

EXPOSE 80
ENTRYPOINT ["./start.sh"]