from fastapi import FastAPI, status, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import select
from models.tarefa import Tarefa, TarefaUpdate, TarefaPost,TarefaGet
from database.db import session
from typing import List
from sqlalchemy.exc import IntegrityError
from datetime import date


#############################################################################
# Instanciação da API
#############################################################################
app = FastAPI(
    title='API de Tarefas',
    version='0.1.0',
    description='API para gestão de Tarefas do dia a dia'
)


#############################################################################
# Traramento de CORS Cross-Origin Resource Sharing
#############################################################################
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#############################################################################
# GET - Redirecionamento da raiz para a documentação
#############################################################################
@app.get(
    '/',
    summary='Documentação',
    description='Documentação técnica da API',
    tags=['Documentação']
)
def redirect_docs():
    return RedirectResponse('/docs')


#############################################################################
# POST - Inclusão de nova tarefa
#############################################################################
@app.post(
        '/tarefa',
        summary='POST Tarefa',
        description='Método para inclusão de tarefa',
        tags=["Tarefa"],
        status_code=status.HTTP_201_CREATED,
        response_model=Tarefa
)
async def post_tarefa(body: TarefaPost):
    new_tarefa = Tarefa(
        titulo=body.titulo,
        descricao=body.descricao
    )
    try:
        session.add(new_tarefa)
        session.commit()
        return new_tarefa
    except Exception as e: 
        session.rollback()
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail= f"Não foi possível concluir a inclusão {e.args}")
        
        
#############################################################################
# GET - Lista de Tarefas
#############################################################################
@app.get(
    '/tarefas',
    summary='GET Lista de Tarefas',
    description='Método para busca de lista de tarefas',
    tags=["Tarefa"],
    status_code=status.HTTP_200_OK,
    response_model=List[TarefaGet]
)
async def get_lista_terefa():
    tarefas = session.exec(select(Tarefa)).all()

    return tarefas


#############################################################################
# PUT - Update Tarefa por ID
#############################################################################
@app.put(
    '/tarefa/update/{tarefa_id}',
    summary='Update Tarefa por ID',
    description='Método para atualizar uma tarefa pelo ID',
    tags=["Tarefa"],
    status_code=status.HTTP_202_ACCEPTED,
    response_model=Tarefa
)
def update_tarefa(tarefa_id: int, body: TarefaUpdate):
   
    tarefa = session.get(Tarefa, {tarefa_id})

    # tarefa.titulo=body.titulo or tarefa.titulo
    # tarefa.descricao=body.descricao or tarefa.descricao
    # tarefa.data_encerramento=body.data_encerramento or tarefa.data_encerramento
    tarefa.status=body.status
    # tarefa.data_encerramento=date.today

    if tarefa.status == 2:
        tarefa.atualiza_data_encerramento()
    session.add(tarefa)
    session.commit()

    return tarefa


#############################################################################
# DELETE - Tarefa por ID
#############################################################################
@app.delete(
    '/tarefa/delete/{tarefa_id}',
    summary='Delete Tarefa por ID',
    description='Método para deletar uma tarefa pelo ID',
    tags=["Tarefa"],
    status_code=status.HTTP_202_ACCEPTED,
    response_model=Tarefa
)
async def update_tarefa(tarefa_id: int):
    tarefa = session.get(Tarefa, {tarefa_id})

    try:
        session.delete(tarefa)
        session.commit()
        return tarefa
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'Tarefa não encontrada')
    

#############################################################################
# Execução da API
#############################################################################
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=8010, reload=True)
