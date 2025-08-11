from abc import ABC, abstractmethod
from datetime import datetime

class Usuario:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def efetuar_transacao(self, conta, transacao):
        transacao.executar(conta)

    def incluir_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Usuario):
    def __init__(self, nome, nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf

class ContaBancaria:
    def __init__(self, numero, usuario):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._usuario = usuario
        self._historico = HistoricoConta()

    @classmethod
    def criar_conta(cls, usuario, numero):
        return cls(numero, usuario)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def usuario(self):
        return self._usuario

    @property
    def historico(self):
        return self._historico

    def saque(self, quantia):
        if quantia > self.saldo:
            print("\n[x] Falha: saldo insuficiente.")
        elif quantia > 0:
            self._saldo -= quantia
            print("\n[✓] Saque efetuado!")
            return True
        else:
            print("\n[x] Valor de saque inválido.")
        return False

    def deposito(self, quantia):
        if quantia > 0:
            self._saldo += quantia
            print("\n[✓] Depósito realizado!")
            return True
        else:
            print("\n[x] Valor do depósito inválido.")
            return False

class ContaCorrente(ContaBancaria):
    def __init__(self, numero, usuario, limite=500, max_saques=3):
        super().__init__(numero, usuario)
        self.limite = limite
        self.max_saques = max_saques

    def saque(self, quantia):
        saques_realizados = len([
            t for t in self.historico.transacoes if t["tipo"] == Saque.__name__
        ])
        if quantia > self.limite:
            print("\n[x] Limite de saque excedido.")
        elif saques_realizados >= self.max_saques:
            print("\n[x] Limite diário de saques atingido.")
        else:
            return super().saque(quantia)
        return False

    def __str__(self):
        return (
            f"Agência: {self.agencia}\n"
            f"Conta: {self.numero}\n"
            f"Titular: {self.usuario.nome}"
        )

class HistoricoConta:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def registrar_transacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        })

class Operacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def executar(self, conta):
        pass

class Saque(Operacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def executar(self, conta):
        if conta.saque(self.valor):
            conta.historico.registrar_transacao(self)

class Deposito(Operacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def executar(self, conta):
        if conta.deposito(self.valor):
            conta.historico.registrar_transacao(self)