FROM python:3.11.0b4-alpine3.15

WORKDIR /flaskApp
COPY . /flaskApp
RUN pip install -r requirements.txt
EXPOSE 5000

#ENTRYPOINT [ "python" ]

CMD ["python" , "app.py" ]


#CMD python ./app.py