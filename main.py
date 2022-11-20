from ContaBancaria import ContaBancaria
from Especializacao import Especializacao

marcus1=ContaBancaria()
marcus1.setBanco("santander")
print(marcus1.getBanco())
marcus1.setAgencia("02394")
print(marcus1.getAgencia())
marcus1.setConta("imprimindo conta")
print(imarcus1.getConta())
marcus1.setTitular("marcus")
print(marcus1.getTitular())
marcus1.depositar(3000)
print(marcus1.getSaldo())

marcus2 = Especializacao()
marcus2.depositar(3000)
marcus2.setSaldoEspecial(500)
print(marcus2.getSaldoEspecial())
marcus2.sacar(400)
marcus2.__init__()
print(marcus2.getSaldo())