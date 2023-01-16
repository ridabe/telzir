FROM python:3.10
WORKDIR /telzir
COPY . /telzir

RUN pip install -r /telzir/requirements.txt
CMD python main.py