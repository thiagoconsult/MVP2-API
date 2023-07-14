# API TAREFA
Esta API foi desenvolvida para entrega do MVP da Sprint 2 da PUC-RIO. Ela foi desenvolvida em FastAPI para servir uma aplicação
desenvolvida em React.

### Esta API trás os seguintes métodos:

| Método           | Funcionalidade                            |
|------------------|-------------------------------------------|
| DELETE/tarefa    | Deleta uma tarefa por ID                  |
| POST/tarefa      | Cadastra uma nova tarefa                  |
| PUT/tarefa       | Atualiza o Status de uma tarefa existente |

# Como executar

Você precisa ter todas as libs utilizadas no projeto e que estão listadas no arquivo requirements.txt.

Para executar este projeto você poderá criar um ambiente virtual primeiramente e ativá-lo.

### Para instalar e ativar a virtual env no windows:

No windows, na raiz do projeto, exexute:
```
python -m venv env
```

Para ativar a env, execute:
```
env/Scripts/activate
```

### Instalando o projeto:

Quando a virtual env estiver ativa, irá aparecer antes do caminho do projeto no cmd o nome (env). Agora, é necessário instalar as libs:
```
pip install -r requirements.txt
```

### RESOLVENDO BUG DO VSCODE

Após executar o procedimento acima, feche a pasta do projeto e abra novamente, ou feche o VSCode e abra novamente, pois, só assim irá reconhecer as libs do FastAPI.


Para executar, se estiver utilizando o VSCode, abra o arquivo main.py e utilize o atalho CTRL+F5 ou se estiver utilizando outro IDE de desenvolvimento
procure nas opções do menu a opção de executar/rodar. Em seguida, abra o seu navegador e cole o endereço da API para ver a documentação:
```
http://127.0.0.1:8010/
```

Esta página permitirá explorar a documentação da API
