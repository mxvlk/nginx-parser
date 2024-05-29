FROM ubuntu:latest

WORKDIR /app

RUN apt update

RUN apt install groff -y

CMD groff -ms -Tpdf ./output/output_groff.ms > ./output/docu.pdf