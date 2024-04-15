from fastapi import FastAPI
from pydantic import BaseModel
import asyncio
from contaAzul import rpa


class data(BaseModel):
    type: str
    cnpj: str
    namEmp: str
    name: str
    num_exec: int


app = FastAPI()


@app.post('/')
async def main(data: data):
    timeout = 120
    try:
        type = data.type
        cnpj = data.cnpj
        namEmp = data.namEmp
        closer = data.name
        exec = data.num_exec
        bot = await asyncio.wait_for(
            rpa.alterCloser(
                name=closer,
                namEmp=namEmp,
                cnpj=cnpj,
            ), timeout=timeout
        )
        return {
            'message': f'{bot}'
        }

    except asyncio.TimeoutError:
        return {
            'message': '''Timeout Error, O bot excedeu o tempo limite'''
        }


