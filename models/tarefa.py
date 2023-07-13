from sqlmodel import SQLModel, Field
from pydantic import BaseModel
from typing import Optional, List
from datetime import date


class Tarefa(SQLModel, table=True):
    """
    Representação do Objeto Tarefa, que também será utilizado como Schema
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    data_criacao: Optional[date] = Field(default_factory=date.today, nullable=True)
    data_encerramento: Optional[date] = Field(nullable=True)
    titulo: str = Field(default=None, nullable=False, max_length=20)
    descricao: str = Field(default=None, nullable=False, max_length=200)
    status: Optional[int] = Field(default=1, nullable=True)

    '''Função utilizada sempre que uma terafa for encerrada, para gravar a data'''
    def atualiza_data_encerramento(self) -> date:
        self.data_encerramento = date.today()


class TarefaGet(SQLModel):
    id: int
    data_criacao: date
    data_encerramento: Optional[date]
    titulo: str
    descricao: str
    status: int


class TarefaUpdate(SQLModel):
    """
    Representação do Objeto Tarefa que será utilizado para o método PUT
    """
    status: Optional[int] = 2
    

class TarefaPost(SQLModel):
    titulo: str
    descricao: str

