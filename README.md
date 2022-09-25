# Ormdantic Starter

[WIP] A starter template for Ormdantic, a Python ORM using Pydantic and SQLAlchemy.

## Project setup

```sh
# clone the repo
$ git clone https://github.com/yezz123/TodoList-Ormdantic-starter.git

# move to the project folder
$ cd TodoList-Ormdantic-starter
```

## Creating virtual environment

- Create a virtual environment using virtualenv.

```shell
# creating virtual environment
$ virtualenv venv

# activate virtual environment
$ source venv/bin/activate

# install all dependencies
$ pip install -r requirements.txt
```

### Running the Application

- To run the [Main](app/main.py) we need to use [uvicorn](https://www.uvicorn.org/) a lightning-fast ASGI server implementation, using uvloop and httptools.

```sh
# Running the application using uvicorn
$ uvicorn main:app --reload
```

## TODO

- [x] Setup Repository
- [x] Setup Routes & Schema
- [ ] Support all [Ormdantic features](https://github.com/yezz123/ormdantic)
  - [x] Create or Insert
  - [x] Delete
  - [x] Find Many
  - [ ] Find One
  - [ ] Update and Upsert
- [ ] Add Tests
- [ ] Add CI/CD
- [ ] Setup More Features
  - [ ] Authentication
  - [ ] Authorization
  - [ ] Pagination
  - [ ] Sorting
  - [ ] Filtering
  - [ ] Caching
  - [ ] Rate Limiting
  - [ ] Logging
  - [ ] Monitoring
  - [ ] Error Handling
  - [ ] Documentation
  - [ ] Deployment