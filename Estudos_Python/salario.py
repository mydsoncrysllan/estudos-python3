salario = float(input('Qual o sálario do funcionário? '))
aumento = salario + (salario * 0.15)
print('O salário de R${} com o aumento de 15% passou a ser R${:.2f}'.format(salario, aumento))