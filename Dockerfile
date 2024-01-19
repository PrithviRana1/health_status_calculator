FROM python:3.13.0a3
RUN mkdir /code 
COPY . /code
COPY pyproject.toml /code
WORKDIR /code
ENV PYTHONPATH=${PYTHONPATH}:${PWD} 
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install
EXPOSE 8000
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
