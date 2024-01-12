from sqlalchemy import insert
from Tables import Cliente
from Tables import Conta
from Engine import get_engine


def cad_cliente(nome, endereco, cpf):
    try:
        stmt = insert(Cliente).values(nome=nome, endereco=endereco, cpf=cpf)
        conn = get_engine().connect()
        result = conn.execute(stmt)
        conn.commit()
        print("Cliente inserido com sucesso")

    except Exception as e:
        print(f"Erro ao inserir cliente: {e}")


def cad_conta(tipo, agencia, num, saldo, id_cliente):
    try:
        stmt = insert(Conta).values(tipo=tipo, agencia=agencia, num=num, saldo=saldo, id_cliente=id_cliente)
        conn = get_engine().connect()
        result = conn.execute(stmt)
        conn.commit()
        print("Conta inserida com sucesso")

    except Exception as e:
        print(f"Erro ao inserir conta: {e}")


# cad_cliente("José Carlos","Sitio","1234567890")
# cad_conta("Corrente", "0001", "1234567890", 0,1)

