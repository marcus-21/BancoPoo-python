from ContaBancaria import ContaBancaria

class Especializacao(ContaBancaria):
  __saldoEspecial = 0.0

  def Especializacao(self):
    print("criando conta bancaria especial")

  def Especializacao(self, saldoEspecial):
    self.__saldoEspecial = saldoEspecial

  def getSaldoEspecial(self):
    return self.__saldoEspecial

  def setSaldoEspecial(self, saldoEspecial):
    self.__saldoEspecial = saldoEspecial

  def getSaldo(self):
    return super().getSaldo() + self.__saldoEspecial

  def sacar(self, valor):
    if (super().getSaldo() >= valor):
      self.sacar = valor
    else:
      println("Saldo Insuficiente")
def __init__(self):
   super().self.sacar()