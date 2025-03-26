preco = float(input('Qual é o valor do produto? R$'))
desc = preco * 0.05
calc = preco - desc
print('O produto que custava R${}, com o desconto de 5% passou a custar R${:.2f}'.format(preco, calc))