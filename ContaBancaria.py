class ContaBancaria:
  __banco = ""
  __agencia = ""
  __conta = ""
  __titular = ""
  __saldo = 0.0

  def ContaBancaria(self):
    print("criando Conta Bancaria")

  def getBanco(self):
    return self.__banco

  def setBanco(self, banco):
    self.__banco = banco

  def getAgencia(self):
    return self.__agencia

  def setAgencia(self, agencia):
    self.__agencia = agencia

  def getConta(self):
    return self.__conta

  def setConta(self, conta):
    self.__conta = conta

  def getTitular(self):
    return self.__titular

  def setTitular(self, titular):
    self.__titular = titular

  def getSaldo(self):
    return self.__saldo

  def depositar(self, valor):
    self.__saldo += valor

  def sacar(self, valor):
    if (getSaldo() >= self.valor):
      self.__saldo -= valor