FROM python:3.8-slim
WORKDIR /app
COPY . .

RUN pip install pipenv
RUN pipenv install --deploy --ignore-pipfile

EXPOSE 8081

CMD ["pipenv", "run", "python", "server.py", "8081"]