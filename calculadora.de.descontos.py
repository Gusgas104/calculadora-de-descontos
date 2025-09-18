print('=' * 25)
print('CALCULADORA DE PREÇOS')
print('=' * 25)

produto_nome = input('Qual produto você deseja comprar? ')
print('O produto escolhido foi: {}'.format(produto_nome))

preço = float(input('Qual é o valor desse produto? R$'))

print('FORMAS DE PAGAMENTOS:')
print('[1] Pagamento á vista')
print('[2] Pagamento com o cartão de crédito')

pagamento = input('Qual vai ser a forma de pagamento? ')

if pagamento == '1':
   novo = preço - (preço * 10/100)
   print('O produto que custava R${:.2f} pagamando á vista tem um desconto de 10%, vai custar R${:.2f}'.format(preço, novo))
elif pagamento == '2':
   parcelas = int(input('Quantas parcelas pretende dividir? '))
   valor_parcela = preço / parcelas
   print('O produto será parcelado em {}x de R${:.2f} sem juros'.format(parcelas, valor_parcela))
print('='*55)


