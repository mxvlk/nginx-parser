FROM python:slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD python main.py && python groff.py



