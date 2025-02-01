FROM redhat/ubi8:8.10
WORKDIR /mycode
COPY app.py .
RUN yum install python3.9 -y
RUN pip3 install flask
ENTRYPOINT ["python3","app.py"]
