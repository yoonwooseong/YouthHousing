FROM python:3.9-slim-buster
COPY . /app
WORKDIR /app
# ENV FLASK_APP hello
RUN python3 -m venv venv && . venv/bin/activate
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "-m", "flask", "run"]
CMD ["--host=0.0.0.0"]
