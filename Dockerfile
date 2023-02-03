FROM python:3.9-slim-buster
COPY . /app
WORKDIR /app
# ENV FLASK_APP hello
RUN python3 -m venv venv && . venv/bin/activate
RUN apt-get -y update
RUN apt -y install wget
RUN apt -y install curl
RUN apt install unzip
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt -y install ./google-chrome-stable_current_amd64.deb
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/` curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN mkdir chrome
RUN unzip /tmp/chromedriver.zip chromedriver -d /app/chrome
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "-m", "flask", "run"]
CMD ["--host=0.0.0.0"]
