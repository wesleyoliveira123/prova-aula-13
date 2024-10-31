class ContaBancaria:
    def __init__(self,saldo:float,titular:str):
        self.saldo=saldo
        self.titular=titular

    def depositar(self,valor):
        if valor >0:
            self.saldo+=valor
            return f"o valor de {valor} foi depositado em sua conta com sucesso!"
        else:
            return f"tente um valor valido!"

    def sacar(self,valor):
        if valor <=self.saldo:
            self.saldo-=valor
            return f"o valor de {valor} foi sacado de sua conta com sucesso!"
        else:
            return f"esse valor nao existe em sua conta! tente um valor mais baixo."

    def exibir_saldo(self):
        return f"existe o saldo de {self.saldo} em sua conta"

conta1=ContaBancaria(1000,"wesley alves de oliveira")

print(conta1.exibir_saldo())
print(conta1.sacar(500))
print(conta1.exibir_saldo())
print(conta1.sacar(501))
print(conta1.depositar(500))
print(conta1.exibir_saldo())