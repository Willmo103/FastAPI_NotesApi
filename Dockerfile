FROM python:3.10.7

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 4200:4200



CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "4200"]
