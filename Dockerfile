FROM python:3.8

WORKDIR /app

COPY main.py player.py ia.py ./

CMD ["python", "./main.py"]