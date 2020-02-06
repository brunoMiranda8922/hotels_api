# REST API + FLASK

* API made to manage several hotels in memory.

##  Summary
1. [Stack]()
2. [Setup and init API]()
3. [Documentation]()
4. [Contribuiting]()
---
## Requirements
- [docker](https://www.docker.com/get-started)
- [docker-compose](https://docs.docker.com/compose/install/)
---

## Stack
-  Docker
-  Docker Compose
-  Python 2.7
-  Flask
-  Flask RESTFull

# Makefile

## Setup and init API
```sh
$    cp .env.example .env # you can edit if necessary
$    make start
```

## view all commands in makefile
```sh
$    make usage
```
---

## Endpoints

- GET   /hotels
- GET   /hotel/id
- POST  /hotel/id
- PUT   /hotel/id
- DELETE /hotel/id

## Documentation
- To speed up the use of API, use [postman requests collection](docs/postman/REST-API-FLASK.postman_collection.json)


## Contribuiting
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/rafaeldias98/python-customer-api/issues/new)

- If you find any problem or have a suggestion, please [open an issue](https://github.com/brunoMiranda8922/hotels_api/issues/new).
