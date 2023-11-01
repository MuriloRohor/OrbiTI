FROM python:3.11.4

WORKDIR /src

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /src

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]