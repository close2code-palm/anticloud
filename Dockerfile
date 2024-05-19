FROM python:3.11
LABEL authors="Acer"

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY /src/anticloud /app

CMD ["uvicorn", "--factory", "main:app_factory", "--host", "0.0.0.0", "--port", "8000"]
