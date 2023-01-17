FROM python:3.10

COPY . .
expose 5000

RUN pip install -r requirements.txt
ENTRYPOINT ["python", "main.py"]