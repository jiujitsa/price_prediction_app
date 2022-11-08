
FROM python:3.9

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
COPY ./xgb_r.pkl /app/xgb_r.pkl



RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app/app


CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "80"]

# docker build -t price_prediction_app .
# docker run -p 80:80 price_prediction_app
