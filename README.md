# Devotionals API 

## Overview
This server was generated by the [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project. 

## Requirements
Python 3.6

MongoDB

## Usage
To run the server, make sure you have a MongoDB instance running locally on port 27017 and please execute the following from the root directory:

```
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python -m swagger_server
```

and open your browser to here:

```
http://localhost:8080/api/v1/ui/
```

Your Swagger definition lives here:

```
http://localhost:8080/api/v1/swagger.json
```

To run the tests
```
python setup.py test
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t swagger_server .
docker pull mongo:latest
# starting up a container
docker run --name devotionals_mongo -p 27017:27017  -d mongo
docker run --rm --name devotionals_api --link devotionals_mongo:localhost -p 8080:8080 swagger_server
```
