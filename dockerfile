FROM "amazon/aws-lambda-python"


WORKDIR '/var/task/bot'
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY bot .
COPY config config


CMD ["bot.index.handler"]