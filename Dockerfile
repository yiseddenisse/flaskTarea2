FROM python:3.10-alpine

WORKDIR /app

COPY . .

COPY requirements.txt .
# Instalar los requerimientos
RUN pip install -r requirements.txt

EXPOSE 5000


CMD ["python", "app.py"]
