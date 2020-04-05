FROM python:3

WORKDIR /usr/src/app

COPY requirements.in ./
RUN pip install --no-cache-dir -r requirements.in

COPY . .

CMD [ "python", "./run.py" ]