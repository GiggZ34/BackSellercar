FROM python:3.12.6-slim

WORKDIR /app

COPY requirements.txt /requirements.txt

RUN apt update && apt -y install git zsh curl

RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

RUN pip install --no-cache-dir -r /requirements.txt


EXPOSE ${PORT}

CMD ["sh", "-c", "python3 manage.py runserver 0.0.0.0:${PORT}"]
