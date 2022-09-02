FROM python:3.9.6
RUN apt-get updage && apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y build-essential

COPY . /app
ENV PATH=/usr/bin:$PATH
RUN pip3 freeze > requirements.txt
RUN pip3 install -r requirements.txt
WORKDIR /app
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]