FROM "amazon/aws-lambda-python"


WORKDIR '/var/task'
COPY src/* .
RUN pip install --no-cache-dir -r requirements.txt



CMD ["src/index.handler"]