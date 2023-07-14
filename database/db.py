from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy_utils import database_exists

db_nome = "database.sqlite3"
db_url = f"sqlite:///database/{db_nome}"

engine = create_engine(db_url, echo=False, connect_args={"check_same_thread": False})

session = Session(engine)

if not database_exists(engine.url):
    SQLModel.metadata.create_all(engine)
