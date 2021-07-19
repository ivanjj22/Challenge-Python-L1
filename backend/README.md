# Challenge Python L1 backend

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Installation

This program requires [Python](https://www.python.org/) v3.8+ to run.

Install the dependencies and devDependencies.

```sh
cd backend
pip install pipenv
pipenv installl
```

To execute from the cli...

```sh
pipenv run python app.py
```

## Run the server

### Run the server from the cli

```sh
pipenv run python server.py 8081
```

### Run using Docker

By default, the Docker will expose port 8081, so change this within the
Dockerfile if necessary. When ready, simply use the Dockerfile to
build the image.

```sh
cd backend
docker build -t python-test:latest .
```

This will create the image and pull in the necessary dependencies.

Once done, run the Docker image and map the port to whatever you wish on
your host. In this example, we simply map port 8081 of the host to
port 8081 of the Docker (or whatever port was exposed in the Dockerfile):

```sh
docker run -d -p 8081:8081 python-test:latest
```

Verify the deployment by navigating to your server address in
your preferred browser.

```sh
127.0.0.1:8001
```

## Testing

To run the test cases...

```sh
pipenv run python -m pytest
```

## License

MIT
