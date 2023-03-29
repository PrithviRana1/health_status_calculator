FROM python:3.8
RUN mkdir /code 
COPY . /code
COPY pyproject.toml /code
WORKDIR /code
ENV PYTHONPATH=${PYTHONPATH}:${PWD} 
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

