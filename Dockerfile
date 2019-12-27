FROM sptkl/docker-geosupport:19d

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

CMD ["python3", "app.py"]

EXPOSE 5000