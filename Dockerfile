FROM python:3.8-slim-buster

WORKDIR /app

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt ./

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

ENTRYPOINT [ "python3" ]

CMD [ "runserver.py" ]
