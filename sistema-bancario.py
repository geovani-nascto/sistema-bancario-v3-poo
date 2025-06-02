from abc import ABC


class Conta:
    pass

class ContaCorrente(Conta):
    pass

class Cliente:
    pass

class PessoaFisica(Cliente):
    pass

class Historico:
    pass

class Transacao(ABC):
    pass

class Deposito(Transacao):
    pass

class Saque(Transacao):
    pass

