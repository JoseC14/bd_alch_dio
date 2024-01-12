from sqlalchemy.orm import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DECIMAL
from sqlalchemy import ForeignKey
from Engine import get_engine

Base = declarative_base()


class Cliente(Base):

    __tablename__ = 'cliente'

    id = Column(Integer, nullable=False, primary_key=True)
    nome = Column(String(130), nullable=False)
    endereco = Column(String(100), nullable=False)
    cpf = Column(String(12), nullable=False)


class Conta(Base):

    __tablename__ = 'conta'

    id = Column(Integer, nullable=False, primary_key=True)
    tipo = Column(String(50), nullable=False)
    agencia = Column(String(5), nullable=False)
    num = Column(String(12), nullable=False)
    saldo = Column(DECIMAL(10,3), nullable=False)
    id_cliente = Column(ForeignKey('cliente.id'), nullable=False)


Base.metadata.create_all(get_engine())
