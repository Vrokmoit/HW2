FROM python

ENV APP /dz2/assistant

WORKDIR $APP

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python", "main.py"]