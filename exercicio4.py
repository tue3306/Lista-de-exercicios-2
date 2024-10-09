# Exercício 4

from abc import ABC, abstractmethod

class ContaBancaria(ABC):
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass

    def exibir_informacoes(self):
        return f"Conta: {self.numero}, Titular: {self.titular}, Saldo: {self.saldo}"

class ContaCorrente(ContaBancaria):
    def __init__(self, numero, titular, saldo=0, limite=500):
        super().__init__(numero, titular, saldo)
        self.limite = limite

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo - valor >= -self.limite:
            self.saldo -= valor
        else:
            print("Saldo insuficiente com o limite disponível.")

class ContaPoupanca(ContaBancaria):
    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente. Operação não permitida.")

    def calcular_juros(self, taxa):
        self.saldo += self.saldo * taxa


cc = ContaCorrente(1234, "João", 1000)
cc.sacar(1200)
print(cc.exibir_informacoes())

cp = ContaPoupanca(5678, "Maria", 500)
cp.calcular_juros(0.05)
print(cp.exibir_informacoes())
