FROM python:3.6

RUN apt update
RUN apt install python3-pip -y

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 5002

ENTRYPOINT ["python3", "app.py"]