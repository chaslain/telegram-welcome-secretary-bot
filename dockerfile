FROM "amazon/aws-lambda-python"


WORKDIR '/var/task'
COPY bot .
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt



CMD ["bot/index.handler"]