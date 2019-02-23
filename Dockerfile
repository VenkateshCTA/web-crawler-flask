FROM python:2.7
MAINTAINER Venkatesh Prasad "venkateshprasad143@gmail.com"
ADD . /gale
WORKDIR /gale
EXPOSE 5000
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "app.py"]
