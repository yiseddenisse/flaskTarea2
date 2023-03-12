FROM python:3.10-alpine

WORKDIR /app

COPY . .

# Instalar los requerimientos
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000


CMD ["python", "app.py"]
