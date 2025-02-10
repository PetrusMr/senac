valor_hora = float(input("Informe o valor recebido por hora: "))
hora = int(input("Informe o numero em horas trabalhadas por mês: "))

salario_bruto = valor_hora * hora

Imposto_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
liquido = salario_bruto -(inss + sindicato + Imposto_renda ) 

print(f"+Salário Bruto: R${salario_bruto} \n -IR (11%): R$:{Imposto_renda} \n -INSS(8%): R$:{inss} \n -Sindicato (5%): R${sindicato} \n = Salário Liquido   : R${liquido}  ")

