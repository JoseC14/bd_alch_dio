from sqlalchemy import select
from Tables import Cliente
from Tables import Conta
from Engine import get_engine


def lista_clientes():
    stmt = select(Cliente)
    conn = get_engine().connect()
    result = conn.execute(stmt)
    conn.commit()
    conn.close()
    return result


def lista_contas():
    stmt = select(Conta)
    conn = get_engine().connect()
    result = conn.execute(stmt)
    conn.commit()
    conn.close()
    return result

def lista_conta_cliente():
    stmt = select(Cliente.nome, Conta.tipo, Conta.agencia, Conta.saldo).join(Conta, Cliente.id == Conta.id_cliente)
    conn = get_engine().connect()
    result = conn.execute(stmt)
    conn.commit()
    conn.close()
    return result


for value in lista_clientes():
    print(value)

for value in lista_contas():
    print(value)

for value in lista_conta_cliente():
    print(value)

