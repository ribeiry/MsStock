FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install --only-binary :all: fastapi[all]
RUN pip install -r requirements.txt


CMD cd /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
