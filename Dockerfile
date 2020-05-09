FROM python:3.7
EXPOSE 8888
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
ENTRYPOINT ["./start.sh"]