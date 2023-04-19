from typing import List
from pydantic import BaseModel
from fastapi import FastAPI
from core import calculation
from database import loadDB

app = FastAPI()


class DataItem(BaseModel):
    owner: str
    repo: str
    base: str
    head: str
    apiV: str
    accept: str
    token: str


class DataList(BaseModel):
    data_list: List[DataItem]


@app.post("/")
async def health_status_score(data_list: DataList):

    data_list_parsed = [config.dict() for config in data_list.data_list]

    test = calculation.Calc(data_list_parsed)
    db = loadDB.DB()

    statuses = test.all_statuses()

    for status in statuses:
        db.load(status)

    response = {score: config for score, config in statuses}

    return {"statuses": response}
